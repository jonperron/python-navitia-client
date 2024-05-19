from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional, Sequence

from navitia_client.entities.base_entity import BaseEntity
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.stop_area import StopPoint
from navitia_client.entities.trip import Trip


@dataclass
class ActivePeriod:
    begin: datetime
    end: datetime

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "ActivePeriod":
        return cls(
            begin=datetime.strptime(payload["begin"], "%Y%m%d"),
            end=datetime.strptime(payload["end"], "%Y%m%d"),
        )


@dataclass
class WeekPattern:
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "WeekPattern":
        return cls(
            monday=bool(payload["monday"]),
            tuesday=bool(payload["tuesday"]),
            wednesday=bool(payload["wednesday"]),
            thursday=bool(payload["thursday"]),
            friday=bool(payload["friday"]),
            saturday=bool(payload["saturday"]),
            sunday=bool(payload["sunday"]),
        )


@dataclass
class Calendar:
    active_periods: Sequence[ActivePeriod]
    week_pattern: WeekPattern

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Calendar":
        return cls(
            active_periods=[
                ActivePeriod.from_payload(data) for data in payload["active_periods"]
            ],
            week_pattern=WeekPattern.from_payload(payload["week_pattern"]),
        )


@dataclass
class Code:
    type: str
    value: str

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Code":
        return cls(
            type=payload["type"],
            value=payload["value"],
        )


@dataclass
class JourneyPattern(BaseEntity):
    pass

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "JourneyPattern":
        return cls(
            id=payload["id"],
            name=payload["name"],
        )


@dataclass
class StopTime:
    arrival_time: int
    departure_time: int
    drop_off_allowed: bool
    headsign: int
    pickup_allowed: bool
    skipped_stop: bool
    stop_point: StopPoint
    utc_arrival_time: int
    utc_departure_time: int

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "StopTime":
        return cls(
            arrival_time=payload["arrival_time"],
            departure_time=payload["departure_time"],
            drop_off_allowed=bool(payload["drop_off_allowed"]),
            headsign=payload["headsign"],
            pickup_allowed=bool(payload["pickup_allowed"]),
            skipped_stop=bool(payload["skipped_stop"]),
            stop_point=StopPoint.from_payload(payload["stop_point"]),
            utc_arrival_time=payload["utc_arrival_time"],
            utc_departure_time=payload["utc_departure_time"],
        )


@dataclass
class ValidityPattern:
    beginning_date: datetime
    days: str

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "ValidityPattern":
        return cls(
            beginning_date=datetime.strptime(payload["beginning_date"], "%Y%m%d"),
            days=payload["days"],
        )


@dataclass
class VehicleJourney:
    id: str
    name: Optional[str]
    calendars: Optional[Sequence[Calendar]]
    codes: Sequence[Code]
    disruptions: Sequence[Disruption]
    headsign: str
    journey_pattern: Optional[JourneyPattern]
    stop_times: Optional[Sequence[StopTime]]
    trip: Optional[Trip]
    validity_pattern: Optional[ValidityPattern]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "VehicleJourney":
        return cls(
            id=payload["id"],
            name=payload.get("name"),
            calendars=[Calendar.from_payload(data) for data in payload["calendars"]]
            if "calendars" in payload
            else None,
            codes=[Code.from_payload(data) for data in payload["codes"]],
            disruptions=[
                Disruption.from_payload(data) for data in payload["disruptions"]
            ],
            headsign=payload["headsign"],
            journey_pattern=JourneyPattern.from_payload(payload["journey_pattern"])
            if "journey_pattern" in payload
            else None,
            stop_times=[StopTime.from_payload(data) for data in payload["stop_times"]]
            if "stop_times" in payload
            else None,
            trip=Trip.from_payload(payload["trip"]) if "trip" in payload else None,
            validity_pattern=ValidityPattern.from_payload(payload["validity_pattern"])
            if "validity_pattern" in payload
            else None,
        )
