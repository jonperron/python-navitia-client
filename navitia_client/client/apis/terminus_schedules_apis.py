from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.terminus_schedule import TerminusScheduleRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.stop_schedule import TerminusSchedule


class TerminusSchedulesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching terminus schedules.
    Uses the TerminusScheduleRequest class to encapsulate query parameters.

    See https://doc.navitia.io/#terminus-schedules
    """

    @staticmethod
    def _get_terminus_schedule_objects_from_response(
        response: Any,
    ) -> Sequence[TerminusSchedule]:
        """
        Static method to transform raw API response data into a list of TerminusSchedule objects.

        Parameters:
            response (Any): The raw API response data.

        Returns:
            Sequence[TerminusSchedule]: A sequence of TerminusSchedule objects.
        """
        terminus_schedules = []
        for terminus_schedule_data in response:
            terminus_schedules.append(
                TerminusSchedule.from_payload(terminus_schedule_data)
            )

        return terminus_schedules

    def _get_stop_schedules(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        """
        Retrieves terminus schedules from the Navitia API based on provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to apply to the API request.

        Returns:
            Tuple[Sequence[TerminusSchedule], Pagination]: A tuple containing a sequence of TerminusSchedule objects and Pagination object.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["terminus_schedules"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_terminus_schedule_objects_from_response(
            raw_results
        ), pagination

    def list_terminus_schedules_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        request: TerminusScheduleRequest,
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        """
        Retrieves terminus schedules for a specified region and resource path from the Navitia API.

        Parameters
        ----------
        region_id : str
            The region ID.
        resource_path : str
            The resource path.
        request : TerminusScheduleRequest
            The request object containing query parameters such as from_datetime,
            duration, depth, count, start_page, items_per_schedule, forbidden_uris,
            data_freshness, disable_geojson, and direction_type.

        Returns
        -------
        Tuple[Sequence[TerminusSchedule], Pagination]
            A tuple containing a sequence of TerminusSchedule objects and Pagination object.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/terminus_schedules"

        return self._get_stop_schedules(request_url, request.to_filters())

    def list_terminus_schedules_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: TerminusScheduleRequest,
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        """
        Retrieves terminus schedules for a specified set of coordinates from the Navitia API.

        Parameters
        ----------
        region_lon : float
            The longitude of the region.
        region_lat : float
            The latitude of the region.
        lon : float
            The longitude of the coordinates.
        lat : float
            The latitude of the coordinates.
        request : TerminusScheduleRequest
            The request object containing query parameters such as from_datetime,
            duration, depth, count, start_page, items_per_schedule, forbidden_uris,
            data_freshness, disable_geojson, and direction_type.

        Returns
        -------
        Tuple[Sequence[TerminusSchedule], Pagination]
            A tuple containing a sequence of TerminusSchedule objects and Pagination object.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/terminus_schedules"

        return self._get_stop_schedules(request_url, request.to_filters())
