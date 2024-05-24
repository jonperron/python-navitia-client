from datetime import datetime
from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.route_schedule import RouteSchedule


class RouteSchedulesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching route schedules.

    See https://doc.navitia.io/#route-schedules

    Methods
    -------
    _get_route_schedule_object_from_response(response: Any) -> Sequence[RouteSchedule]:
        A static method to transform raw API response data into a list of RouteSchedule objects.

    list_route_schedules_by_region_id_and_path(
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "base_schedule",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Sequence[RouteSchedule]:
        Retrieves route schedules for a specified region and resource path from the Navitia API.

    list_route_schedules_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "base_schedule",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Sequence[RouteSchedule]:
        Retrieves route schedules for a specified set of coordinates from the Navitia API.
    """

    @staticmethod
    def _get_route_schedule_object_from_response(
        response: Any,
    ) -> Sequence[RouteSchedule]:
        """
        Static method to transform raw API response data into a list of RouteSchedule objects.

        Parameters:
            response (Any): The raw API response data.

        Returns:
            Sequence[RouteSchedule]: A sequence of RouteSchedule objects.
        """
        route_schedules = []
        for route_schedule_data in response:
            route_schedules.append(RouteSchedule.from_payload(route_schedule_data))

        return route_schedules

    def _get_routes_nearby(self, url: str, filters: dict) -> Sequence[RouteSchedule]:
        """
        Retrieves route schedules from the Navitia API based on provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to apply to the API request.

        Returns:
            Sequence[RouteSchedule]: A sequence of RouteSchedule objects.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["route_schedules"]
        return self._get_route_schedule_object_from_response(raw_results)

    def list_route_schedules_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "base_schedule",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Sequence[RouteSchedule]:
        """
        Retrieves route schedules for a specified region and resource path from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            resource_path (str): The resource path.
            from_datetime (datetime, optional): The start datetime for the schedule. Defaults to datetime.now().
            duration (int, optional): The duration of the schedule in seconds. Defaults to 86400.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            items_per_schedule (int, optional): The number of items per schedule. Defaults to 1.
            forbidden_uris (Optional[Sequence[str]], optional): Forbidden URIs. Defaults to None.
            data_freshness (str, optional): The freshness of data to retrieve. Defaults to "base_schedule".
            disable_geojson (bool, optional): Whether to disable GeoJSON in the response. Defaults to False.
            direction_type (str, optional): The direction type. Defaults to "all".

        Returns:
            Sequence[RouteSchedule]: A sequence of RouteSchedule objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/route_schedules"

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

        return self._get_routes_nearby(request_url, filters)

    def list_route_schedules_by_coordinates(
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
        data_freshness: str = "base_schedule",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Sequence[RouteSchedule]:
        """
        Retrieves route schedules for a specified set of coordinates from the Navitia API.

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
            data_freshness (str, optional): The freshness of data to retrieve. Defaults to "base_schedule".
            disable_geojson (bool, optional): Whether to disable GeoJSON in the response. Defaults to False.
            direction_type (str, optional): The direction type. Defaults to "all".

        Returns:
            Sequence[RouteSchedule]: A sequence of RouteSchedule objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/route_schedules"

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

        return self._get_routes_nearby(request_url, filters)
