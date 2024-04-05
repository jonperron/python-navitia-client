from dataclasses import dataclass
from typing import Sequence

from .base_entity import BaseEntity
from .coord import Coord
from .administrative_region import AdministrativeRegion


@dataclass
class Address(BaseEntity):
    label: str
    coord: Coord
    house_number: int
    administrative_regions: Sequence[AdministrativeRegion]
