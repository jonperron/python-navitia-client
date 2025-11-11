from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.request.base_entity_request import BasePTEntityRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.physical_mode import PhysicalMode


class PhysicalModeApiClient(ApiBaseClient, EntityApi[PhysicalMode]):
    """API client for handling 'PhysicalMode' entities in the Navitia API.

    See https://doc.navitia.io/#pt-ref

    Attributes:
        entity_name: Name of the entity ('physical_modes').
        get_navitia_api: Method to get the Navitia API.
    """

    entity_name: str = "physical_modes"
    get_navitia_api = ApiBaseClient.get_navitia_api

    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[PhysicalMode]:
        """Extract PhysicalMode entities from the raw API response.

        Args:
            raw_entity_response: Raw API response containing physical mode data.

        Returns:
            List of PhysicalMode instances.
        """
        entities = []
        for entity in raw_entity_response:
            entities.append(PhysicalMode.from_payload(entity))
        return entities

    def list_entity_collection_from_region(
        self,
        region_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """List physical modes for a given region.

        Args:
            region_id: ID of the region.
            request: Request parameters for filtering.

        Returns:
            List of PhysicalMode instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id(
        self,
        region_id: str,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """Get a physical mode by its ID in a given region.

        Args:
            region_id: ID of the region.
            object_id: ID of the physical mode.
            request: Request parameters for filtering.

        Returns:
            List of PhysicalMode instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def list_entity_collection_from_coordinates(
        self,
        lon: float,
        lat: float,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """List physical modes for given geographic coordinates.

        Args:
            lon: Longitude.
            lat: Latitude.
            request: Request parameters for filtering.

        Returns:
            List of PhysicalMode instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """Get a physical mode by its ID for given geographic coordinates.

        Args:
            lon: Longitude.
            lat: Latitude.
            object_id: ID of the physical mode.
            request: Request parameters for filtering.

        Returns:
            List of PhysicalMode instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())
