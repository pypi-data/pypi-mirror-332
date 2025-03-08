from shapely.geometry import Point
from typing import List, Tuple
import geopandas as gpd
import numpy as np

from .constants import GeospatialConstants


class CoordinateProcessor:
    """Processes and filters coordinates in a GeoDataFrame."""

    @staticmethod
    def filter_points_by_condition(
        gdf: gpd.GeoDataFrame, condition: Point
    ) -> List[int]:
        """
        Filter points by a specific condition.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame
        condition : Point
            Point condition to filter by

        Returns
        -------
        List[int]
            List of row IDs matching the condition
        """
        return gdf[gdf["geometry"] == condition]["_id"].tolist()

    @staticmethod
    def process_special_coordinates(
        gdf: gpd.GeoDataFrame, condition: Point
    ) -> Tuple[gpd.GeoDataFrame, List[int]]:
        """
        Process points with special coordinate conditions.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame
        condition : Point
            Point condition to filter by

        Returns
        -------
        Tuple[gpd.GeoDataFrame, List[int]]
            Modified GeoDataFrame and list of IDs for filtered points
        """
        matched_ids = CoordinateProcessor.filter_points_by_condition(gdf, condition)

        # Replace matched points with zero coordinates
        if matched_ids:
            gdf.loc[
                gdf["geometry"] == condition,
                ["geometry"],
            ] = Point(0, 0)

        return gdf, matched_ids

    @staticmethod
    def filter_irish_assets(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Filter and label Irish assets in the GeoDataFrame.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame

        Returns
        -------
        gpd.GeoDataFrame
            Modified GeoDataFrame with Irish assets labeled
        """
        const = GeospatialConstants
        irish_mask = (
            (gdf.geometry.x > const.IRISH_X_MIN)
            & (gdf.geometry.x < const.IRISH_X_MAX)
            & (gdf.geometry.y > const.IRISH_Y_MIN)
            & (gdf.geometry.y < const.IRISH_Y_MAX)
        )

        gdf.loc[irish_mask, ["_elr", "_mileage"]] = ["IRISH", np.nan]
        return gdf

    @staticmethod
    def filter_far_points(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Filter and label points that exceed the far coordinates threshold.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame

        Returns
        -------
        gpd.GeoDataFrame
            Modified GeoDataFrame with far points labeled
        """
        far_mask = gdf["_distance"] > GeospatialConstants.FAR_COORDS_THRESHOLD_M
        gdf.loc[far_mask, ["_elr", "_mileage"]] = ["FAR_COORDS", np.nan]
        return gdf
