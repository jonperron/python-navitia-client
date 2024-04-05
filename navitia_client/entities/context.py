from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Context:
    timezone: str
    current_datetime: datetime
    car_direct_path: dict[str, Any]
