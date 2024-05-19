from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Sequence

from navitia_client.entities.display_information import DisplayInformation
from navitia_client.entities.line_and_route import Route
from navitia_client.entities.pt_datetime import PTDatetime
from navitia_client.entities.stop_area import StopPoint


@dataclass
class AdditionalInformationEnum(Enum):
    DATE_OUT_OF_BOUNDS = "date_out_of_bounds"
    NO_DEPARTURE_THIS_DAY = "no_departure_this_day"
    NO_ACTIVE_CIRCULATION_THIS_DAY = "no_active_circulation_this_day"
    TERMINUS = "terminus"
    PARTIAL_TERMINUS = "partial_terminus"
    ACTIVE_DISRUPTION = "active_disruption"


@dataclass
class StopSchedule:
    display_informations: DisplayInformation
    route: Route
    date_times: Sequence[PTDatetime]
    stop_point: StopPoint
    additional_informations: Optional[AdditionalInformationEnum]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "StopSchedule":
        return cls(
            display_informations=DisplayInformation.from_payload(
                payload["display_informations"]
            ),
            route=Route.from_payload(payload["route"]),
            date_times=[
                PTDatetime.from_payload(data) for data in payload["date_times"]
            ],
            stop_point=StopPoint.from_payload(payload["stop_point"]),
            additional_informations=AdditionalInformationEnum(
                payload["additional_informations"]
            )
            if payload["additional_informations"]
            else None,
        )


@dataclass
class TerminusSchedule(StopSchedule):
    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "TerminusSchedule":
        stop_schedule = super(TerminusSchedule, cls).from_payload(payload)
        return cls(
            display_informations=stop_schedule.display_informations,
            route=stop_schedule.route,
            date_times=stop_schedule.date_times,
            stop_point=stop_schedule.stop_point,
            additional_informations=stop_schedule.additional_informations,
        )
