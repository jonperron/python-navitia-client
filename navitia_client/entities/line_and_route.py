from dataclasses import dataclass

from typing import Sequence

from .base_entity import BaseEntity
from .physical_mode import CommercialMode, PhysicalMode
from .place import Place


@dataclass
class Line(BaseEntity):
    code: str
    color: str
    opening_time: str
    closing_time: str
    routes: Sequence["Route"]
    commercial_mode: CommercialMode
    physical_modes: Sequence[PhysicalMode]


@dataclass
class Route(BaseEntity):
    is_frequence: bool
    line: Line
    direction: Place