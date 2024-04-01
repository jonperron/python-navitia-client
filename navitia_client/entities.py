from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from typing import Any, Optional, Sequence

# TODO: refacto file


@dataclass
class BaseEntity:
    id: str
    name: str


@dataclass
class Coord:
    lon: float
    lat: float


@dataclass
class AdministrativeRegion(BaseEntity):
    label: str
    coord: Coord
    level: int
    zip_code: str


@dataclass
class POIType(BaseEntity):
    pass


class StandStatus(Enum):
    UNAVAILABLE = "unavailable"
    OPEN = "open"
    CLOSED = "closed"


@dataclass
class Stands:
    available_places: int
    available_bikes: int
    total_stands: int
    status: StandStatus


@dataclass
class POI(BaseEntity):
    label: str
    poi_type: POIType
    stands: Stands


@dataclass
class Address(BaseEntity):
    label: str
    coord: Coord
    house_number: int
    administrative_regions: Sequence[AdministrativeRegion]


@dataclass
class Network(BaseEntity):
    pass


@dataclass
class CommercialMode(BaseEntity):
    physical_mode: Sequence["PhysicalMode"]


class PhysicalModeId(Enum):
    AIR = "physical_mode:Air"
    BOAT = "physical_mode:Boat"
    BUS = "physical_mode:Bus"
    BUS_RAPID_TRANSIT = "physical_mode:BusRapidTransit"
    COACH = "physical_mode:Coach"
    FERRY = "physical_mode:Ferry"
    FUNICULAR = "physical_mode:Funicular"
    LOCAL_TRAIN = "physical_mode:LocalTrain"
    LONG_DISTANCE_TRAIN = "physical_mode:LongDistanceTrain"
    METRO = "physical_mode:Metro"
    RAIL_SHUTTLE = "physical_mode:RailShuttle"
    RAPID_TRANSIT = "physical_mode:RapidTransit"
    SHUTTLE = "physical_mode:Shuttle"
    SUSPENDED_CAR_CABLE = "physical_mode:SuspendedCableCar"
    TAXI = "physical_mode:Taxi"
    TRAIN = "physical_mode:Train"
    TRAMWAY = "physical_mode:Tramway"


@dataclass
class PhysicalMode:
    id: PhysicalModeId
    name: str
    commercial_modes: Sequence[CommercialMode]


@dataclass
class Place(BaseEntity):
    quality: int
    embedded_type: "PlaceEmbeddedType"
    administrative_region: AdministrativeRegion
    stop_area: "StopAreaEquipments"
    poi: POI
    address: Address
    stop_point: "StopPoint"


@dataclass
class Route(BaseEntity):
    is_frequence: bool
    line: "Line"
    direction: Place


@dataclass
class Line(BaseEntity):
    code: str
    color: str
    opening_time: str
    closing_time: str
    routes: Sequence[Route]
    commercial_mode: CommercialMode
    physical_modes: Sequence[PhysicalMode]


@dataclass
class StopArea(BaseEntity):
    label: str
    coord: Coord
    administrative_regions: Sequence[AdministrativeRegion]
    stop_points: Sequence["StopPoint"]


@dataclass
class StopPoint(BaseEntity):
    coord: Coord
    administrative_regions: Sequence[AdministrativeRegion]
    equipments: Sequence[str]
    stop_area: StopArea


@dataclass
class Company(BaseEntity):
    pass


@dataclass
class Trip(BaseEntity):
    pass


@dataclass
class PTObjectEmbeddedType:
    network: Network
    commercial_mode: CommercialMode
    line: Line
    route: Route
    stop_area: StopArea
    stop_point: StopPoint
    trip: Trip


@dataclass
class PtObject(BaseEntity):
    quality: int
    embedded_type: PTObjectEmbeddedType
    stop_area: StopArea
    stop_point: StopPoint
    network: Network
    commercial_mode: CommercialMode
    line: Line
    route: Route
    trip: Trip


@dataclass
class EquipmentAvailability:
    status: str
    cause: Optional[str]
    effect: Optional[str]
    periods: Optional[dict[str, str]]


@dataclass
class EquipmentDetails(BaseEntity):
    current_availability: EquipmentAvailability
    embedded_type: str


@dataclass
class StopAreaEquipments:
    equiment_details: EquipmentDetails
    stop_area: StopArea


@dataclass
class EquipmentReports:
    line: Line
    stop_area_equipments: StopAreaEquipments


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


@dataclass
class Region(BaseEntity):
    dataset_created_at: Optional[datetime]
    end_production_date: Optional[datetime]
    last_load_at: Optional[datetime]
    shape: Optional[str]
    start_production_date: Optional[datetime]
    status: Optional[str]


class DisruptionStatus(Enum):
    PAST = "past"
    ACTIVE = "active"
    FUTURE = "future"


class Effect(Enum):
    NO_SERVICE = "no_service"
    REDUCED_SERVICE = "reduced_service"
    SIGNIFICANT_DELAYS = "significant_delays"
    DETOUR = "detour"
    ADDITIONAL_SERVICE = "additional_service"
    MODIFIED_SERVICE = "modified_service"
    OTHER_EFFECT = "other_effect"
    UNKNOWN_EFFECT = "unknown_effect"
    STOP_MOVED = "stop_moved"
    NO_EFFECT = "no_effect"
    ACCESSIBILITY_ISSUE = "accessibility_issue"


@dataclass
class Severity:
    color: str
    priority: int | None
    name: str
    effect: Effect


@dataclass
class DisruptionPeriod:
    begin: datetime
    end: datetime


@dataclass
class Channel:
    id: str
    content_type: str
    name: str


@dataclass
class DisruptionMessage:
    text: str
    channel: Channel


@dataclass
class ImpactedSection:
    section_from: PtObject
    section_to: PtObject
    routes: Route


class StopTimeEffect(Enum):
    ADDED = "added"
    DELETED = "deleted"
    DELAYED = "delayed"
    UNCHANGED = "unchanged"


@dataclass
class ImpactedStop:
    stop_point: StopPoint
    amended_departure_time: str
    amended_arrival_time: str
    base_departure_time: str
    base_arrival_time: str
    cause: str
    stop_time_effect: StopTimeEffect  # written as deprecated in the doc
    arrival_status: StopTimeEffect
    departure_status: StopTimeEffect


@dataclass
class ImpactedObject:
    pt_object: PtObject
    impacted_section: ImpactedSection
    impacted_stops: Sequence[ImpactedStop]


@dataclass
class Disruption:
    id: str
    status: DisruptionStatus
    disruption_id: str
    impact_id: str
    severity: Severity
    application_periods: Sequence[DisruptionPeriod]
    messages: Sequence[DisruptionMessage]
    updated_at: datetime
    impacted_objects: Sequence[ImpactedObject]
    cause: str
    category: str
    contributor: str


@dataclass
class AccessPoint(BaseEntity):
    coord: Coord
    access_point_code: str


@dataclass
class Pathway(BaseEntity):
    is_entrance: bool
    is_exit: bool
    length: int
    traversal_time: int
