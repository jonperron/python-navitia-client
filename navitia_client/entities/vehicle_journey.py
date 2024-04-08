from dataclasses import dataclass
from datetime import datetime
from typing import Any, Sequence

from navitia_client.entities.base_entity import BaseEntity
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.stop_area import StopPoint
from navitia_client.entities.trip import Trip


@dataclass
class ActivePeriod:
    begin: datetime
    end: datetime

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "ActivePeriod":
        return ActivePeriod(
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

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "WeekPattern":
        return WeekPattern(
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

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "Calendar":
        return Calendar(
            active_periods=[
                ActivePeriod.from_json(data) for data in payload["active_periods"]
            ],
            week_pattern=WeekPattern.from_json(payload["week_pattern"]),
        )


@dataclass
class Code:
    type: str
    value: str

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "Code":
        return Code(
            type=payload["type"],
            value=payload["value"],
        )


@dataclass
class JourneyPattern(BaseEntity):
    pass

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "JourneyPattern":
        return JourneyPattern(
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

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "StopTime":
        return StopTime(
            arrival_time=payload["arrival_time"],
            departure_time=payload["departure_time"],
            drop_off_allowed=bool(payload["drop_off_allowed"]),
            headsign=payload["headsign"],
            pickup_allowed=bool(payload["pickup_allowed"]),
            skipped_stop=bool(payload["skipped_stop"]),
            stop_point=StopPoint.from_json(payload["stop_point"]),
            utc_arrival_time=payload["utc_arrival_time"],
            utc_departure_time=payload["utc_departure_time"],
        )


@dataclass
class ValidityPattern:
    beginning_date: datetime
    days: str

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "ValidityPattern":
        return ValidityPattern(
            beginning_date=datetime.strptime(payload["beginning_date"], "%Y%m%d"),
            days=payload["days"],
        )


@dataclass
class VehicleJourney(BaseEntity):
    calendars: Sequence[Calendar]
    codes: Sequence[Code]
    disruptions: Sequence[Disruption]
    headsign: str
    journey_pattern: JourneyPattern
    stop_times: Sequence[StopTime]
    trip: Trip
    validity_pattern: ValidityPattern

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "VehicleJourney":
        return VehicleJourney(
            id=payload["id"],
            name=payload["name"],
            calendars=[Calendar.from_json(data) for data in payload["calendars"]],
            codes=[Code.from_json(data) for data in payload["codes"]],
            disruptions=[Disruption.from_json(data) for data in payload["disruptions"]],
            headsign=payload["headsign"],
            journey_pattern=JourneyPattern.from_json(payload["journey_pattern"]),
            stop_times=[StopTime.from_json(data) for data in payload["stop_times"]],
            trip=Trip.from_json(payload["trip"]),
            validity_pattern=ValidityPattern.from_json(payload["validity_pattern"]),
        )
