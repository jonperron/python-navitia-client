from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.stop_area import StopArea


class StopAreaApiClient(ApiBaseClient, EntityApi[StopArea]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[StopArea]:
        stop_areas = []
        for stop_area_data in raw_entity_response:
            stop_area = StopArea.from_json(
                stop_area_data,
            )
            stop_areas.append(stop_area)

        return stop_areas

    def list_entity_collection_from_region(self, region_id: str) -> Sequence[StopArea]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/stop_areas"
        )
        raw_results = results.json()["stop_areas"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[StopArea]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/stop_areas/{object_id}"
        )
        raw_results = results.json()["stop_areas"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[StopArea]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/stop_areas/"
        )
        raw_results = results.json()["stop_areas"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[StopArea]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/stop_areas/{object_id}"
        )
        raw_results = results.json()["stop_areas"]
        return self._get_entity_from_response(raw_results)
