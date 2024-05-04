from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.line_and_route import Route


class RouteApiClient(ApiBaseClient, EntityApi[Route]):
    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[Route]:
        routes: list[Route] = []
        for route_data in raw_entity_response:
            route = Route.from_json(
                payload=route_data,
            )
            routes.append(route)

        return routes

    def list_entity_collection_from_region(self, region_id: str) -> Sequence[Route]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/routes"
        )
        raw_results = results.json()["routes"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id(self, region_id: str, object_id: str) -> Sequence[Route]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/routes/{object_id}"
        )
        raw_results = results.json()["routes"]
        return self._get_entity_from_response(raw_results)

    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Route]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/routes/"
        )
        raw_results = results.json()["routes"]
        return self._get_entity_from_response(raw_results)

    def get_entity_by_id_and_coordinates(
        self, lon: float, lat: float, object_id: str
    ) -> Sequence[Route]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}/routes/{object_id}"
        )
        raw_results = results.json()["routes"]
        return self._get_entity_from_response(raw_results)
