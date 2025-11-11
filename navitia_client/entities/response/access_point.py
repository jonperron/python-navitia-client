from dataclasses import dataclass

from .base_entity import BaseEntity
from .coord import Coord


@dataclass
class AccessPoint(BaseEntity):
    coord: Coord
    access_point_code: str
