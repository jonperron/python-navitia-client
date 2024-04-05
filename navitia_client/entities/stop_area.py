from dataclasses import dataclass
from typing import Sequence


from .base_entity import BaseEntity
from .coord import Coord
from .administrative_region import AdministrativeRegion


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
