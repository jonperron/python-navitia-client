from dataclasses import dataclass
from typing import Any


@dataclass
class Coord:
    lon: float
    lat: float

    @staticmethod
    def from_json(payload: Any) -> "Coord":
        return Coord(
            lon=payload.get("lon"),
            lat=payload.get("lat"),
        )
