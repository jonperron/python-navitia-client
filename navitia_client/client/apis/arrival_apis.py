from datetime import datetime
from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.arrival import Arrival


class ArrivalApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching arrival information.

    See https://doc.navitia.io/#arrivals

    Methods
    -------
    _get_departure_objects_from_response(response: Any) -> Sequence[Arrival]
        A static method to transform raw API response data into a list of Arrival objects.

    _get_departures(url: str, filters: dict) -> Tuple[Sequence[Arrival], Pagination]
        Internal method to fetch departures based on a given URL and filters.

    list_arrivals_by_region_id_and_path(region_id: str, resource_path: str, from_datetime: datetime = datetime.now(), duration: int = 86400, depth: int = 1, forbidden_uris: Optional[Sequence[str]] = None, data_freshness: str = "realtime", disable_geojson: bool = False, direction_type: str = "all") -> Tuple[Sequence[Arrival], Pagination]
        Retrieves a list of arrivals for a specific region and resource path.

    list_arrivals_by_coordinates(region_lon: float, region_lat: float, lon: float, lat: float, from_datetime: datetime = datetime.now(), duration: int = 86400, depth: int = 1, forbidden_uris: Optional[Sequence[str]] = None, data_freshness: str = "realtime", disable_geojson: bool = False, direction_type: str = "all") -> Tuple[Sequence[Arrival], Pagination]
        Retrieves a list of arrivals for specific coordinates.
    """

    @staticmethod
    def _get_arrival_objects_from_response(
        response: Any,
    ) -> Sequence[Arrival]:
        """
        Converts raw response data into a list of Arrival objects.

        Parameters
        ----------
        response : Any
            The raw response data from the API containing arrivals' information.

        Returns
        -------
        Sequence[Arrival]
            A list of Arrival objects created from the raw response data.
        """

        arrivals = []
        for arrival_data in response:
            arrivals.append(Arrival.from_payload(arrival_data))

        return arrivals

    def _get_arrivals(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Arrival], Pagination]:
        """
        Internal method to fetch departures based on a given URL and filters.

        Parameters
        ----------
        url : str
            The URL for the API request.
        filters : dict
            The filters to apply to the API request.

        Returns
        -------
        Tuple[Sequence[Arrival], Pagination]
            A tuple containing a list of Arrival objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["arrivals"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_arrival_objects_from_response(raw_results), pagination

    def list_arrivals_by_region_id_and_path(
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
    ) -> Tuple[Sequence[Arrival], Pagination]:
        """
        Retrieves a list of arrivals for a specific region and resource path.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch arrivals from.
        resource_path : str
            The resource path within the region to fetch arrivals for.
        from_datetime : datetime, optional
            The starting datetime for fetching arrivals (default is current datetime).
        duration : int, optional
            The duration in seconds for which to fetch arrivals (default is 86400 seconds).
        depth : int, optional
            The depth of the search (default is 1).
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs to exclude from the search (default is None).
        data_freshness : str, optional
            The freshness of the data to fetch, either "realtime" or "base_schedule" (default is "realtime").
        disable_geojson : bool, optional
            Whether to disable geoJSON in the response (default is False).
        direction_type : str, optional
            The direction type of the arrivals to fetch, e.g., "all", "forward", "backward" (default is "all").

        Returns
        -------
        Tuple[Sequence[Arrival], Pagination]
            A tuple containing a list of Arrival objects and a Pagination object for managing result pages.
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

        return self._get_arrivals(request_url, filters)

    def list_arrivals_by_coordinates(
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
    ) -> Tuple[Sequence[Arrival], Pagination]:
        """
        Retrieves a list of arrivals for specific coordinates.

        Parameters
        ----------
        region_lon : float
            The longitude of the region to fetch arrivals from.
        region_lat : float
            The latitude of the region to fetch arrivals from.
        lon : float
            The longitude of the specific location to fetch arrivals for.
        lat : float
            The latitude of the specific location to fetch arrivals for.
        from_datetime : datetime, optional
            The starting datetime for fetching arrivals (default is current datetime).
        duration : int, optional
            The duration in seconds for which to fetch arrivals (default is 86400 seconds).
        depth : int, optional
            The depth of the search (default is 1).
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs to exclude from the search (default is None).
        data_freshness : str, optional
            The freshness of the data to fetch, either "realtime" or "base_schedule" (default is "realtime").
        disable_geojson : bool, optional
            Whether to disable geoJSON in the response (default is False).
        direction_type : str, optional
            The direction type of the arrivals to fetch, e.g., "all", "forward", "backward" (default is "all").

        Returns
        -------
        Tuple[Sequence[Arrival], Pagination]
            A tuple containing a list of Arrival objects and a Pagination object for managing result pages.
        """
        # List of objects near the resource, navitia guesses the region from coordinates
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

        return self._get_arrivals(request_url, filters)
