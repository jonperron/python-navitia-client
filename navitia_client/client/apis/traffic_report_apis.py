from datetime import datetime
from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.traffic_report import TrafficReport


class TrafficReportsApiClient(ApiBaseClient):
    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string regarding provided filters"""
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_traffic_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        line_reports = [
            TrafficReport.from_payload(data)
            for data in results.json()["traffic_reports"]
        ]
        disruptions = [
            Disruption.from_payload(data) for data in results.json()["disruptions"]
        ]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return disruptions, line_reports, pagination

    def list_traffic_reports(
        self,
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        count: int = 25,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        disable_geojson: bool = False,
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/traffic_reports"

        filters = {
            "count": count,
            "depth": depth,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
        }

        if since:
            filters["since"] = since.isoformat()

        if until:
            filters["until"] = until.isoformat()

        return self._get_traffic_reports(request_url, filters)
