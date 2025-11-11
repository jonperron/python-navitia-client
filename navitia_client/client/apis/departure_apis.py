from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.departure import DepartureRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.departure import Departure


class DepartureApiClient(ApiBaseClient):
    """Client for interacting with the Navitia API to retrieve departure schedules.

    See https://doc.navitia.io/#departures
    """

    @staticmethod
    def _get_departure_objects_from_response(
        response: Any,
    ) -> Sequence[Departure]:
        """Convert raw response data into a list of Departure objects.

        Args:
            response: The raw response data from the API containing departures' information.

        Returns:
            A list of Departure objects created from the raw response data.
        """
        departures = []
        for departure_data in response:
            departures.append(Departure.from_payload(departure_data))

        return departures

    def _get_departures(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Departure], Pagination]:
        """Fetch departures from the Navitia API based on the provided URL and filters.

        Args:
            url: The URL to fetch departures from.
            filters: A dictionary of filters to apply to the query.

        Returns:
            A tuple containing a list of Departure objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["departures"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_departure_objects_from_response(raw_results), pagination

    def list_departures_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        request: DepartureRequest,
    ) -> Tuple[Sequence[Departure], Pagination]:
        """Retrieve a list of departures for a specified region and resource path.

        Args:
            region_id: The identifier of the region to fetch departures from.
            resource_path: The resource path to fetch departures for.
            request: The request object containing query parameters.

        Returns:
            A tuple containing a list of Departure objects and a Pagination object for managing result pages.
        """
        request_url = (
            f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/departures"
        )

        return self._get_departures(request_url, request.to_filters())

    def list_departures_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: DepartureRequest,
    ) -> Tuple[Sequence[Departure], Pagination]:
        """Retrieve a list of departures for a specified region and coordinates.

        Args:
            region_lon: The longitude of the region.
            region_lat: The latitude of the region.
            lon: The longitude of the specific location.
            lat: The latitude of the specific location.
            request: The request object containing query parameters.

        Returns:
            A tuple containing a list of Departure objects and a Pagination object for managing result pages.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/departures"

        return self._get_departures(request_url, request.to_filters())
