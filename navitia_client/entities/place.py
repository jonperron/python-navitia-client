from dataclasses import dataclass

from .address import Address
from .administrative_region import AdministrativeRegion
from .base_entity import BaseEntity
from .equipment import StopAreaEquipments
from .poi import POI
from .stop_area import StopArea, StopPoint


@dataclass
class PlaceEmbeddedType:
    administrative_region: AdministrativeRegion
    stop_area: StopArea
    stop_point: StopPoint
    address: Address
    poi: POI


@dataclass
class Place(BaseEntity):
    quality: int
    embedded_type: PlaceEmbeddedType
    administrative_region: AdministrativeRegion
    stop_area: StopAreaEquipments
    poi: POI
    address: Address

    stop_point: StopPoint
