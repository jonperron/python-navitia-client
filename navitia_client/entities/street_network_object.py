from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence

from navitia_client.entities.base import BaseEntity
from navitia_client.entities.standard import Coord
from navitia_client.entities.public_transport import Line, StopArea


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
class AccessPoint(BaseEntity):
    coord: Coord
    access_point_code: str


@dataclass
class Pathway(BaseEntity):
    is_entrance: bool
    is_exit: bool
    length: int
    traversal_time: int


@dataclass
class AdministrativeRegion(BaseEntity):
    label: str
    coord: Coord
    level: int
    zip_code: str


@dataclass
class Address(BaseEntity):
    label: str
    coord: Coord
    house_number: int
    administrative_regions: Sequence[AdministrativeRegion]


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
