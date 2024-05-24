from datetime import datetime
from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.departure import Departure


class DepartureApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching departure information.

    See https://doc.navitia.io/#departures

    Methods
    -------
    _get_departure_objects_from_response(response: Any) -> Sequence[Departure]
        A static method to transform raw API response data into a list of Departure objects.

    _get_departures(url: str, filters: dict) -> Tuple[Sequence[Departure], Pagination]
        Fetches departures from the Navitia API based on the provided URL and filters.

    list_departures_by_region_id_and_path(
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all"
    ) -> Tuple[Sequence[Departure], Pagination]
        Retrieves a list of departures for a specified region and resource path from the Navitia API.

    list_departures_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all"
    ) -> Tuple[Sequence[Departure], Pagination]
        Retrieves a list of departures for a specified location based on coordinates from the Navitia API.
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
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[Departure], Pagination]:
        """
        Retrieves a list of departures for a specified region and resource path from the Navitia API.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch departures from.
        resource_path : str
            The resource path to fetch departures for.
        from_datetime : datetime, optional
            The starting datetime for fetching departures (default is current time).
        duration : int, optional
            The duration for which to fetch departures, in seconds (default is 86400 seconds, i.e., 1 day).
        depth : int, optional
            The depth of the search (default is 1).
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs to exclude from the search (default is None).
        data_freshness : str, optional
            The data freshness parameter (default is "realtime").
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        direction_type : str, optional
            The direction type for the departures (default is "all").

        Returns
        -------
        Tuple[Sequence[Departure], Pagination]
            A tuple containing a list of Departure objects and a Pagination object for managing result pages.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/terminus_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_departures(request_url, filters)

    def list_departures_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[Departure], Pagination]:
        """
        Retrieves a list of departures for a specified location based on coordinates from the Navitia API.

        Parameters
        ----------
        region_lon : float
            The longitude of the region to fetch departures for.
        region_lat : float
            The latitude of the region to fetch departures for.
        lon : float
            The longitude of the specific location to fetch departures for.
        lat : float
            The latitude of the specific location to fetch departures for.
        from_datetime : datetime, optional
            The starting datetime for fetching departures (default is current time).
        duration : int, optional
            The duration for which to fetch departures, in seconds (default is 86400 seconds, i.e., 1 day).
        depth : int, optional
            The depth of the search (default is 1).
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs to exclude from the search (default is None).
        data_freshness : str, optional
            The data freshness parameter (default is "realtime").
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        direction_type : str, optional
            The direction type for the departures (default is "all").

        Returns
        -------
        Tuple[Sequence[Departure], Pagination]
            A tuple containing a list of Departure objects and a Pagination object for managing result pages.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/terminus_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_departures(request_url, filters)
