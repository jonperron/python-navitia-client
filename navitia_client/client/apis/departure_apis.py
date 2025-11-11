from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.departure import DepartureRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.departure import Departure


class DepartureApiClient(ApiBaseClient):
    """
    This module provides a client for interacting with the Navitia API to retrieve departure schedules.

    It includes the `DepartureApiClient` class, which allows users to fetch departure information
    based on region ID and resource paths or by specifying coordinates. The client uses the
    `DepartureRequest` class to encapsulate query parameters.

    Classes
    -------
    DepartureApiClient
        A client for accessing departure schedules from the Navitia API.
    """

    @staticmethod
    def _get_departure_objects_from_response(
        response: Any,
    ) -> Sequence[Departure]:
        """
        Converts raw response data into a list of Departure objects.

        Parameters
        ----------
        response : Any
            The raw response data from the API containing departures' information.

        Returns
        -------
        Sequence[Departure]
            A list of Departure objects created from the raw response data.
        """
        departures = []
        for departure_data in response:
            departures.append(Departure.from_payload(departure_data))

        return departures

    def _get_departures(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Departure], Pagination]:
        """
        Fetches departures from the Navitia API based on the provided URL and filters.

        Parameters
        ----------
        url : str
            The URL to fetch departures from.
        filters : dict
            A dictionary of filters to apply to the query.

        Returns
        -------
        Tuple[Sequence[Departure], Pagination]
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
        """
        Retrieves a list of departures for a specified region and resource path from the Navitia API.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch departures from.
        resource_path : str
            The resource path to fetch departures for.
        request : DepartureRequest
            The request object containing query parameters such as from_datetime,
            duration, depth, count, start_page, forbidden_uris, data_freshness,
            disable_geojson, and direction_type.

        Returns
        -------
        Tuple[Sequence[Departure], Pagination]
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
        """
        Retrieves a list of departures for a specified region and coordinates from the Navitia API.

        Parameters
        ----------
        region_lon : float
            The longitude of the region.
        region_lat : float
            The latitude of the region.
        lon : float
            The longitude of the specific location.
        lat : float
            The latitude of the specific location.
        request : DepartureRequest
            The request object containing query parameters such as from_datetime,
            duration, depth, count, start_page, forbidden_uris, data_freshness,
            disable_geojson, and direction_type.

        Returns
        -------
        Tuple[Sequence[Departure], Pagination]
            A tuple containing a list of Departure objects and a Pagination object for managing result pages.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/departures"

        return self._get_departures(request_url, request.to_filters())
