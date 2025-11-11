from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.places_nearby import PlacesNearbyRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.place import Place


class PlacesNearbyApiClient(ApiBaseClient):
    """A client class to interact with the Navitia API for fetching nearby places information.

    See https://doc.navitia.io/#places_nearby
    """

    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[Place]:
        """Transform raw API response data into a list of Place objects.

        Args:
            response: The raw API response data.

        Returns:
            A list of Place objects.
        """
        entities = []
        for entity_data in response:
            entities.append(Place.from_payload(entity_data))

        return entities

    def _get_places_nearby(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Place], Pagination]:
        """Fetch nearby places based on the provided URL and filters.

        Args:
            url: The URL for the API request.
            filters: Filters to be applied to the API request.

        Returns:
            A tuple containing a list of nearby Place objects and pagination information.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["places_nearby"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_pt_objects_from_response(raw_results), pagination

    def list_objects_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        request: PlacesNearbyRequest,
    ) -> Tuple[Sequence[Place], Pagination]:
        """Retrieve a list of places nearby based on region ID and resource path.

        Args:
            region_id: The region ID.
            resource_path: The resource path.
            request: The PlacesNearbyRequest containing filters and parameters for the query.

        Returns:
            A tuple containing a list of nearby Place objects and pagination information.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/places_nearby"

        return self._get_places_nearby(request_url, request.to_filters())

    def list_objects_by_region_id_and_coordinates(
        self,
        region_id: str,
        lon: float,
        lat: float,
        request: PlacesNearbyRequest,
    ) -> Tuple[Sequence[Place], Pagination]:
        """Retrieve a list of places nearby based on region ID and coordinates.

        Args:
            region_id: The region ID.
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            request: The PlacesNearbyRequest containing filters and parameters for the query.

        Returns:
            A tuple containing a list of nearby Place objects and pagination information.
        """
        request_url = (
            f"{self.base_navitia_url}/coverage/{region_id}/{lon};{lat}/places_nearby"
        )

        return self._get_places_nearby(request_url, request.to_filters())

    def list_objects_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: PlacesNearbyRequest,
    ) -> Tuple[Sequence[Place], Pagination]:
        """Retrieve a list of places nearby based on the provided coordinates.

        Args:
            region_lon: The longitude coordinate of the region.
            region_lat: The latitude coordinate of the region.
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            request: The PlacesNearbyRequest containing filters and parameters for the query.

        Returns:
            A tuple containing a list of nearby Place objects and pagination information.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/places_nearby"

        return self._get_places_nearby(request_url, request.to_filters())

    def list_objects_by_object_coordinates_only(
        self,
        lon: float,
        lat: float,
        request: PlacesNearbyRequest,
    ) -> Tuple[Sequence[Place], Pagination]:
        """Retrieve a list of places nearby based on the provided coordinates.

        Args:
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            request: The PlacesNearbyRequest containing filters and parameters for the query.

        Returns:
            A tuple containing a list of nearby Place objects and pagination information.
        """
        request_url = f"{self.base_navitia_url}/coverage/{lon};{lat}/places_nearby"

        return self._get_places_nearby(request_url, request.to_filters())
