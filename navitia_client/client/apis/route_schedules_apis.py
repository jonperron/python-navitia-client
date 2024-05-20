from datetime import datetime
from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.route_schedule import RouteSchedule


class RouteSchedulesApiClient(ApiBaseClient):
    @staticmethod
    def _get_route_schedule_object_from_response(
        response: Any,
    ) -> Sequence[RouteSchedule]:
        route_schedules = []
        for route_schedule_data in response:
            route_schedules.append(RouteSchedule.from_payload(route_schedule_data))

        return route_schedules

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string regarding provided filters"""
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_routes_nearby(self, url: str, filters: dict) -> Sequence[RouteSchedule]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["route_schedules"]
        return self._get_route_schedule_object_from_response(raw_results)

    def list_route_schedules_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "base_schedule",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Sequence[RouteSchedule]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/route_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "items_per_schedule": items_per_schedule,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_routes_nearby(request_url, filters)

    def list_route_schedules_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "base_schedule",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Sequence[RouteSchedule]:
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/route_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "items_per_schedule": items_per_schedule,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_routes_nearby(request_url, filters)
