from typing import Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.freefloatings_nearby import (
    FreefloatingsNearbyRequest,
)
from navitia_client.entities.response.free_floating import FreeFloating
from navitia_client.entities.response import Pagination


class FreefloatingsNearbyApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching nearby free-floating vehicles.

    See https://doc.navitia.io/#freefloatings-nearby-api

    Methods
    -------
    _get_freefloatings_nearby(
        url: str, filters: dict
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        Retrieves free-floating vehicles from the Navitia API based on provided URL and filters.

    list_freefloatings_nearby(
        region_id: str,
        lon: float,
        lat: float,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        Retrieves free-floating vehicles near coordinates in a specific region from the Navitia API.

    list_freefloatings_nearby_with_resource_path(
        region_id: str,
        resource_path: str,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        Retrieves free-floating vehicles near a specific resource path in a region from the Navitia API.

    list_freefloatings_nearby_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        Retrieves free-floating vehicles near coordinates, navitia guesses the region from coordinates.

    list_freefloatings_nearby_by_coordinates_only(
        lon: float,
        lat: float,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        Retrieves free-floating vehicles near coordinates without any region id.
    """

    def _get_freefloatings_nearby(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """
        Retrieves free-floating vehicles from the Navitia API based on provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to apply to the API request.

        Returns:
            Tuple[Sequence[FreeFloating], Pagination]: A tuple containing sequences of FreeFloating objects and Pagination object.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        free_floatings = [
            FreeFloating.from_payload(data) for data in results.json()["free_floatings"]
        ]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return free_floatings, pagination

    def list_freefloatings_nearby(
        self,
        region_id: str,
        lon: float,
        lat: float,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """
        Retrieves free-floating vehicles near coordinates in a specific region from the Navitia API.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) based on user-provided coordinates.

        Parameters:
            region_id (str): The region ID (coverage identifier).
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            request (FreefloatingsNearbyRequest): The request object containing query parameters.

        Returns:
            Tuple[Sequence[FreeFloating], Pagination]: A tuple containing sequences of FreeFloating objects and Pagination object.

        Note:
            This feature requires a specific configuration from a freefloating data service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/coords/{lon};{lat}/freefloatings_nearby"
        return self._get_freefloatings_nearby(request_url, request.to_filters())

    def list_freefloatings_nearby_with_resource_path(
        self,
        region_id: str,
        resource_path: str,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """
        Retrieves free-floating vehicles near a specific resource path in a region from the Navitia API.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) near a specific resource (stop area, address, etc.).

        Parameters:
            region_id (str): The region ID (coverage identifier).
            resource_path (str): The resource path (e.g., 'stop_areas/stop_area:XXX').
            request (FreefloatingsNearbyRequest): The request object containing query parameters.

        Returns:
            Tuple[Sequence[FreeFloating], Pagination]: A tuple containing sequences of FreeFloating objects and Pagination object.

        Note:
            This feature requires a specific configuration from a freefloating data service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/freefloatings_nearby"
        return self._get_freefloatings_nearby(request_url, request.to_filters())

    def list_freefloatings_nearby_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """
        Retrieves free-floating vehicles near coordinates, navitia guesses the region from coordinates.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) based on user-provided coordinates. Navitia will automatically
        determine the region based on the provided region coordinates.

        Parameters:
            region_lon (float): The longitude coordinate for region identification.
            region_lat (float): The latitude coordinate for region identification.
            lon (float): The longitude coordinate for the search center.
            lat (float): The latitude coordinate for the search center.
            request (FreefloatingsNearbyRequest): The request object containing query parameters.

        Returns:
            Tuple[Sequence[FreeFloating], Pagination]: A tuple containing sequences of FreeFloating objects and Pagination object.

        Note:
            This feature requires a specific configuration from a freefloating data service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/freefloatings_nearby"
        return self._get_freefloatings_nearby(request_url, request.to_filters())

    def list_freefloatings_nearby_by_coordinates_only(
        self,
        lon: float,
        lat: float,
        request: FreefloatingsNearbyRequest = FreefloatingsNearbyRequest(),
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """
        Retrieves free-floating vehicles near coordinates without any region id.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) based on user-provided coordinates. This method does not require
        a region ID; Navitia will automatically determine the appropriate region.

        Parameters:
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            request (FreefloatingsNearbyRequest): The request object containing query parameters.

        Returns:
            Tuple[Sequence[FreeFloating], Pagination]: A tuple containing sequences of FreeFloating objects and Pagination object.

        Note:
            This feature requires a specific configuration from a freefloating data service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coord/{lon};{lat}/freefloatings_nearby"
        return self._get_freefloatings_nearby(request_url, request.to_filters())
