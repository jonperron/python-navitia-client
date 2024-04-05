from dataclasses import dataclass
from datetime import datetime
from typing import Any, Sequence


@dataclass
class PTDatetime:
    additional_information: Sequence[str]
    departure_date_time: datetime
    arrival_date_time: datetime
    links: Sequence[dict[str, Any]]
