from datetime import datetime
from typing import Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.line_report import LineReport


class LineReportsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching line reports.

    See https://doc.navitia.io/#line-reports

    Methods
    -------
    _get_line_reports(url: str, filters: dict) -> Tuple[Sequence[Disruption], Sequence[LineReport]]:
        Retrieves line reports from the specified URL with the provided filters.

    list_line_reports(region_id: Optional[str] = None, resource_path: Optional[str] = None, since: Optional[datetime] = None, until: Optional[datetime] = None, count: int = 25, depth: int = 1, forbidden_uris: Optional[Sequence[str]] = None, disable_geojson: bool = False) -> Tuple[Sequence[Disruption], Sequence[LineReport]]:
        Lists line reports based on specified criteria.
    """

    def _get_line_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Disruption], Sequence[LineReport]]:
        """
        Retrieves line reports from the specified URL with the provided filters.

        Parameters
        ----------
        url : str
            The URL to fetch line reports from.
        filters : dict
            Filters to apply to the API request.

        Returns
        -------
        Tuple[Sequence[Disruption], Sequence[LineReport]]
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
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        count: int = 25,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        disable_geojson: bool = False,
    ) -> Tuple[Sequence[Disruption], Sequence[LineReport]]:
        """
        Lists line reports based on specified criteria.

        Parameters
        ----------
        region_id : Optional[str], optional
            The ID of the region for which to fetch line reports, by default None.
        resource_path : Optional[str], optional
            The resource path for line reports, by default None.
        since : Optional[datetime], optional
            Filter line reports since this date and time, by default None.
        until : Optional[datetime], optional
            Filter line reports until this date and time, by default None.
        count : int, optional
            The number of line reports to retrieve, by default 25.
        depth : int, optional
            The depth of the query, by default 1.
        forbidden_uris : Optional[Sequence[str]], optional
            List of URIs to forbid, by default None.
        disable_geojson : bool, optional
            Whether to disable GeoJSON output, by default False.

        Returns
        -------
        Tuple[Sequence[Disruption], Sequence[LineReport]]
            A tuple containing sequences of Disruption and LineReport objects.
        """
        if resource_path:
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/line_reports"
        else:
            request_url = f"{self.base_navitia_url}/coverage/{region_id}/line_reports"

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

        return self._get_line_reports(request_url, filters)
