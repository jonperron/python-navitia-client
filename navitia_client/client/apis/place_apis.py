from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.place import Place


class PlacesApiClient(ApiBaseClient):
    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[Place]:
        entities = []
        for entity_data in response:
            entities.append(Place.from_payload(entity_data))

        return entities

    def list_places(
        self,
        region_id: str,
        query: str,
        type: Sequence[str] = ["stop_area", "address", "poi", "administrative_region"],
        disable_geojson: bool = False,
        depth: int = 1,
        from_lon_lat: Optional[tuple[float, float]] = None,
    ) -> Sequence[Place]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/pt_objects?q={query}&type={type}&disable_geojson={disable_geojson}&depth={depth}"
        if from_lon_lat:
            request_url += f"&filter={from_lon_lat[0]};{from_lon_lat[1]}"

        results = self.get_navitia_api(request_url)
        raw_results = results.json()["places"]
        return self._get_pt_objects_from_response(raw_results)
