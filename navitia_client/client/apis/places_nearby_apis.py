from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.place import Place


class PlacesNearbyApiClient(ApiBaseClient):
    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[Place]:
        entities = []
        for entity_data in response:
            entities.append(Place.from_json(entity_data))

        return entities

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string regarding provided filters"""
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_places_nearby(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Place], Pagination]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["places_nearby"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_pt_objects_from_response(raw_results), pagination

    def list_objects(
        self,
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        region_lon: Optional[float] = None,
        region_lat: Optional[float] = None,
        lon: Optional[float] = None,
        lat: Optional[float] = None,
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
        request_url: str | None = None
        if region_id:
            # See https://doc.navitia.io/#places-nearby-api for URL description
            if resource_path:
                # List of objects near the resource
                request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/places_nearby"
            elif lon and lat:
                # List of objects near a coordinate
                request_url = f"{self.base_navitia_url}/coverage/{region_id}/{lon};{lat}/places_nearby"
        elif region_lon and region_lat and lon and lat:
            # List of objects near the resource, navitia guesses the region from coordinates
            request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/places_nearby"
        elif lon and lat and not any([region_id, region_lat, region_lon]):
            # List of objects near the resource without any region id (same result as above)
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
