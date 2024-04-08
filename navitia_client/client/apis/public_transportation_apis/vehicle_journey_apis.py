from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.vehicle_journey import VehicleJourney


class VehicleJourneyApiClient(ApiBaseClient, EntityApi[VehicleJourney]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[VehicleJourney]:
        vehicle_journeys = []
        for vehicle_journey in raw_entity_response:
            vehicle_journeys.append(VehicleJourney.from_json(vehicle_journey))
        return vehicle_journeys

    def list_entity_collection_from_region(
        self, region_id: str
    ) -> Sequence[VehicleJourney]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/vehicle_journeys"
        )
        raw_results = results.json()["vehicle_journeys"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(
        self, region_id: str, object_id: str
    ) -> Sequence[VehicleJourney]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/vehicle_journeys/{object_id}"
        )
        raw_results = results.json()["vehicle_journeys"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[VehicleJourney]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/vehicle_journeys/"
        )
        raw_results = results.json()["vehicle_journeys"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[VehicleJourney]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/vehicle_journeys/{object_id}"
        )
        raw_results = results.json()["vehicle_journeys"]
        return self._get_entity_from_response(raw_results)
