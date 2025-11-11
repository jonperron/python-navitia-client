from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.route_schedule import RouteScheduleRequest
from navitia_client.entities.response.route_schedule import RouteSchedule


class RouteSchedulesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching route schedules.
    Uses the RouteScheduleRequest class to encapsulate query parameters.

    See https://doc.navitia.io/#route-schedules
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
        request: RouteScheduleRequest,
    ) -> Sequence[RouteSchedule]:
        """
        Retrieves route schedules for a specified region and resource path from the Navitia API.

        Parameters
        ----------
        region_id : str
            The region ID.
        resource_path : str
            The resource path.
        request : RouteScheduleRequest
            The request object containing query parameters such as from_datetime,
            duration, depth, count, start_page, items_per_schedule, forbidden_uris,
            data_freshness, disable_geojson, and direction_type.

        Returns
        -------
        Sequence[RouteSchedule]
            A sequence of RouteSchedule objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/route_schedules"

        return self._get_routes_nearby(request_url, request.to_filters())

    def list_route_schedules_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: RouteScheduleRequest,
    ) -> Sequence[RouteSchedule]:
        """
        Retrieves route schedules for a specified set of coordinates from the Navitia API.

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
        request : RouteScheduleRequest
            The request object containing query parameters such as from_datetime,
            duration, depth, count, start_page, items_per_schedule, forbidden_uris,
            data_freshness, disable_geojson, and direction_type.

        Returns
        -------
        Sequence[RouteSchedule]
            A sequence of RouteSchedule objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/route_schedules"

        return self._get_routes_nearby(request_url, request.to_filters())
