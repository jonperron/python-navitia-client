from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.stop_schedule import StopScheduleRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.stop_schedule import StopSchedule


class StopSchedulesApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching stop schedules.

    See https://doc.navitia.io/#stop-schedules
    """

    @staticmethod
    def _get_stop_schedule_objects_from_response(
        response: Any,
    ) -> Sequence[StopSchedule]:
        """Transform raw API response data into a list of StopSchedule objects.

        Args:
            response: The raw API response data.

        Returns:
            A sequence of StopSchedule objects.
        """
        stop_schedules = []
        for stop_schedule_data in response:
            stop_schedules.append(StopSchedule.from_payload(stop_schedule_data))

        return stop_schedules

    def _get_stop_schedules(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        """Retrieve stop schedules from the Navitia API based on provided URL and filters.

        Args:
            url: The URL for the API request.
            filters: Filters to apply to the API request.

        Returns:
            A tuple containing a sequence of StopSchedule objects and Pagination object.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["stop_schedules"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_stop_schedule_objects_from_response(raw_results), pagination

    def list_stop_schedules_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: StopScheduleRequest,
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        """Retrieve stop schedules for a specified set of coordinates.

        Args:
            region_lon: The longitude of the region.
            region_lat: The latitude of the region.
            lon: The longitude of the coordinates.
            lat: The latitude of the coordinates.
            request: The request object containing query parameters.

        Returns:
            A tuple containing a sequence of StopSchedule objects and Pagination object.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/stop_schedules"

        return self._get_stop_schedules(request_url, request.to_filters())

    def list_stop_schedules_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        request: StopScheduleRequest,
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        """Retrieve stop schedules for a specified region and resource path.

        Args:
            region_id: The region ID.
            resource_path: The resource path.
            request: The request object containing query parameters.

        Returns:
            A tuple containing a sequence of StopSchedule objects and Pagination object.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/stop_schedules"

        return self._get_stop_schedules(request_url, request.to_filters())
