from dataclasses import dataclass
from typing import Any, Optional

from .base_entity import BaseEntity
from .physical_mode import CommercialMode
from .network import Network
from .line_and_route import Line, Route
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
    embedded_type: str
    stop_area: Optional[StopArea]
    stop_point: Optional[StopPoint]
    network: Optional[Network]
    commercial_mode: Optional[CommercialMode]
    line: Optional[Line]
    route: Optional[Route]
    trip: Optional[Trip]

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "PtObject":
        return PtObject(
            id=payload["id"],
            name=payload["name"],
            quality=payload["quality"],
            embedded_type=payload["embedded_type"],
            stop_area=StopArea.from_json(payload["stop_area"])
            if "stop_area" in payload
            else None,
            stop_point=StopPoint.from_json(payload["stop_point"])
            if "stop_point" in payload
            else None,
            network=Network.from_json(payload["network"])
            if "network" in payload
            else None,
            commercial_mode=CommercialMode.from_json(payload["commercial_mode"])
            if "commercial_mode" in payload
            else None,
            line=Line.from_json(payload["line"]) if "line" in payload else None,
            route=Route.from_json(payload["route"]) if "route" in payload else None,
            trip=Trip.from_json(payload["trip"]) if "trip" in payload else None,
        )
