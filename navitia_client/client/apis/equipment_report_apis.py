from typing import Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.equipment_report import EquipmentReportRequest
from navitia_client.entities.response.equipment_reports import EquipmentReports
from navitia_client.entities.response import Pagination


class EquipmentReportsApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching equipment reports.

    See https://doc.navitia.io/#equipment-reports
    """

    def _get_equipment_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        """Retrieve equipment reports from the Navitia API based on provided URL and filters.

        Args:
            url: The URL for the API request.
            filters: Filters to apply to the API request.

        Returns:
            A tuple containing sequences of EquipmentReports objects and Pagination object.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        equipment_reports = [
            EquipmentReports.from_payload(data)
            for data in results.json()["equipment_reports"]
        ]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return equipment_reports, pagination

    def list_equipment_reports(
        self,
        region_id: str,
        request: EquipmentReportRequest,
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        """Retrieve equipment reports for a specified region from the Navitia API.

        This service provides the state of equipments such as lifts or elevators that
        are giving better accessibility to public transport facilities.
        The endpoint will report accessible equipment per stop area and per line.

        Args:
            region_id: The region ID (coverage identifier).
            request: The request object containing query parameters.

        Returns:
            A tuple containing sequences of EquipmentReports objects and Pagination object.

        Note:
            This feature requires a specific configuration from an equipment service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/equipment_reports"
        return self._get_equipment_reports(request_url, request.to_filters())

    def list_equipment_reports_with_resource_path(
        self,
        region_id: str,
        resource_path: str,
        request: EquipmentReportRequest,
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        """Retrieve equipment reports for a specific resource path in a region.

        This service provides the state of equipments such as lifts or elevators that
        are giving better accessibility to public transport facilities.
        The endpoint will report accessible equipment per stop area and per line.

        Args:
            region_id: The region ID (coverage identifier).
            resource_path: The resource path (e.g., 'lines/line:A').
            request: The request object containing query parameters.

        Returns:
            A tuple containing sequences of EquipmentReports objects and Pagination object.

        Note:
            This feature requires a specific configuration from an equipment service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/equipment_reports"
        return self._get_equipment_reports(request_url, request.to_filters())
