from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.stop_area import StopPoint


class StopPointApiClient(ApiBaseClient, EntityApi[StopPoint]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[StopPoint]:
        stop_points = []
        for stop_point_data in raw_entity_response:
            stop_point = StopPoint.from_json(
                stop_point_data,
            )

            stop_points.append(stop_point)

        return stop_points

    def list_entity_collection_from_region(self, region_id: str) -> Sequence[StopPoint]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/stop_points"
        )
        raw_results = results.json()["stop_points"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[StopPoint]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/stop_points/{object_id}"
        )
        raw_results = results.json()["stop_points"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[StopPoint]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/stop_points/"
        )
        raw_results = results.json()["stop_points"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[StopPoint]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/stop_points/{object_id}"
        )
        raw_results = results.json()["stop_points"]
        return self._get_entity_from_response(raw_results)
