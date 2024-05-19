from dataclasses import dataclass
from typing import Any


@dataclass
class Coord:
    lon: float
    lat: float

    @classmethod
    def from_payload(cls, payload: Any) -> "Coord":
        return cls(
            lon=payload.get("lon"),
            lat=payload.get("lat"),
        )
