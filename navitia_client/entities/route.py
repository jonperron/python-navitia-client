from dataclasses import dataclass

from .base_entity import BaseEntity
from .line import Line
from .place import Place


@dataclass
class Route(BaseEntity):
    is_frequence: bool
    line: Line
    direction: Place
