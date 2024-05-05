from dataclasses import dataclass
from typing import Any

from .address import Address
from .administrative_region import AdministrativeRegion
from .base_entity import BaseEntity
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
    embedded_type: str
    stop_area: StopArea

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "Place":
        return cls(
            id=payload["id"],
            name=payload["name"],
            embedded_type=payload["embedded_type"],
            quality=payload["quality"],
            stop_area=StopArea.from_json(payload["stop_area"]),
        )
