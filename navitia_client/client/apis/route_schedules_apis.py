from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.route_schedule import RouteScheduleRequest
from navitia_client.entities.response.route_schedule import RouteSchedule


class RouteSchedulesApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching route schedules.

    See https://doc.navitia.io/#route-schedules
    """

    @staticmethod
    def _get_route_schedule_object_from_response(
        response: Any,
    ) -> Sequence[RouteSchedule]:
        """Transform raw API response data into a list of RouteSchedule objects.

        Args:
            response: The raw API response data.

        Returns:
            A sequence of RouteSchedule objects.
        """
        route_schedules = []
        for route_schedule_data in response:
            route_schedules.append(RouteSchedule.from_payload(route_schedule_data))

        return route_schedules

    def _get_routes_nearby(self, url: str, filters: dict) -> Sequence[RouteSchedule]:
        """Retrieve route schedules from the Navitia API based on provided URL and filters.

        Args:
            url: The URL for the API request.
            filters: Filters to apply to the API request.

        Returns:
            A sequence of RouteSchedule objects.
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
        """Retrieve route schedules for a specified region and resource path.

        Args:
            region_id: The region ID.
            resource_path: The resource path.
            request: The request object containing query parameters.

        Returns:
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
        """Retrieve route schedules for a specified set of coordinates.

        Args:
            region_lon: The longitude of the region.
            region_lat: The latitude of the region.
            lon: The longitude of the coordinates.
            lat: The latitude of the coordinates.
            request: The request object containing query parameters.

        Returns:
            A sequence of RouteSchedule objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/route_schedules"

        return self._get_routes_nearby(request_url, request.to_filters())
