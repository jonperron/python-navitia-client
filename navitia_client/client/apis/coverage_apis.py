from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.administrative_region import Region
from navitia_client.entities.pagination import Pagination


class CoverageApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching coverage area information.

    See https://doc.navitia.io/#coverage

    Methods
    -------
    _get_regions_from_response(raw_regions_response: Any) -> Sequence[Region]
        A static method to transform raw API response data into a list of Region objects.

    list_covered_areas(start_page: int = 0, count: int = 25) -> Tuple[Sequence[Region], Pagination]
        Retrieves a list of covered areas from the Navitia API.

    get_coverage_by_region_id(region_id: str, start_page: int = 0, count: int = 25) -> Tuple[Sequence[Region], Pagination]
        Retrieves information about a specific region by its ID.

    get_coverage_by_region_coordinates_and_coordinates(lon: float, lat: float, start_page: int = 0, count: int = 25) -> Tuple[Sequence[Region], Pagination]
        Retrieves information about a region based on coordinates.
    """

    @staticmethod
    def _get_regions_from_response(raw_regions_response: Any) -> Sequence[Region]:
        """
        Converts raw response data into a list of Region objects.

        Parameters
        ----------
        raw_regions_response : Any
            The raw response data from the API containing regions' information.

        Returns
        -------
        Sequence[Region]
            A list of Region objects created from the raw response data.
        """
        regions = []
        for region_data in raw_regions_response:
            regions.append(Region.from_payload(region_data))
        return regions

    def list_covered_areas(
        self, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Region], Pagination]:
        """
        Retrieves a list of covered areas from the Navitia API.

        Parameters
        ----------
        start_page : int, optional
            The starting page for pagination (default is 0).
        count : int, optional
            The number of regions to fetch per page (default is 25).

        Returns
        -------
        Tuple[Sequence[Region], Pagination]
            A tuple containing a list of Region objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage?start_page={start_page}&count={count}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        pagination = Pagination.from_payload(results.json()["pagination"])
        return regions, pagination

    def get_coverage_by_region_id(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Region], Pagination]:
        """
        Retrieves information about a specific region by its ID.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch information about.
        start_page : int, optional
            The starting page for pagination (default is 0).
        count : int, optional
            The number of regions to fetch per page (default is 25).

        Returns
        -------
        Tuple[Sequence[Region], Pagination]
            A tuple containing a list of Region objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}?start_page={start_page}&count={count}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        pagination = Pagination.from_payload(results.json()["pagination"])
        return regions, pagination

    def get_coverage_by_region_coordinates_and_coordinates(
        self, lon: float, lat: float, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Region], Pagination]:
        """
        Retrieves information about a region based on coordinates.

        Parameters
        ----------
        lon : float
            The longitude of the location to fetch information about.
        lat : float
            The latitude of the location to fetch information about.
        start_page : int, optional
            The starting page for pagination (default is 0).
        count : int, optional
            The number of regions to fetch per page (default is 25).

        Returns
        -------
        Tuple[Sequence[Region], Pagination]
            A tuple containing a list of Region objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}?start_page={start_page}&count={count}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        pagination = Pagination.from_payload(results.json()["pagination"])
        return regions, pagination
