from dataclasses import dataclass

from typing import Any, Optional, Sequence

from navitia_client.entities.direction import Direction
from navitia_client.entities.network import Network

from navitia_client.entities.base_entity import BaseEntity
from navitia_client.entities.physical_mode import CommercialMode, PhysicalMode


@dataclass
class Line(BaseEntity):
    code: str
    color: str
    opening_time: str
    closing_time: str
    routes: Optional[Sequence["Route"]]
    commercial_mode: CommercialMode
    physical_modes: Sequence[PhysicalMode]
    text_color: Optional[str]
    network: Network

    @classmethod
    def from_payload(
        cls,
        payload: Any,
    ) -> "Line":
        routes = (
            [Route.from_payload(route) for route in payload["routes"]]
            if "routes" in payload
            else None
        )

        physical_modes = [
            PhysicalMode.from_payload(physical_mode)
            for physical_mode in payload["physical_modes"]
        ]

        return cls(
            id=payload["id"],
            name=payload["name"],
            code=payload["code"],
            color=payload["color"],
            opening_time=payload["opening_time"],
            closing_time=payload["closing_time"],
            routes=routes,
            commercial_mode=CommercialMode.from_payload(payload["commercial_mode"]),
            physical_modes=physical_modes,
            text_color=payload["text_color"],
            network=Network.from_payload(payload["network"]),
        )


@dataclass
class Route(BaseEntity):
    is_frequence: bool
    line: Optional[Line]
    direction: Direction
    direction_type: str

    @classmethod
    def from_payload(
        cls,
        payload: dict[str, Any],
    ) -> "Route":
        line = Line.from_payload(payload["line"]) if "line" in payload else None

        return cls(
            id=payload["id"],
            name=payload["name"],
            is_frequence=bool(payload["is_frequence"]),
            direction_type=payload["direction_type"],
            direction=Direction.from_payload(payload["direction"]),
            line=line,
        )
