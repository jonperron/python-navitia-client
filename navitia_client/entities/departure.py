from dataclasses import dataclass
from typing import Any

from navitia_client.entities.line_and_route import Route
from navitia_client.entities.stop_area import StopPoint
from navitia_client.entities.stop_datetime import StopDateTime


@dataclass
class Departure:
    route: Route
    stop_date_time: StopDateTime
    stop_point: StopPoint

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Departure":
        return cls(
            route=Route.from_payload(payload["route"]),
            stop_point=StopPoint.from_payload(payload["stop_point"]),
            stop_date_time=StopDateTime.from_payload(payload["stop_date_time"]),
        )
