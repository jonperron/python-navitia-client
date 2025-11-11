from dataclasses import dataclass

from .base_entity import BaseEntity
from .stand import Stands


@dataclass
class POIType(BaseEntity):
    pass


@dataclass
class POI(BaseEntity):
    label: str
    poi_type: POIType
    stands: Stands
