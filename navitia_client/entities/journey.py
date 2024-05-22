from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Optional, Sequence

from navitia_client.entities.display_information import DisplayInformation
from navitia_client.entities.link import Link
from navitia_client.entities.path import Path
from navitia_client.entities.place import Place
from navitia_client.entities.ticket import Fare


class SectionType(Enum):
    PUBLIC_TRANSPORT = "public_transport"
    STREET_NETWORK = "street_network"
    WAITING = "waiting"
    STAY_IN = "stay_in"
    TRANSFER = "transfer"
    CROW_FLY = "crow_fly"
    ON_DEMAND_TRANSPORT = "on_demand_demand_transport"
    BSS_RENT = "bss_rent"
    BSS_PUT_BACK = "bss_put_back"
    BOARDING = "boarding"
    ALIGHTING = "alighting"
    PARK = "park"
    RIDESHARING = "ride_sharing"


class SectionAdditionalInformation(Enum):
    REGULAR = "regular"
    HAS_DATE_TIME_ESTIMATED = "has_date_time_estimated"
    ODT_WITH_STOP_TIME = "odt_with_stop_time"
    ODT_WITH_STOP_POINT = "odt_with_stop_point"
    ODT_WITH_ZONE = "odt_with_zone"


class SectionTransferType(Enum):
    WALKING = "walking"
    STAY_IN = "stay_in"


@dataclass
class Section:
    type: SectionType
    id: str
    mode: Optional[str]
    duration: int
    from_: Optional[Place]
    to: Optional[Place]
    links: Sequence[Link]
    display_informations: Optional[DisplayInformation]
    additional_informations: Optional[SectionAdditionalInformation]
    geojson: Optional[Any]
    path: Optional[Sequence[Path]]
    transfer_type: Optional[SectionTransferType]
    departure_date_time: datetime
    arrival_date_time: datetime

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Section":
        return cls(
            type=SectionType(payload["type"]),
            id=payload["id"],
            mode=payload.get("mode"),
            duration=payload["duration"],
            from_=Place.from_payload(payload["from"]) if "from" in payload else None,
            to=Place.from_payload(payload["to"]) if "to" in payload else None,
            links=[Link.from_payload(data) for data in payload["links"]],
            display_informations=DisplayInformation.from_payload(
                payload["display_informations"]
            )
            if "display_informations" in payload
            else None,
            additional_informations=SectionAdditionalInformation(
                payload["additional_informations"][0]
            )
            if "additional_informations" in payload
            else None,
            geojson=payload.get("geojson"),
            path=[Path.from_payload(data) for data in payload["path"]]
            if "path" in payload
            else None,
            transfer_type=SectionTransferType(payload["transfer_type"])
            if "transfer_type" in payload
            else None,
            departure_date_time=datetime.strptime(
                payload["departure_date_time"], "%Y%m%dT%H%M%S"
            ),
            arrival_date_time=datetime.strptime(
                payload["arrival_date_time"], "%Y%m%dT%H%M%S"
            ),
        )


@dataclass
class Journey:
    duration: int
    nb_transfers: int
    departure_date_time: datetime
    requested_date_time: datetime
    arrival_date_time: datetime
    sections: Sequence[Section]
    from_: Optional[Place]
    to_: Optional[Place]
    links: Sequence[Link]
    type: str
    fare: Fare
    tags: Sequence[str]
    status: str

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Journey":
        return cls(
            duration=payload["duration"],
            nb_transfers=payload["nb_transfers"],
            departure_date_time=datetime.strptime(
                payload["departure_date_time"], "%Y%m%dT%H%M%S"
            ),
            requested_date_time=datetime.strptime(
                payload["requested_date_time"], "%Y%m%dT%H%M%S"
            ),
            arrival_date_time=datetime.strptime(
                payload["arrival_date_time"], "%Y%m%dT%H%M%S"
            ),
            sections=[Section.from_payload(data) for data in payload["sections"]],
            from_=Place.from_payload(payload["from"]) if "from" in payload else None,
            to_=Place.from_payload(payload["to"]) if "to" in payload else None,
            links=[Link.from_payload(data) for data in payload["links"]],
            type=payload["type"],
            fare=Fare.from_payload(payload["fare"]),
            tags=[data for data in payload["tags"]],
            status=payload["status"],
        )
