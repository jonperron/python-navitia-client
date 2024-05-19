from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.place import Place


class InvertedGeocodingApiClient(ApiBaseClient):
    @staticmethod
    def _get_regions_from_response(response: Any) -> Sequence[Place]:
        entities = []
        for entity_data in response:
            entities.append(Place.from_payload(entity_data))

        return entities

    def get_address_and_region_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Place]:
        result = self.get_navitia_api(f"{self.base_navitia_url}/places/{lon};{lat}")
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_and_region_from_id(self, id: str) -> Sequence[Place]:
        result = self.get_navitia_api(f"{self.base_navitia_url}/places/{id}")
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_coordinates_and_coordinates(
        self, region_lon: float, region_lat: float, lon: float, lat: float
    ) -> Sequence[Place]:
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/places/{lon};{lat}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_coordinates_and_id(
        self, region_lon: float, region_lat: float, id: str
    ) -> Sequence[Place]:
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/places/{id}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_id_and_coordinates(
        self, region_id: str, lon: float, lat: float
    ) -> Sequence[Place]:
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/places/{lon};{lat}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_id_and_id(
        self, region_id: str, id: str
    ) -> Sequence[Place]:
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/places/{id}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places
