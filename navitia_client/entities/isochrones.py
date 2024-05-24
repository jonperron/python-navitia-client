from dataclasses import dataclass
from datetime import datetime
from typing import Any

from navitia_client.entities.place import Place


@dataclass
class Isochrone:
    from_: Place
    geojson: Any
    max_date_time: datetime
    max_duration: int
    min_date_time: datetime
    min_duration: int
    requested_date_time: datetime

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Isochrone":
        return cls(
            from_=Place.from_payload(payload["from"]),
            geojson=payload["geojson"],
            max_date_time=datetime.strptime(payload["max_date_time"], "%Y%m%dT%H%M%S"),
            max_duration=payload["max_duration"],
            min_date_time=datetime.strptime(payload["min_date_time"], "%Y%m%dT%H%M%S"),
            min_duration=payload["min_duration"],
            requested_date_time=datetime.strptime(
                payload["requested_date_time"], "%Y%m%dT%H%M%S"
            ),
        )
