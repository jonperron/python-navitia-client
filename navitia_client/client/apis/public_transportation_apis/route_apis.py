from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.request.base_entity_request import BasePTEntityRequest
from navitia_client.entities.response.line_and_route import Route
from navitia_client.entities.response import Pagination


class RouteApiClient(ApiBaseClient, EntityApi[Route]):
    """API client for handling 'Route' entities in the Navitia API.

    See https://doc.navitia.io/#pt-ref

    Attributes:
        entity_name: Name of the entity ('routes').
        get_navitia_api: Method to get the Navitia API.
    """

    entity_name: str = "routes"
    get_navitia_api = ApiBaseClient.get_navitia_api

    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[Route]:
        """Extract Route entities from the raw API response.

        Args:
            raw_entity_response: Raw API response containing route data.

        Returns:
            List of Route instances.
        """
        entities = []
        for entity in raw_entity_response:
            entities.append(Route.from_payload(entity))
        return entities

    def list_entity_collection_from_region(
        self,
        region_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[Route], Pagination]:
        """List routes for a given region.

        Args:
            region_id: ID of the region.
            request: Request parameters for filtering.

        Returns:
            List of Route instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id(
        self,
        region_id: str,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[Route], Pagination]:
        """Get a route by its ID in a given region.

        Args:
            region_id: ID of the region.
            object_id: ID of the route.
            request: Request parameters for filtering.

        Returns:
            List of Route instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def list_entity_collection_from_coordinates(
        self,
        lon: float,
        lat: float,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[Route], Pagination]:
        """List routes for given geographic coordinates.

        Args:
            lon: Longitude.
            lat: Latitude.
            request: Request parameters for filtering.

        Returns:
            List of Route instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[Route], Pagination]:
        """Get a route by its ID for given geographic coordinates.

        Args:
            lon: Longitude.
            lat: Latitude.
            object_id: ID of the route.
            request: Request parameters for filtering.

        Returns:
            List of Route instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())
