from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.vehicle_journey import VehicleJourney


class VehicleJourneyApiClient(ApiBaseClient, EntityApi[VehicleJourney]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[VehicleJourney]:
        vehicle_journeys = []
        for vehicle_journey in raw_entity_response:
            vehicle_journeys.append(VehicleJourney.from_json(vehicle_journey))
        return vehicle_journeys

    def list_entity_collection_from_region(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/vehicle_journeys?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["vehicle_journeys"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    def get_entity_by_id(
        self, region_id: str, object_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/vehicle_journeys/{object_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["vehicle_journeys"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/vehicle_journeys?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["vehicle_journeys"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/vehicle_journeys/{object_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["vehicle_journeys"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination
