from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.request.base_entity_request import BasePTEntityRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.physical_mode import CommercialMode


class CommercialModeApiClient(ApiBaseClient, EntityApi[CommercialMode]):
    """API client for handling 'CommercialMode' entities in the Navitia API.

    See https://doc.navitia.io/#pt-ref

    Attributes:
        entity_name: The name of the entity.
        get_navitia_api: A method to get the Navitia API.
    """

    entity_name: str = "commercial_modes"
    get_navitia_api = ApiBaseClient.get_navitia_api

    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[CommercialMode]:
        """Extract CommercialMode entities from the API response.

        Args:
            raw_entity_response: The raw response from the API.

        Returns:
            A sequence of CommercialMode objects.
        """
        entities = []
        for entity in raw_entity_response:
            entities.append(CommercialMode.from_payload(entity))
        return entities

    def list_entity_collection_from_region(
        self,
        region_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """List commercial modes from a specified region.

        Args:
            region_id: The ID of the region.
            request: Request parameters for filtering.

        Returns:
            A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id(
        self,
        region_id: str,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """Retrieve a specific commercial mode by its ID from a specified region.

        Args:
            region_id: The ID of the region.
            object_id: The ID of the commercial mode.
            request: Request parameters for filtering.

        Returns:
            A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def list_entity_collection_from_coordinates(
        self,
        lon: float,
        lat: float,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """List commercial modes from specified coordinates.

        Args:
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            request: Request parameters for filtering.

        Returns:
            A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """Retrieve a specific commercial mode by its ID from specified coordinates.

        Args:
            lon: The longitude coordinate.
            lat: The latitude coordinate.
            object_id: The ID of the commercial mode.
            request: Request parameters for filtering.

        Returns:
            A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())
