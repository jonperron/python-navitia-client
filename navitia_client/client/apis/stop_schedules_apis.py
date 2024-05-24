from datetime import datetime
from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.stop_schedule import StopSchedule


class StopSchedulesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching stop schedules.

    See https://doc.navitia.io/#stop-schedules

    Methods
    -------
    _get_stop_schedule_objects_from_response(response: Any) -> Sequence[StopSchedule]:
        A static method to transform raw API response data into a list of StopSchedule objects.

    list_stop_schedules_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        Retrieves stop schedules for a specified set of coordinates from the Navitia API.

    list_stop_schedules_by_region_id_and_path(
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        Retrieves stop schedules for a specified region and resource path from the Navitia API.
    """

    @staticmethod
    def _get_stop_schedule_objects_from_response(
        response: Any,
    ) -> Sequence[StopSchedule]:
        """
        Static method to transform raw API response data into a list of StopSchedule objects.

        Parameters:
            response (Any): The raw API response data.

        Returns:
            Sequence[StopSchedule]: A sequence of StopSchedule objects.
        """
        stop_schedules = []
        for stop_schedule_data in response:
            stop_schedules.append(StopSchedule.from_payload(stop_schedule_data))

        return stop_schedules

    def _get_stop_schedules(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        """
        Retrieves stop schedules from the Navitia API based on provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to apply to the API request.

        Returns:
            Tuple[Sequence[StopSchedule], Pagination]: A tuple containing a sequence of StopSchedule objects and Pagination object.
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
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        """
        Retrieves stop schedules for a specified set of coordinates from the Navitia API.

        Parameters:
            region_lon (float): The longitude of the region.
            region_lat (float): The latitude of the region.
            lon (float): The longitude of the coordinates.
            lat (float): The latitude of the coordinates.
            from_datetime (datetime, optional): The start datetime for the schedule. Defaults to datetime.now().
            duration (int, optional): The duration of the schedule in seconds. Defaults to 86400.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            items_per_schedule (int, optional): The number of items per schedule. Defaults to 1.
            forbidden_uris (Optional[Sequence[str]], optional): Forbidden URIs. Defaults to None.
            data_freshness (str, optional): The freshness of data to retrieve. Defaults to "realtime".
            disable_geojson (bool, optional): Whether to disable GeoJSON in the response. Defaults to False.
            direction_type (str, optional): The direction type. Defaults to "all".

        Returns:
            Tuple[Sequence[StopSchedule], Pagination]: A tuple containing a sequence of StopSchedule objects and Pagination object.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/stop_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "items_per_schedule": items_per_schedule,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_stop_schedules(request_url, filters)

    def list_stop_schedules_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[StopSchedule], Pagination]:
        """
        Retrieves stop schedules for a specified region and resource path from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            resource_path (str): The resource path.
            from_datetime (datetime, optional): The start datetime for the schedule. Defaults to datetime.now().
            duration (int, optional): The duration of the schedule in seconds. Defaults to 86400.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            items_per_schedule (int, optional): The number of items per schedule. Defaults to 1.
            forbidden_uris (Optional[Sequence[str]], optional): Forbidden URIs. Defaults to None.
            data_freshness (str, optional): The freshness of data to retrieve. Defaults to "realtime".
            disable_geojson (bool, optional): Whether to disable GeoJSON in the response. Defaults to False.
            direction_type (str, optional): The direction type. Defaults to "all".

        Returns:
            Tuple[Sequence[StopSchedule], Pagination]: A tuple containing a sequence of StopSchedule objects and Pagination object.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/stop_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "items_per_schedule": items_per_schedule,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_stop_schedules(request_url, filters)
