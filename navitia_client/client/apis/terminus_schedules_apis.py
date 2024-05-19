from datetime import datetime
from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.stop_schedule import TerminusSchedule


class TerminusSchedulesApiClient(ApiBaseClient):
    @staticmethod
    def _get_terminus_schedule_object_from_response(
        response: Any,
    ) -> Sequence[TerminusSchedule]:
        terminus_schedules = []
        for terminus_schedule_data in response:
            terminus_schedules.append(
                TerminusSchedule.from_json(terminus_schedule_data)
            )

        return terminus_schedules

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string regarding provided filters"""
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_stop_schedules(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["terminus_schedules"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return self._get_terminus_schedule_object_from_response(raw_results), pagination

    def list_terminus_schedules(
        self,
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        region_lon: Optional[float] = None,
        region_lat: Optional[float] = None,
        lon: Optional[float] = None,
        lat: Optional[float] = None,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        request_url: str | None = None
        if region_id and resource_path:
            # See https://doc.navitia.io/#route-schedules for URL description
            # List of route schedules near the resource
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/terminus_schedules"
        elif all([region_lon, region_lat, lon, lat]):
            # List of objects near the resource, navitia guesses the region from coordinates
            request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/terminus_schedules"

        if not request_url:
            raise ValueError(
                "Region id and resource path or region coordinates and coordinates must be provided."
            )

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

        return self._get_stop_schedules(request_url, filters)
