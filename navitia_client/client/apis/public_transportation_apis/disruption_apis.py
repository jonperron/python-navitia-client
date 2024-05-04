from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.disruption import (
    Disruption,
)


class DisruptionApiClient(ApiBaseClient, EntityApi[Disruption]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[Disruption]:
        disruptions = []
        for disruption_data in raw_entity_response:
            disruption = Disruption.from_json(
                payload=disruption_data,
            )
            disruptions.append(disruption)
        return disruptions

    def list_entity_collection_from_region(
        self, region_id: str
    ) -> Sequence[Disruption]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/disruptions"
        )
        raw_results = results.json()["disruptions"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[Disruption]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/disruptions/{object_id}"
        )
        raw_results = results.json()["disruptions"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Disruption]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/disruptions/"
        )
        raw_results = results.json()["disruptions"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[Disruption]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/disruptions/{object_id}"
        )
        raw_results = results.json()["disruptions"]
        return self._get_entity_from_response(raw_results)
