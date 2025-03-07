from pandera.typing import DataFrame
from typing import List, Dict
import geopandas as gpd
import pandera as pa
import pandas as pd
import numpy as np

from .constants import GeospatialConstants
from .processor import CoordinateProcessor
from .exceptions import ELRExceptionEnum
from .mileage import MileageCalculator
from .validator import InputValidator
from .loader import ELRDataLoader

from ..models import DataframeWithElrMileages27700



class ELRMileageCalculationService:
    """Service class for calculating ELR mileages for geographic points."""

    def __init__(self, elr_data_path: str = "cross_locs/data/elrs.pkl"):
        """
        Initialize the service.

        Parameters
        ----------
        elr_data_path : str
            Path to the ELR reference data file
        """
        self.elr_data_path = elr_data_path
        self.constants = GeospatialConstants()

    def process_dataframe(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Process the input GeoDataFrame to calculate ELR mileages.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame with geometries

        Returns
        -------
        gpd.GeoDataFrame
            GeoDataFrame with calculated ELR mileages

        Raises
        ------
        ValueError
            If input validation fails
        """
        # Validate input
        InputValidator.validate_input_dataframe(gdf, DataframeWithElrMileages27700)

        # Add ID column for tracking
        gdf = gdf.copy()
        gdf.loc[:, "_id"] = range(len(gdf))

        # Process special coordinate cases
        special_point_ids = self._process_special_coordinates(gdf)

        # Join with ELR data
        gdf = self._join_with_elr_data(gdf)

        # Calculate mileages
        gdf = self._calculate_mileages(gdf)

        # Apply filters and mark exceptions
        gdf = self._apply_filters(gdf, special_point_ids)

        # Format output
        gdf = self._format_output(gdf)

        return gdf

    def _process_special_coordinates(
        self, gdf: gpd.GeoDataFrame
    ) -> Dict[str, List[int]]:
        """
        Process all special coordinate cases.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame

        Returns
        -------
        Dict[str, List[int]]
            Dictionary of special point IDs by category
        """
        processor = CoordinateProcessor
        constants = GeospatialConstants

        # Process null coordinates
        gdf, null_coords_ids = processor.process_special_coordinates(
            gdf, constants.NULL_COORDS_POINT
        )

        # Process infinite coordinates
        gdf, infinite_coords_ids = processor.process_special_coordinates(
            gdf, constants.INFINITE_POINT
        )

        # Process origin coordinates
        gdf, origin_coords_ids = processor.process_special_coordinates(
            gdf, constants.ORIGIN_POINT
        )

        # Process empty coordinates
        gdf, empty_coords_ids = processor.process_special_coordinates(
            gdf, constants.EMPTY_POINT
        )

        return {
            "NULL_COORDS": null_coords_ids,
            "WRONG_COORDS": infinite_coords_ids,
            "ORIGIN_COORDS": origin_coords_ids,
            "EMPTY_COORDS": empty_coords_ids,
        }

    def _join_with_elr_data(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Join the input GeoDataFrame with ELR reference data.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame

        Returns
        -------
        gpd.GeoDataFrame
            Joined GeoDataFrame

        Raises
        ------
        ValueError
            If geospatial join fails
        """
        # Load ELR reference data
        elrs = ELRDataLoader.load_elr_data(self.elr_data_path)

        # Perform spatial join
        joined_gdf = gdf.sjoin_nearest(
            elrs,
            distance_col="_distance",
        )

        if len(joined_gdf) == 0:
            raise ValueError("Geospatial join failed to find any matches.")

        # Rename ELR column
        joined_gdf = joined_gdf.rename(columns={"ELR": "_elr"})

        return joined_gdf

    def _calculate_mileages(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Calculate relative and absolute mileages.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame after joining with ELR data

        Returns
        -------
        gpd.GeoDataFrame
            GeoDataFrame with calculated mileages
        """
        calculator = MileageCalculator

        # Calculate relative mileage
        gdf.loc[:, "_relative_mileage"] = calculator.adjust_mileage(gdf)

        # Calculate absolute mileage
        gdf.loc[:, "_mileage"] = gdf.apply(
            lambda x: calculator.find_absolute_mileage(
                start=x["L_M_FROM"],
                end=x["L_M_TO"],
                dr=x["_relative_mileage"],
            ),
            axis=1,
        )

        # Remove duplicate matches for the same point
        gdf = gdf.drop_duplicates(subset=["_id"], keep="first")

        return gdf

    def _apply_filters(
        self, gdf: gpd.GeoDataFrame, special_point_ids: Dict[str, List[int]]
    ) -> gpd.GeoDataFrame:
        """
        Apply filters and mark exceptions.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame
        special_point_ids : Dict[str, List[int]]
            Dictionary of special point IDs by category

        Returns
        -------
        gpd.GeoDataFrame
            Filtered GeoDataFrame
        """
        # Filter far points
        gdf = CoordinateProcessor.filter_far_points(gdf)

        # Filter Irish assets
        gdf = CoordinateProcessor.filter_irish_assets(gdf)

        # Mark special coordinate points
        for exception_type, ids in special_point_ids.items():
            if ids:
                gdf.loc[
                    gdf["_id"].isin(ids),
                    ["_elr", "_mileage"],
                ] = [exception_type, np.nan]

        return gdf

    def _format_output(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Format the output GeoDataFrame.

        Parameters
        ----------
        gdf : gpd.GeoDataFrame
            Input GeoDataFrame

        Returns
        -------
        gpd.GeoDataFrame
            Formatted GeoDataFrame
        """
        # Extract exception codes
        exception_codes = [e.name for e in ELRExceptionEnum]

        # Set _elr_exception column
        gdf.loc[:, "_elr_exception"] = gdf["_elr"].apply(
            lambda x: x if x in exception_codes else np.nan
        )

        # Clean up _elr column
        gdf["_elr"] = gdf["_elr"].apply(
            lambda x: x if x not in exception_codes else np.nan
        )

        # Set message and error columns
        gdf.loc[:, "_message"] = gdf["_elr_exception"].apply(
            lambda x: (
                f"{ELRExceptionEnum[x].message} Docs Reference: {ELRExceptionEnum[x].ref}"
                if not pd.isna(x)
                else np.nan
            )
        )

        gdf.loc[:, "_error"] = gdf["_elr_exception"].apply(
            lambda x: True if not pd.isna(x) else False
        )

        # Drop temporary columns
        gdf = gdf.drop(columns=["index_right", "_id", "_saved_geom", "L_M_FROM", "L_M_TO"])

        return gdf


@pa.check_types
def get_elr_mileages(gdf: gpd.GeoDataFrame) -> DataFrame[DataframeWithElrMileages27700]:
    """
    Calculate ELR mileages for geographical points. It adds columns:
    
    - `_elr`: ELR code
    - `_mileage`: Mileage value (in miles)
    - `_relative_mileage`: Relative mileage value
    - `_elr_exception`: Exception code
    - `_message`: Exception message
    - `_error`: Error flag

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        Input GeoDataFrame with geometries in EPSG:27700

    Returns
    -------
    DataFrame[DataframeWithElrMileages27700]
        DataFrame with calculated ELR mileages

    Raises
    ------
    ValueError
        If validation fails or processing encounters errors
    """
    service = ELRMileageCalculationService()
    return service.process_dataframe(gdf)
