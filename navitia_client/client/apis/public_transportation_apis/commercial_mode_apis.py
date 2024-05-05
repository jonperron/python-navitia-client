from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.physical_mode import CommercialMode


class CommercialModeApiClient(ApiBaseClient, EntityApi[CommercialMode]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[CommercialMode]:
        commercial_modes = []
        for commercial_mode in raw_entity_response:
            commercial_modes.append(CommercialMode.from_json(commercial_mode))
        return commercial_modes

    def list_entity_collection_from_region(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/commercial_modes?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["commercial_modes"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    def get_entity_by_id(
        self, region_id: str, object_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/commercial_modes/{object_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["commercial_modes"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/commercial_modes?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["commercial_modes"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/commercial_modes/{object_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["commercial_modes"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination
