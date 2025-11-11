from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional, Sequence

from navitia_client.entities.response import ParkMode
from .base_entity_request import BaseEntityRequest


@dataclass
class JourneyRequest(BaseEntityRequest):
    """
    Request class for Journey queries.

    Attributes
    ----------
    from_ : Optional[str], optional
        The starting point for the journey (default is None).
    to_ : Optional[str], optional
        The ending point for the journey (default is None).
    datetime_ : datetime, optional
        The date and time for the journey calculation (default is datetime.now()).
    datetime_represents : str, optional
        Represents whether the datetime is for departure or arrival (default is "departure").
    traveler_type : str, optional
        The type of traveler (default is "standard").
    data_freshness : str, optional
        The freshness of the data, can be "realtime" or "base_schedule" (default is "realtime").
    forbidden_uris : Optional[Sequence[str]], optional
        A list of URIs that are forbidden in the journey calculation (default is None).
    allowed_id : Optional[Sequence[str]], optional
        A list of allowed IDs for the journey calculation (default is None).
    first_section_mode : Optional[Sequence[str]], optional
        Modes of transportation for the first section of the journey (default is None).
    last_section_mode : Optional[Sequence[str]], optional
        Modes of transportation for the last section of the journey (default is None).
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
        Modes of transportation for direct paths (default is None).
    add_poi_infos : Optional[Sequence[str]], optional
        Additional points of interest information to be included (default is None).
    debug : bool, optional
        Whether to include debug information in the response (default is False).
    free_radius_from : int, optional
        Free radius from the starting point in meters (default is 0).
    free_radius_to : int, optional
        Free radius to the ending point in meters (default is 0).
    timeframe_duration : int, optional
        Timeframe duration in seconds for the journey calculation (default is 0).
    park_mode : ParkMode, optional
        Parking mode for car-based journeys (default is ParkMode.NONE).
    is_journey_schedules : bool, optional
        Whether to return journey schedules instead of journeys (default is False).
    bike_use_hills : Optional[float], optional
        Valhalla parameter: preference for using hills when biking, from 0 (avoid) to 1 (prefer) (default is None).
    walking_use_hills : Optional[float], optional
        Valhalla parameter: preference for using hills when walking, from 0 (avoid) to 1 (prefer) (default is None).
    bike_avoid_bad_surfaces : Optional[float], optional
        Valhalla parameter: preference for avoiding bad surfaces when biking, from 0 (don't avoid) to 1 (strongly avoid) (default is None).
    walking_step_penalty : Optional[float], optional
        Valhalla parameter: penalty applied to steps when walking, in seconds (default is None).
    bike_maneuver_penalty : Optional[float], optional
        Valhalla parameter: penalty applied to maneuvers when biking, in seconds (default is None).
    bike_use_living_streets : Optional[float], optional
        Valhalla parameter: preference for using living streets when biking, from 0 (avoid) to 1 (prefer) (default is None).
    """

    from_: Optional[str] = None
    to_: Optional[str] = None
    datetime_: datetime = field(default_factory=datetime.now)
    datetime_represents: str = "departure"
    traveler_type: str = "standard"
    data_freshness: str = "realtime"
    forbidden_uris: Optional[Sequence[str]] = None
    allowed_id: Optional[Sequence[str]] = None
    first_section_mode: Optional[Sequence[str]] = None
    last_section_mode: Optional[Sequence[str]] = None
    language: str = "en-GB"
    depth: int = 1
    max_duration_to_pt: int = 30 * 60
    walking_speed: float = 1.12
    bike_speed: float = 4.1
    bss_speed: float = 4.1
    car_speed: float = 16.8
    min_nb_journeys: int = 1
    max_nb_journeys: int = 1
    max_nb_transfers: int = 10
    min_nb_transfers: int = 0
    max_duration: int = 86400
    wheelchair: bool = False
    direct_path: str = "indifferent"
    direct_path_mode: Optional[Sequence[str]] = None
    add_poi_infos: Optional[Sequence[str]] = None
    debug: bool = False
    free_radius_from: int = 0
    free_radius_to: int = 0
    timeframe_duration: int = 0
    park_mode: ParkMode = ParkMode.NONE
    is_journey_schedules: bool = False
    bike_use_hills: Optional[float] = None
    walking_use_hills: Optional[float] = None
    bike_avoid_bad_surfaces: Optional[float] = None
    walking_step_penalty: Optional[float] = None
    bike_maneuver_penalty: Optional[float] = None
    bike_use_living_streets: Optional[float] = None

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the JourneyRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters = {
            "datetime": self.datetime_.isoformat(),
            "datetime_represents": self.datetime_represents,
            "traveler_type": self.traveler_type,
            "data_freshness": self.data_freshness,
            "language": self.language,
            "depth": self.depth,
            "max_duration_to_pt": self.max_duration_to_pt,
            "walking_speed": self.walking_speed,
            "bike_speed": self.bike_speed,
            "bss_speed": self.bss_speed,
            "car_speed": self.car_speed,
            "min_nb_journeys": self.min_nb_journeys,
            "max_nb_journeys": self.max_nb_journeys,
            "count": self.count,
            "max_nb_transfers": self.max_nb_transfers,
            "min_nb_transfers": self.min_nb_transfers,
            "max_duration": self.max_duration,
            "wheelchair": self.wheelchair,
            "direct_path": self.direct_path,
            "debug": self.debug,
            "free_radius_from": self.free_radius_from,
            "free_radius_to": self.free_radius_to,
            "timeframe_duration": self.timeframe_duration,
            "is_journey_schedules": self.is_journey_schedules,
            "park_mode": self.park_mode.value,
        }

        if self.from_:
            filters["from"] = self.from_

        if self.to_:
            filters["to"] = self.to_

        if self.bike_use_hills is not None:
            filters["bike_use_hills"] = self.bike_use_hills

        if self.walking_use_hills is not None:
            filters["walking_use_hills"] = self.walking_use_hills

        if self.bike_avoid_bad_surfaces is not None:
            filters["bike_avoid_bad_surfaces"] = self.bike_avoid_bad_surfaces

        if self.walking_step_penalty is not None:
            filters["walking_step_penalty"] = self.walking_step_penalty

        if self.bike_maneuver_penalty is not None:
            filters["bike_maneuver_penalty"] = self.bike_maneuver_penalty

        if self.bike_use_living_streets is not None:
            filters["bike_use_living_streets"] = self.bike_use_living_streets

        if self.forbidden_uris:
            filters["forbidden_uris[]"] = self.forbidden_uris

        if self.allowed_id:
            filters["allowed_id[]"] = self.allowed_id

        if self.first_section_mode:
            filters["first_section_mode[]"] = self.first_section_mode

        if self.last_section_mode:
            filters["last_section_mode[]"] = self.last_section_mode

        if self.add_poi_infos:
            filters["add_poi_infos[]"] = self.add_poi_infos

        # Special logic: direct_path_mode defaults to first_section_mode if not provided
        if any([self.direct_path_mode, self.first_section_mode]):
            filters["direct_path_mode[]"] = (
                self.direct_path_mode or self.first_section_mode
            )

        return filters
