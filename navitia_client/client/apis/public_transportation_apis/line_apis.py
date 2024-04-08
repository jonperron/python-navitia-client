from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.line_and_route import Line


class LineApiClient(ApiBaseClient, EntityApi[Line]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[Line]:
        lines = []
        for line_data in raw_entity_response:
            line = Line.from_json(
                payload=line_data,
            )

            lines.append(line)

        return lines

    def list_entity_collection_from_region(self, region_id: str) -> Sequence[Line]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/lines"
        )
        raw_results = results.json()["lines"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[Line]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/lines/{object_id}"
        )
        raw_results = results.json()["lines"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Line]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/lines/"
        )
        raw_results = results.json()["lines"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[Line]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/lines/{object_id}"
        )
        raw_results = results.json()["lines"]
        return self._get_entity_from_response(raw_results)
