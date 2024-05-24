from datetime import datetime
from typing import Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.traffic_report import TrafficReport


class TrafficReportsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching traffic reports.

    See https://doc.navitia.io/#traffic-reports

    Methods
    -------
    _get_traffic_reports(
        url: str, filters: dict
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        Retrieves traffic reports from the Navitia API based on provided URL and filters.

    list_traffic_reports(
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        count: int = 25,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        disable_geojson: bool = False,
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        Retrieves traffic reports for a specified region and resource path from the Navitia API.
    """

    def _get_traffic_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        """
        Retrieves traffic reports from the Navitia API based on provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to apply to the API request.

        Returns:
            Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]: A tuple containing sequences of Disruption and TrafficReport objects, and Pagination object.
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
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        count: int = 25,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        disable_geojson: bool = False,
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        """
        Retrieves traffic reports for a specified region and resource path from the Navitia API.

        Parameters:
            region_id (Optional[str]): The region ID.
            resource_path (Optional[str]): The resource path.
            since (Optional[datetime]): The start datetime for the reports.
            until (Optional[datetime]): The end datetime for the reports.
            count (int): The number of reports to retrieve. Defaults to 25.
            depth (int): The depth of data to retrieve. Defaults to 1.
            forbidden_uris (Optional[Sequence[str]]): Forbidden URIs.
            disable_geojson (bool): Whether to disable GeoJSON in the response. Defaults to False.

        Returns:
            Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]: A tuple containing sequences of Disruption and TrafficReport objects, and Pagination object.
        """
        if resource_path:
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/traffic_reports"
        else:
            request_url = (
                f"{self.base_navitia_url}/coverage/{region_id}/traffic_reports"
            )

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
