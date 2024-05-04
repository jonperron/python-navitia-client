from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Optional, Sequence

from .pt_object import PtObject
from .line_and_route import Route
from .stop_area import StopPoint


class DisruptionStatus(Enum):
    PAST = "past"
    ACTIVE = "active"
    FUTURE = "future"


class Effect(Enum):
    NO_SERVICE = "NO_SERVICE"
    REDUCED_SERVICE = "REDUCED_SERVICE"
    SIGNIFICANT_DELAYS = "SIGNIFICANT_DELAYS"
    DETOUR = "DETOUR"
    ADDITIONAL_SERVICE = "ADDITIONAL_SERVICE"
    MODIFIED_SERVICE = "MODIFIED_SERVICE"
    OTHER_EFFECT = "OTHER_EFFECT"
    UNKNOWN_EFFECT = "UNKNOWN_EFFECT"
    STOP_MOVED = "STOP_MOVED"
    NO_EFFECT = "NO_EFFECT"
    ACCESSIBILITY_ISSUE = "ACCESSIBILITY_ISSUE"


@dataclass
class Severity:
    color: str
    priority: int | None
    name: str
    effect: Effect

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "Severity":
        return cls(
            color=payload["color"],
            priority=payload["priority"],
            name=payload["name"],
            effect=Effect(payload["effect"]),
        )


@dataclass
class DisruptionPeriod:
    begin: datetime
    end: datetime

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "DisruptionPeriod":
        return cls(
            begin=datetime.strptime(payload["begin"], "%Y%m%dT%H%M%S"),
            end=datetime.strptime(payload["end"], "%Y%m%dT%H%M%S"),
        )


@dataclass
class Channel:
    id: str
    content_type: str
    name: str

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "Channel":
        return cls(
            id=payload["id"], content_type=payload["content_type"], name=payload["name"]
        )


@dataclass
class DisruptionMessage:
    text: str
    channel: Channel

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "DisruptionMessage":
        return cls(text=payload["text"], channel=Channel.from_json(payload["channel"]))


@dataclass
class ImpactedSection:
    section_from: PtObject
    section_to: PtObject
    routes: Sequence[Route]

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "ImpactedSection":
        routes = [Route.from_json(route_data) for route_data in payload["routes"]]

        return cls(
            section_from=PtObject.from_json(payload["section_from"]),
            section_to=PtObject.from_json(payload["section_to"]),
            routes=routes,
        )


class StopTimeEffect(Enum):
    ADDED = "added"
    DELETED = "deleted"
    DELAYED = "delayed"
    UNCHANGED = "unchanged"


@dataclass
class ImpactedStop:
    stop_point: StopPoint
    amended_departure_time: str
    amended_arrival_time: str
    base_departure_time: Optional[str]
    base_arrival_time: Optional[str]
    cause: str
    stop_time_effect: StopTimeEffect  # written as deprecated in the doc
    arrival_status: StopTimeEffect
    departure_status: StopTimeEffect
    is_detour: bool

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "ImpactedStop":
        return cls(
            amended_arrival_time=payload["amended_arrival_time"],
            amended_departure_time=payload["amended_departure_time"],
            arrival_status=StopTimeEffect(payload["arrival_status"]),
            base_arrival_time=payload["base_arrival_time"]
            if "base_arrival_time" in payload
            else None,
            base_departure_time=payload["base_departure_time"]
            if "base_departure_time" in payload
            else None,
            cause=payload["cause"],
            departure_status=StopTimeEffect(payload["departure_status"]),
            is_detour=bool(payload["is_detour"]),
            stop_point=StopPoint.from_json(payload["stop_point"]),
            stop_time_effect=StopTimeEffect(payload["stop_time_effect"]),
        )


@dataclass
class ImpactedObject:
    pt_object: Optional[PtObject]
    impacted_section: Optional[ImpactedSection]
    impacted_stops: Optional[Sequence[ImpactedStop]]

    @classmethod
    def from_json(
        cls,
        payload: dict[str, Any],
    ) -> "ImpactedObject":
        impacted_stops = (
            [
                ImpactedStop.from_json(impacted_stop_data)
                for impacted_stop_data in payload["impacted_stops"]
            ]
            if "impacted_stops" in payload
            else None
        )
        return cls(
            pt_object=PtObject.from_json(payload["pt_object"])
            if "pt_object" in payload
            else None,
            impacted_section=ImpactedSection.from_json(payload["impacted_section"])
            if "impacted_section" in payload
            else None,
            impacted_stops=impacted_stops,
        )


@dataclass
class Disruption:
    id: str
    status: DisruptionStatus
    disruption_id: str
    impact_id: str
    severity: Severity
    application_periods: Sequence[DisruptionPeriod]
    messages: Optional[Sequence[DisruptionMessage]]
    updated_at: datetime
    impacted_objects: Sequence[ImpactedObject]
    cause: str
    category: Optional[str]
    contributor: str

    @classmethod
    def from_json(
        cls,
        payload: dict[str, Any],
    ) -> "Disruption":
        application_periods = [
            DisruptionPeriod.from_json(application_period)
            for application_period in payload["application_periods"]
        ]
        messages = (
            [DisruptionMessage.from_json(message) for message in payload["messages"]]
            if "messages" in payload
            else None
        )
        impacted_objects = [
            ImpactedObject.from_json(object) for object in payload["impacted_objects"]
        ]

        return cls(
            id=payload["id"],
            status=DisruptionStatus(payload["status"]),
            disruption_id=payload["disruption_id"],
            impact_id=payload["impact_id"],
            severity=Severity.from_json(payload["severity"]),
            application_periods=application_periods,
            messages=messages,
            updated_at=datetime.strptime(payload["updated_at"], "%Y%m%dT%H%M%S"),
            impacted_objects=impacted_objects,
            cause=payload["cause"],
            category=payload.get("category"),
            contributor=payload["contributor"],
        )
