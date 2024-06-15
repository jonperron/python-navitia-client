from datetime import datetime
from typing import Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.journey import Journey


class JourneyApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching journey data.

    See https://doc.navitia.io/#journeys

    Methods
    -------
    _get_journeys(url: str, filters: dict) -> Sequence[Journey]
        Internal method to fetch journey data based on the provided URL and filters.

    list_journeys(
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Optional[Sequence[str]] = None,
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0
    ) -> Sequence[Journey]
        Fetches journey data based on various parameters.

    list_journeys_with_region_id(
        self,
        region_id: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Optional[Sequence[str]] = None,
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0
    ) -> Sequence[Journey]
        Fetches journey data for a specific region based on various parameters.

    list_journeys_with_resource_path(
        self,
        resource_path: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Optional[Sequence[str]] = None,
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0
    ) -> Sequence[Journey]
        Fetches journey data for a specific resource path based on various parameters.
    """

    def _get_journeys(self, url: str, filters: dict) -> Sequence[Journey]:
        """
        Internal method to fetch journey data based on the provided URL and filters.

        Parameters
        ----------
        url : str
            The API endpoint URL for fetching journey data.
        filters : dict
            The query parameters for filtering the journey data.

        Returns
        -------
        Sequence[Journey]
            A list of Journey objects created from the API response.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        journeys = [Journey.from_payload(data) for data in results.json()["journeys"]]
        return journeys

    def list_journeys(
        self,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Optional[Sequence[str]] = None,
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0,
    ) -> Sequence[Journey]:
        """
        Fetches journey data based on various parameters.

        Parameters
        ----------
        from_ : Optional[str], optional
            The starting point for the journey.
        to_ : Optional[str], optional
            The ending point for the journey.
        datetime_ : datetime, optional
            The date and time for the journey calculation (default is datetime.now()).
        datetime_represents : str, optional
            Represents whether the datetime is for departure or arrival (default is "departure").
        traveler_type : str, optional
            The type of traveler (default is "standard").
        data_freshness : str, optional
            The freshness of the data, can be "realtime" or "base_schedule" (default is "realtime").
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs that are forbidden in the journey calculation.
        allowed_id : Optional[Sequence[str]], optional
            A list of allowed IDs for the journey calculation.
        first_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the first section of the journey.
        last_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the last section of the journey.
        language : str, optional
            The language for the journey results (default is "en-GB").
        depth : int, optional
            The depth of the journey search (default is 1).
        max_duration_to_pt : int, optional
            Maximum duration to public transportation in seconds (default is 30 * 60).
        walking_speed : float, optional
            Walking speed in meters per second (default is 1.12).
        bike_speed : float, optional
            Bike speed in meters per second (default is 4.1).
        bss_speed : float, optional
            Bike-sharing speed in meters per second (default is 4.1).
        car_speed : float, optional
            Car speed in meters per second (default is 16.8).
        min_nb_journeys : int, optional
            Minimum number of journeys to be returned (default is 1).
        max_nb_journeys : int, optional
            Maximum number of journeys to be returned (default is 1).
        count : int, optional
            Number of journey results to return (default is 1).
        max_nb_transfers : int, optional
            Maximum number of transfers allowed in the journey (default is 10).
        min_nb_transfers : int, optional
            Minimum number of transfers required in the journey (default is 0).
        max_duration : int, optional
            Maximum duration of the journey in seconds (default is 86400).
        wheelchair : bool, optional
            Whether the journey should be wheelchair accessible (default is False).
        direct_path : str, optional
            Preference for direct paths, can be "indifferent", "requested", or "forbidden" (default is "indifferent").
        direct_path_mode : Optional[Sequence[str]], optional
            Modes of transportation for direct paths.
        add_poi_infos : Sequence[str], optional
            Additional points of interest information to be included.
        debug : bool, optional
            Whether to include debug information in the response (default is False).
        free_radius_from : int, optional
            Free radius from the starting point in meters (default is 0).
        free_radius_to : int, optional
            Free radius to the ending point in meters (default is 0).
        timeframe_duration : int, optional
            Timeframe duration in seconds for the journey calculation (default is 0).

        Returns
        -------
        Sequence[Journey]
            A list of Journey objects representing the journey results.
        """
        request_url = f"{self.base_navitia_url}/journeys"

        filters = {
            "datetime": datetime_.isoformat(),
            "datetime_represents": datetime_represents,
            "traveler_type": traveler_type,
            "data_freshness": data_freshness,
            "language": language,
            "depth": depth,
            "max_duration_to_pt": max_duration_to_pt,
            "walking_speed": walking_speed,
            "bike_speed": bike_speed,
            "bss_speed": bss_speed,
            "car_speed": car_speed,
            "min_nb_journeys": min_nb_journeys,
            "max_nb_journeys": max_nb_journeys,
            "count": count,
            "max_nb_transfers": max_nb_transfers,
            "min_nb_transfers": min_nb_transfers,
            "max_duration": max_duration,
            "wheelchair": wheelchair,
            "direct_path": direct_path,
            "debug": debug,
            "free_radius_from": free_radius_from,
            "free_radius_to": free_radius_to,
            "timeframe_duration": timeframe_duration,
        }

        if from_:
            filters["from"] = from_

        if to_:
            filters["to"] = to_

        if forbidden_uris:
            filters["forbidden_uris[]"] = forbidden_uris

        if allowed_id:
            filters["allowed_id[]"] = allowed_id

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if add_poi_infos:
            filters["add_poi_infos[]"] = add_poi_infos

        if any([direct_path_mode, first_section_mode]):
            filters["direct_path_mode[]"] = direct_path_mode or first_section_mode

        return self._get_journeys(request_url, filters)

    def list_journeys_with_region_id(
        self,
        region_id: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Optional[Sequence[str]] = None,
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0,
    ) -> Sequence[Journey]:
        """
        Fetches journey data for a specific region based on various parameters.

        Parameters
        ----------
        region_id : str
            The ID of the region to fetch journey data for.
        from_ : Optional[str], optional
            The starting point for the journey.
        to_ : Optional[str], optional
            The ending point for the journey.
        datetime_ : datetime, optional
            The date and time for the journey calculation (default is datetime.now()).
        datetime_represents : str, optional
            Represents whether the datetime is for departure or arrival (default is "departure").
        traveler_type : str, optional
            The type of traveler (default is "standard").
        data_freshness : str, optional
            The freshness of the data, can be "realtime" or "base_schedule" (default is "realtime").
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs that are forbidden in the journey calculation.
        allowed_id : Optional[Sequence[str]], optional
            A list of allowed IDs for the journey calculation.
        first_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the first section of the journey.
        last_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the last section of the journey.
        language : str, optional
            The language for the journey results (default is "en-GB").
        depth : int, optional
            The depth of the journey search (default is 1).
        max_duration_to_pt : int, optional
            Maximum duration to public transportation in seconds (default is 30 * 60).
        walking_speed : float, optional
            Walking speed in meters per second (default is 1.12).
        bike_speed : float, optional
            Bike speed in meters per second (default is 4.1).
        bss_speed : float, optional
            Bike-sharing speed in meters per second (default is 4.1).
        car_speed : float, optional
            Car speed in meters per second (default is 16.8).
        min_nb_journeys : int, optional
            Minimum number of journeys to be returned (default is 1).
        max_nb_journeys : int, optional
            Maximum number of journeys to be returned (default is 1).
        count : int, optional
            Number of journey results to return (default is 1).
        max_nb_transfers : int, optional
            Maximum number of transfers allowed in the journey (default is 10).
        min_nb_transfers : int, optional
            Minimum number of transfers required in the journey (default is 0).
        max_duration : int, optional
            Maximum duration of the journey in seconds (default is 86400).
        wheelchair : bool, optional
            Whether the journey should be wheelchair accessible (default is False).
        direct_path : str, optional
            Preference for direct paths, can be "indifferent", "requested", or "forbidden" (default is "indifferent").
        direct_path_mode : Optional[Sequence[str]], optional
            Modes of transportation for direct paths.
        add_poi_infos : Sequence[str], optional
            Additional points of interest information to be included.
        debug : bool, optional
            Whether to include debug information in the response (default is False).
        free_radius_from : int, optional
            Free radius from the starting point in meters (default is 0).
        free_radius_to : int, optional
            Free radius to the ending point in meters (default is 0).
        timeframe_duration : int, optional
            Timeframe duration in seconds for the journey calculation (default is 0).

        Returns
        -------
        Sequence[Journey]
            A list of Journey objects representing the journey results for the specified region.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/journeys"

        filters = {
            "datetime": datetime_.isoformat(),
            "datetime_represents": datetime_represents,
            "traveler_type": traveler_type,
            "data_freshness": data_freshness,
            "language": language,
            "depth": depth,
            "max_duration_to_pt": max_duration_to_pt,
            "walking_speed": walking_speed,
            "bike_speed": bike_speed,
            "bss_speed": bss_speed,
            "car_speed": car_speed,
            "min_nb_journeys": min_nb_journeys,
            "max_nb_journeys": max_nb_journeys,
            "count": count,
            "max_nb_transfers": max_nb_transfers,
            "min_nb_transfers": min_nb_transfers,
            "max_duration": max_duration,
            "wheelchair": wheelchair,
            "direct_path": direct_path,
            "debug": debug,
            "free_radius_from": free_radius_from,
            "free_radius_to": free_radius_to,
            "timeframe_duration": timeframe_duration,
        }

        if from_:
            filters["from"] = from_

        if to_:
            filters["to"] = to_

        if forbidden_uris:
            filters["forbidden_uris[]"] = forbidden_uris

        if allowed_id:
            filters["allowed_id[]"] = allowed_id

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if add_poi_infos:
            filters["add_poi_infos[]"] = add_poi_infos

        if any([direct_path_mode, first_section_mode]):
            filters["direct_path_mode[]"] = direct_path_mode or first_section_mode

        return self._get_journeys(request_url, filters)

    def list_journeys_with_resource_path(
        self,
        resource_path: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Optional[Sequence[str]] = None,
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0,
    ) -> Sequence[Journey]:
        """
        Fetches journey data for a specific resource path based on various parameters.

        Parameters
        ----------
        region_id : str
            The ID of the region to fetch journey data for.
        from_ : Optional[str], optional
            The starting point for the journey.
        to_ : Optional[str], optional
            The ending point for the journey.
        datetime_ : datetime, optional
            The date and time for the journey calculation (default is datetime.now()).
        datetime_represents : str, optional
            Represents whether the datetime is for departure or arrival (default is "departure").
        traveler_type : str, optional
            The type of traveler (default is "standard").
        data_freshness : str, optional
            The freshness of the data, can be "realtime" or "base_schedule" (default is "realtime").
        forbidden_uris : Optional[Sequence[str]], optional
            A list of URIs that are forbidden in the journey calculation.
        allowed_id : Optional[Sequence[str]], optional
            A list of allowed IDs for the journey calculation.
        first_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the first section of the journey.
        last_section_mode : Optional[Sequence[str]], optional
            Modes of transportation for the last section of the journey.
        language : str, optional
            The language for the journey results (default is "en-GB").
        depth : int, optional
            The depth of the journey search (default is 1).
        max_duration_to_pt : int, optional
            Maximum duration to public transportation in seconds (default is 30 * 60).
        walking_speed : float, optional
            Walking speed in meters per second (default is 1.12).
        bike_speed : float, optional
            Bike speed in meters per second (default is 4.1).
        bss_speed : float, optional
            Bike-sharing speed in meters per second (default is 4.1).
        car_speed : float, optional
            Car speed in meters per second (default is 16.8).
        min_nb_journeys : int, optional
            Minimum number of journeys to be returned (default is 1).
        max_nb_journeys : int, optional
            Maximum number of journeys to be returned (default is 1).
        count : int, optional
            Number of journey results to return (default is 1).
        max_nb_transfers : int, optional
            Maximum number of transfers allowed in the journey (default is 10).
        min_nb_transfers : int, optional
            Minimum number of transfers required in the journey (default is 0).
        max_duration : int, optional
            Maximum duration of the journey in seconds (default is 86400).
        wheelchair : bool, optional
            Whether the journey should be wheelchair accessible (default is False).
        direct_path : str, optional
            Preference for direct paths, can be "indifferent", "requested", or "forbidden" (default is "indifferent").
        direct_path_mode : Optional[Sequence[str]], optional
            Modes of transportation for direct paths.
        add_poi_infos : Sequence[str], optional
            Additional points of interest information to be included.
        debug : bool, optional
            Whether to include debug information in the response (default is False).
        free_radius_from : int, optional
            Free radius from the starting point in meters (default is 0).
        free_radius_to : int, optional
            Free radius to the ending point in meters (default is 0).
        timeframe_duration : int, optional
            Timeframe duration in seconds for the journey calculation (default is 0).

        Returns
        -------
        Sequence[Journey]
            A list of Journey objects representing the journey results for the specified region.
        """
        request_url = f"{self.base_navitia_url}/coverage/{resource_path}/journeys"

        filters = {
            "datetime": datetime_.isoformat(),
            "datetime_represents": datetime_represents,
            "traveler_type": traveler_type,
            "data_freshness": data_freshness,
            "language": language,
            "depth": depth,
            "max_duration_to_pt": max_duration_to_pt,
            "walking_speed": walking_speed,
            "bike_speed": bike_speed,
            "bss_speed": bss_speed,
            "car_speed": car_speed,
            "min_nb_journeys": min_nb_journeys,
            "max_nb_journeys": max_nb_journeys,
            "count": count,
            "max_nb_transfers": max_nb_transfers,
            "min_nb_transfers": min_nb_transfers,
            "max_duration": max_duration,
            "wheelchair": wheelchair,
            "direct_path": direct_path,
            "debug": debug,
            "free_radius_from": free_radius_from,
            "free_radius_to": free_radius_to,
            "timeframe_duration": timeframe_duration,
        }

        if from_:
            filters["from"] = from_

        if to_:
            filters["to"] = to_

        if forbidden_uris:
            filters["forbidden_uris[]"] = forbidden_uris

        if allowed_id:
            filters["allowed_id[]"] = allowed_id

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if add_poi_infos:
            filters["add_poi_infos[]"] = add_poi_infos

        if any([direct_path_mode, first_section_mode]):
            filters["direct_path_mode[]"] = direct_path_mode or first_section_mode

        return self._get_journeys(request_url, filters)
