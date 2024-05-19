from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional, Sequence

from navitia_client.entities.link import Link


@dataclass
class PTDatetime:
    additional_informations: Sequence[str]
    departure_date_time: Optional[datetime]
    arrival_date_time: Optional[datetime]
    links: Sequence[Link]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "PTDatetime":
        return cls(
            additional_informations=[
                additional_information
                for additional_information in payload["additional_informations"]
            ],
            departure_date_time=datetime.strptime(
                payload["departure_date_time"], "%Y%m%d"
            )
            if "departure_date_time" in payload
            else None,
            arrival_date_time=datetime.strptime(payload["arrival_date_time"], "%Y%m%d")
            if "arrival_date_time" in payload
            else None,
            links=[Link.from_payload(link) for link in payload["links"]],
        )
