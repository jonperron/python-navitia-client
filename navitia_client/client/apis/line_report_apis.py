from typing import Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.line_report import LineReportRequest
from navitia_client.entities.response.disruption import Disruption
from navitia_client.entities.response.line_report import LineReport


class LineReportsApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching line reports.

    See https://doc.navitia.io/#line-reports
    """

    def _get_line_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Disruption], Sequence[LineReport]]:
        """Retrieve line reports from the specified URL with the provided filters.

        Args:
            url: The URL to fetch line reports from.
            filters: Filters to apply to the API request.

        Returns:
            A tuple containing sequences of Disruption and LineReport objects.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        line_reports = [
            LineReport.from_payload(data) for data in results.json()["line_reports"]
        ]
        disruptions = [
            Disruption.from_payload(data) for data in results.json()["disruptions"]
        ]
        return disruptions, line_reports

    def list_line_reports(
        self,
        request: LineReportRequest,
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
    ) -> Tuple[Sequence[Disruption], Sequence[LineReport]]:
        """List line reports based on specified criteria.

        Args:
            request: The request object containing query parameters.
            region_id: The ID of the region for which to fetch line reports, by default None.
            resource_path: The resource path for line reports, by default None.

        Returns:
            A tuple containing sequences of Disruption and LineReport objects.
        """
        if resource_path:
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/line_reports"
        else:
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/line_reports"

        return self._get_line_reports(request_url, request.to_filters())
