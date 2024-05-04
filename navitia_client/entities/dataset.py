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

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "Dataset":
        return Dataset(
            contributor=Contributor.from_json(payload["contributor"]),
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
