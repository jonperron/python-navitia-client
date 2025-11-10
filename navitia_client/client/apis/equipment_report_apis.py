from typing import Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.equipment_reports import EquipmentReports
from navitia_client.entities.pagination import Pagination


class EquipmentReportsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching equipment reports.

    See https://doc.navitia.io/#equipment-reports

    Methods
    -------
    _get_equipment_reports(
        url: str, filters: dict
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        Retrieves equipment reports from the Navitia API based on provided URL and filters.

    list_equipment_reports(
        region_id: str,
        count: int = 10,
        depth: int = 1,
        filter: Optional[str] = None,
        forbidden_uris: Optional[Sequence[str]] = None,
        start_page: int = 0,
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        Retrieves equipment reports for a specified region from the Navitia API.

    list_equipment_reports_with_resource_path(
        region_id: str,
        resource_path: str,
        count: int = 10,
        depth: int = 1,
        filter: Optional[str] = None,
        forbidden_uris: Optional[Sequence[str]] = None,
        start_page: int = 0,
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        Retrieves equipment reports for a specific resource path in a region from the Navitia API.
    """

    def _get_equipment_reports(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        """
        Retrieves equipment reports from the Navitia API based on provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to apply to the API request.

        Returns:
            Tuple[Sequence[EquipmentReports], Pagination]: A tuple containing sequences of EquipmentReports objects and Pagination object.
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
        count: int = 10,
        depth: int = 1,
        filter: Optional[str] = None,
        forbidden_uris: Optional[Sequence[str]] = None,
        start_page: int = 0,
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        """
        Retrieves equipment reports for a specified region from the Navitia API.

        This service provides the state of equipments such as lifts or elevators that
        are giving better accessibility to public transport facilities.
        The endpoint will report accessible equipment per stop area and per line.

        Parameters:
            region_id (str): The region ID (coverage identifier).
            count (int): Elements per page. Defaults to 10.
            depth (int): Json response depth. Defaults to 1.
            filter (Optional[str]): A filter to refine your request (e.g., 'line.code=A').
            forbidden_uris (Optional[Sequence[str]]): If you want to avoid lines, modes, networks, etc.
            start_page (int): The page number. Defaults to 0.

        Returns:
            Tuple[Sequence[EquipmentReports], Pagination]: A tuple containing sequences of EquipmentReports objects and Pagination object.

        Note:
            This feature requires a specific configuration from an equipment service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/equipment_reports"

        filters = {
            "count": count,
            "depth": depth,
            "start_page": start_page,
            "forbidden_uris[]": forbidden_uris,
        }

        if filter:
            filters["filter"] = filter

        return self._get_equipment_reports(request_url, filters)

    def list_equipment_reports_with_resource_path(
        self,
        region_id: str,
        resource_path: str,
        count: int = 10,
        depth: int = 1,
        filter: Optional[str] = None,
        forbidden_uris: Optional[Sequence[str]] = None,
        start_page: int = 0,
    ) -> Tuple[Sequence[EquipmentReports], Pagination]:
        """
        Retrieves equipment reports for a specific resource path in a region from the Navitia API.

        This service provides the state of equipments such as lifts or elevators that
        are giving better accessibility to public transport facilities.
        The endpoint will report accessible equipment per stop area and per line.

        Parameters:
            region_id (str): The region ID (coverage identifier).
            resource_path (str): The resource path (e.g., 'lines/line:A').
            count (int): Elements per page. Defaults to 10.
            depth (int): Json response depth. Defaults to 1.
            filter (Optional[str]): A filter to refine your request (e.g., 'line.code=A').
            forbidden_uris (Optional[Sequence[str]]): If you want to avoid lines, modes, networks, etc.
            start_page (int): The page number. Defaults to 0.

        Returns:
            Tuple[Sequence[EquipmentReports], Pagination]: A tuple containing sequences of EquipmentReports objects and Pagination object.

        Note:
            This feature requires a specific configuration from an equipment service provider.
            Therefore, this service is not available by default.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/equipment_reports"

        filters = {
            "count": count,
            "depth": depth,
            "start_page": start_page,
            "forbidden_uris[]": forbidden_uris,
        }

        if filter:
            filters["filter"] = filter

        return self._get_equipment_reports(request_url, filters)
