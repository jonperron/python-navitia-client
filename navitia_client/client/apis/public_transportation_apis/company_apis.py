from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.company import Company


class CompanyApiClient(ApiBaseClient, EntityApi[Company]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[Company]:
        companies = []
        for company in raw_entity_response:
            companies.append(Company.from_json(company))
        return companies

    def list_entity_collection_from_region(self, region_id: str) -> Sequence[Company]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/companies"
        )
        raw_results = results.json()["companies"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[Company]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/companies/{object_id}"
        )
        raw_results = results.json()["companies"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Company]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/companies/"
        )
        raw_results = results.json()["companies"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[Company]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/companies/{object_id}"
        )
        raw_results = results.json()["companies"]
        return self._get_entity_from_response(raw_results)
