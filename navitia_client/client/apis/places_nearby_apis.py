from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.place import Place


class PlacesNearbyApiClient(ApiBaseClient):
    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[Place]:
        entities = []
        for entity_data in response:
            entities.append(Place.from_payload(entity_data))

        return entities

    def _get_places_nearby(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Place], Pagination]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["places_nearby"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_pt_objects_from_response(raw_results), pagination

    def list_objects_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/places_nearby"

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)

    def list_objects_by_region_id_and_coordinates(
        self,
        region_id: str,
        lon: float,
        lat: float,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        request_url = (
            f"{self.base_navitia_url}/coverage/{region_id}/{lon};{lat}/places_nearby"
        )

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)

    def list_objects_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/places_nearby"

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)

    def list_objects_by_object_coordinates_only(
        self,
        lon: float,
        lat: float,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        request_url = f"{self.base_navitia_url}/coverage/{lon};{lat}/places_nearby"

        if not request_url:
            raise ValueError(
                "Region id, region coordinates or coordinates must be provided."
            )

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)
