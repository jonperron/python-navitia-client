from dataclasses import dataclass

from .pt_datetime import PTDatetime
from .stop_area import StopPoint


@dataclass
class StopDateTime:
    date_time: PTDatetime
    stop_point: StopPoint
