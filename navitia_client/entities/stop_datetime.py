from dataclasses import dataclass
from datetime import datetime
from typing import Any, Sequence

from navitia_client.entities.link import Link


@dataclass
class StopDateTime:
    additional_informations: Sequence[str]
    arrival_date_time: datetime
    base_arrival_date_time: datetime
    base_departure_date_time: datetime
    data_freshness: str
    departure_date_time: datetime
    links: Sequence[Link]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "StopDateTime":
        return cls(
            additional_informations=[
                additional_information
                for additional_information in payload["additional_informations"]
            ],
            arrival_date_time=datetime.strptime(
                payload["arrival_date_time"], "%Y%m%dT%H%M%S"
            ),
            base_arrival_date_time=datetime.strptime(
                payload["base_arrival_date_time"], "%Y%m%dT%H%M%S"
            ),
            base_departure_date_time=datetime.strptime(
                payload["base_departure_date_time"], "%Y%m%dT%H%M%S"
            ),
            data_freshness=payload["data_freshness"],
            departure_date_time=datetime.strptime(
                payload["departure_date_time"], "%Y%m%dT%H%M%S"
            ),
            links=[Link.from_payload(link) for link in payload["links"]],
        )
