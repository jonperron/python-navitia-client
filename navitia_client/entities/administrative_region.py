from dataclasses import dataclass
from .base_entity import BaseEntity
from .coord import Coord


@dataclass
class AdministrativeRegion(BaseEntity):
    label: str
    coord: Coord
    level: int
    zip_code: str
