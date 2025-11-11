from typing import Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.traffic_report import TrafficReportRequest
from navitia_client.entities.response.disruption import Disruption
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.traffic_report import TrafficReport


class TrafficReportsApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching traffic reports.

    See https://doc.navitia.io/#traffic-reports
    """

    def _get_traffic_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        """Retrieve traffic reports from the Navitia API based on provided URL and filters.

        Args:
            url: The URL for the API request.
            filters: Filters to apply to the API request.

        Returns:
            A tuple containing sequences of Disruption and TrafficReport objects, and Pagination object.
        """
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
        request: TrafficReportRequest,
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        """Retrieve traffic reports for a specified region and resource path.

        Args:
            request: The request object containing query parameters.
            region_id: The region ID.
            resource_path: The resource path.

        Returns:
            A tuple containing sequences of Disruption and TrafficReport objects, and Pagination object.
        """
        if resource_path:
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/traffic_reports"
        else:
            request_url = (
                f"{self.base_navitia_url}/coverage/{region_id}/traffic_reports"
            )

        return self._get_traffic_reports(request_url, request.to_filters())
