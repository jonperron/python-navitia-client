from dataclasses import dataclass
from enum import Enum


class StandStatus(Enum):
    UNAVAILABLE = "unavailable"
    OPEN = "open"
    CLOSED = "closed"


@dataclass
class Stands:
    available_places: int
    available_bikes: int
    total_stands: int
    status: StandStatus
