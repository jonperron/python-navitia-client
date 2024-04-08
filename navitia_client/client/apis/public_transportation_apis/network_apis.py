from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.network import Network


class NetworkApiClient(ApiBaseClient, EntityApi[Network]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[Network]:
        networks = []
        for network in raw_entity_response:
            networks.append(Network.from_json(network))
        return networks

    def list_entity_collection_from_region(self, region_id: str) -> Sequence[Network]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/networks"
        )
        raw_results = results.json()["networks"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[Network]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/networks/{object_id}"
        )
        raw_results = results.json()["networks"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Network]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/networks/"
        )
        raw_results = results.json()["networks"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[Network]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/networks/{object_id}"
        )
        raw_results = results.json()["networks"]
        return self._get_entity_from_response(raw_results)
