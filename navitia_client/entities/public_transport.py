from enum import Enum
from dataclasses import dataclass
from typing import Sequence

from navitia_client.entities.base import BaseEntity
from navitia_client.entities.standard import Coord
from navitia_client.entities.street_network_object import (
    AdministrativeRegion,
    Address,
    POI,
    StopAreaEquipments,
)
from navitia_client.entities.others import PlaceEmbeddedType


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
    embedded_type: PlaceEmbeddedType
    administrative_region: AdministrativeRegion
    stop_area: StopAreaEquipments
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
