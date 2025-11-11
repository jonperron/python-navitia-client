from typing import Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.freefloatings_nearby import (
    FreefloatingsNearbyRequest,
)
from navitia_client.entities.response.free_floating import FreeFloating
from navitia_client.entities.response import Pagination


class FreefloatingsNearbyApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching nearby free-floating vehicles.

    See https://doc.navitia.io/#freefloatings-nearby-api
    """

    def _get_freefloatings_nearby(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """Retrieve free-floating vehicles from the Navitia API based on provided URL and filters.

        Args:
            url: The URL for the API request.
            filters: Filters to apply to the API request.

        Returns:
            A tuple containing sequences of FreeFloating objects and Pagination object.
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
        request: FreefloatingsNearbyRequest,
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """Retrieve free-floating vehicles near coordinates in a specific region.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) based on user-provided coordinates.

        Args:
            region_id: The region ID (coverage identifier).
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            request: The request object containing query parameters.

        Returns:
            A tuple containing sequences of FreeFloating objects and Pagination object.

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
        request: FreefloatingsNearbyRequest,
    ) -> Tuple[Sequence[FreeFloating], Pagination]:
        """Retrieve free-floating vehicles near a specific resource path in a region.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) near a specific resource (stop area, address, etc.).

        Args:
            region_id: The region ID (coverage identifier).
            resource_path: The resource path (e.g., 'stop_areas/stop_area:XXX').
            request: The request object containing query parameters.

        Returns:
            A tuple containing sequences of FreeFloating objects and Pagination object.

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
        """Retrieve free-floating vehicles near coordinates, navitia guesses the region from coordinates.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) based on user-provided coordinates. Navitia will automatically
        determine the region based on the provided region coordinates.

        Args:
            region_lon: The longitude coordinate for region identification.
            region_lat: The latitude coordinate for region identification.
            lon: The longitude coordinate for the search center.
            lat: The latitude coordinate for the search center.
            request: The request object containing query parameters.

        Returns:
            A tuple containing sequences of FreeFloating objects and Pagination object.

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
        """Retrieve free-floating vehicles near coordinates without any region id.

        This service provides access to nearby shared mobility options (such as bikes,
        scooters, or cars) based on user-provided coordinates. This method does not require
        a region ID; Navitia will automatically determine the appropriate region.

        Args:
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            request: The request object containing query parameters.

        Returns:
            A tuple containing sequences of FreeFloating objects and Pagination object.

        Note:
            This feature requires a specific configuration from a freefloating data service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coord/{lon};{lat}/freefloatings_nearby"
        return self._get_freefloatings_nearby(request_url, request.to_filters())
