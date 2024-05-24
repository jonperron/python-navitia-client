from datetime import datetime
from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.isochrones import Isochrone


class IsochronesApiClient(ApiBaseClient):
    def _get_traffic_reports(self, url: str, filters: dict) -> Sequence[Isochrone]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        isochrones = [
            Isochrone.from_payload(data) for data in results.json()["isochrones"]
        ]
        return isochrones

    def list_isochrones_with_region_id(
        self,
        from_: str,
        region_id: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Sequence[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None,
    ) -> Sequence[Isochrone]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/isochrones"

        filters: dict[str, Any] = {
            "datetime": start_datetime.isoformat(),
            "boundary_duration[]": boundary_duration,
            "from": from_,
        }

        if to:
            filters["to"] = to

        if min_duration:
            filters["min_duration"] = min_duration

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if max_duration:
            filters["max_duration"] = max_duration
            if len(boundary_duration) == 0:
                # From API: you should provide a 'boundary_duration[]' or a 'max_duration'
                filters.pop("min_duration")

        return self._get_traffic_reports(request_url, filters)

    def list_isochrones(
        self,
        from_: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Sequence[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None,
    ) -> Sequence[Isochrone]:
        request_url = f"{self.base_navitia_url}/isochrones"

        filters: dict[str, Any] = {
            "datetime": start_datetime.isoformat(),
            "boundary_duration[]": boundary_duration,
            "from": from_,
        }
        if to:
            filters["to"] = to

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if min_duration:
            filters["min_duration"] = min_duration

        if max_duration:
            filters["max_duration"] = max_duration
            if len(boundary_duration) == 0:
                # From API: you should provide a 'boundary_duration[]' or a 'max_duration'
                filters.pop("min_duration")

        return self._get_traffic_reports(request_url, filters)
