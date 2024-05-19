from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from navitia_client.entities.contributor import Contributor


@dataclass
class Dataset:
    contributor: Contributor
    description: Optional[str]
    end_validation_date: datetime
    id: str
    realtime_level: str
    start_validation_date: datetime
    system: Optional[str]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Dataset":
        return cls(
            contributor=Contributor.from_payload(payload["contributor"]),
            description=payload["description"],
            end_validation_date=datetime.strptime(
                payload["end_validation_date"], "%Y%m%dT%H%M%S"
            ),
            id=payload["id"],
            realtime_level=payload["realtime_level"],
            start_validation_date=datetime.strptime(
                payload["start_validation_date"], "%Y%m%dT%H%M%S"
            ),
            system=payload["system"],
        )
