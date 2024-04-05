from dataclasses import dataclass

from .base_entity import BaseEntity
from .physical_mode import CommercialMode
from .network import Network
from .line import Line
from .route import Route
from .stop_area import StopArea, StopPoint
from .trip import Trip


@dataclass
class PtObjectEmbeddedType:
    network: Network
    commercial_mode: CommercialMode
    line: Line
    route: Route
    stop_area: StopArea
    stop_point: StopPoint
    trip: Trip


@dataclass
class PtObject(BaseEntity):
    quality: int
    embedded_type: PtObjectEmbeddedType
    stop_area: StopArea
    stop_point: StopPoint
    network: Network
    commercial_mode: CommercialMode
    line: Line
    route: Route
    trip: Trip
