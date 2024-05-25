from datetime import datetime
from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.isochrones import Isochrone


class IsochronesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching isochrones data.

    See https://doc.navitia.io/#isochrones-api

    Methods
    -------
    _get_traffic_reports(url: str, filters: dict) -> Sequence[Isochrone]
        Internal method to fetch isochrone data based on the provided URL and filters.

    list_isochrones_with_region_id(
        from_: str,
        region_id: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Sequence[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None
    ) -> Sequence[Isochrone]
        Fetches isochrones data for a specific region based on various parameters.

    list_isochrones(
        from_: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Sequence[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None
    ) -> Sequence[Isochrone]
        Fetches isochrones data based on various parameters.
    """

    def _get_traffic_reports(self, url: str, filters: dict) -> Sequence[Isochrone]:
        """
        Internal method to fetch isochrone data based on the provided URL and filters.

        Parameters
        ----------
        url : str
            The API endpoint URL for fetching isochrone data.
        filters : dict
            The query parameters for filtering the isochrone data.

        Returns
        -------
        Sequence[Isochrone]
            A list of Isochrone objects created from the API response.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        isochrones = [
            Isochrone.from_payload(data) for data in results.json()["isochrones"]
        ]
        return isochrones

    def list_isochrones_with_region_id(
        self,
        from_: str,
        region_id: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Sequence[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None,
    ) -> Sequence[Isochrone]:
        """
        Fetches isochrones data for a specific region based on various parameters.

        Parameters
        ----------
        from_ : str
            The starting point for the isochrone calculation.
        region_id : str
            The identifier of the region.
        start_datetime : datetime, optional
            The starting date and time for the isochrone calculation (default is datetime.now()).
        boundary_duration : Sequence[int], optional
            List of durations in seconds defining the isochrones boundaries.
        to : Optional[str], optional
            The ending point for the isochrone calculation.
        first_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the first section of the journey.
        last_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the last section of the journey.
        min_duration : Optional[int], optional
            The minimum duration for the isochrone calculation.
        max_duration : Optional[int], optional
            The maximum duration for the isochrone calculation.

        Returns
        -------
        Sequence[Isochrone]
            A list of Isochrone objects representing the isochrone data.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/isochrones"

        filters: dict[str, Any] = {
            "datetime": start_datetime.isoformat(),
            "boundary_duration[]": boundary_duration,
            "from": from_,
        }

        if to:
            filters["to"] = to

        if min_duration:
            filters["min_duration"] = min_duration

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if max_duration:
            filters["max_duration"] = max_duration
            if len(boundary_duration) == 0:
                filters.pop("min_duration")

        return self._get_traffic_reports(request_url, filters)

    def list_isochrones(
        self,
        from_: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Sequence[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None,
    ) -> Sequence[Isochrone]:
        """
        Fetches isochrones data based on various parameters.

        Parameters
        ----------
        from_ : str
            The starting point for the isochrone calculation.
        start_datetime : datetime, optional
            The starting date and time for the isochrone calculation (default is datetime.now()).
        boundary_duration : Sequence[int], optional
            List of durations in seconds defining the isochrones boundaries.
        to : Optional[str], optional
            The ending point for the isochrone calculation.
        first_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the first section of the journey.
        last_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the last section of the journey.
        min_duration : Optional[int], optional
            The minimum duration for the isochrone calculation.
        max_duration : Optional[int], optional
            The maximum duration for the isochrone calculation.

        Returns
        -------
        Sequence[Isochrone]
            A list of Isochrone objects representing the isochrone data.
        """
        request_url = f"{self.base_navitia_url}/isochrones"

        filters: dict[str, Any] = {
            "datetime": start_datetime.isoformat(),
            "boundary_duration[]": boundary_duration,
            "from": from_,
        }
        if to:
            filters["to"] = to

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if min_duration:
            filters["min_duration"] = min_duration

        if max_duration:
            filters["max_duration"] = max_duration
            if len(boundary_duration) == 0:
                filters.pop("min_duration")

        return self._get_traffic_reports(request_url, filters)
