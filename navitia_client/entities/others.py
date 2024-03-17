from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Optional, Sequence

from navitia_client.entities.public_transport import (
    CommercialMode,
    Line,
    Network,
    PhysicalMode,
    Route,
    StopArea,
    StopPoint,
    Trip,
)
from navitia_client.entities.street_network_object import (
    POI,
    Address,
    AdministrativeRegion,
)


@dataclass
class Context:
    timezone: str
    current_datetime: datetime
    car_direct_path: dict[str, Any]


@dataclass
class PTDatetime:
    additional_information: Sequence[str]
    departure_date_time: datetime
    arrival_date_time: datetime
    links: Sequence[dict[str, Any]]


@dataclass
class Note:
    id: str
    value: str


@dataclass
class StopDateTime:
    date_time: PTDatetime
    stop_point: StopPoint


@dataclass
class PlaceEmbeddedType:
    administrative_region: AdministrativeRegion
    stop_area: StopArea
    stop_point: StopPoint
    address: Address
    poi: POI


@dataclass
class PTObjectEmbeddedType:
    network: Network
    commercial_mode: CommercialMode
    line: Line
    route: Route
    stop_area: StopArea
    stop_point: StopPoint
    trip: Trip


class Equiment(Enum):
    WHEELCHAIR_ACCESSIBILITY = "has_wheelchair_accessibility"
    BIKE_ACCEPTED = "has_bike_accepted"
    AIR_CONDITIONED = "has_air_conditioned"
    VISUAL_ANNOUNCEMENT = "has_visual_announcement"
    AUDIBLE_ANNOUNCEMENT = "has_audible_announcement"
    APPROPRIATE_ESCORT = "has_appropriate_escort"
    APPROPRIATE_SIGNAGE = "has_appropriate_signage"
    SCHOOL_VEHICLE = "has_school_vehicle"
    WHEELCHAR_BOARDING = "has_wheelchair_boarding"
    SHELTERED = "has_sheltered"
    ELEVATOR = "has_elevator"
    ESCALATOR = "has_escalator"
    BIKE_DEPOT = "has_bike_depot"


@dataclass
class DisplayInformation:
    network: Network
    physical_mode: PhysicalMode
    commercial_mode: CommercialMode
    code: str
    color: str
    text_color: str
    direction: str
    headsign: str
    label: str
    name: str
    trip_short_name: str
    equipments: Sequence[Equiment]
    description: Optional[str]
