from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.physical_mode import PhysicalMode


class PhysicalModeApiClient(ApiBaseClient, EntityApi[PhysicalMode]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[PhysicalMode]:
        physical_modes = []
        for physical_mode in raw_entity_response:
            physical_modes.append(
                PhysicalMode.from_json(
                    physical_mode,
                )
            )
        return physical_modes

    def list_entity_collection_from_region(
        self, region_id: str
    ) -> Sequence[PhysicalMode]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/physical_modes"
        )
        raw_results = results.json()["physical_modes"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(
        self, region_id: str, object_id: str
    ) -> Sequence[PhysicalMode]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/physical_modes/{object_id}"
        )
        raw_results = results.json()["physical_modes"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[PhysicalMode]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/physical_modes/"
        )
        raw_results = results.json()["physical_modes"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[PhysicalMode]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/physical_modes/{object_id}"
        )
        raw_results = results.json()["physical_modes"]
        return self._get_entity_from_response(raw_results)
