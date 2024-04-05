from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Sequence

from .pt_object import PtObject
from .line_and_route import Route
from .stop_area import StopPoint


class DisruptionStatus(Enum):
    PAST = "past"
    ACTIVE = "active"
    FUTURE = "future"


class Effect(Enum):
    NO_SERVICE = "no_service"
    REDUCED_SERVICE = "reduced_service"
    SIGNIFICANT_DELAYS = "significant_delays"
    DETOUR = "detour"
    ADDITIONAL_SERVICE = "additional_service"
    MODIFIED_SERVICE = "modified_service"
    OTHER_EFFECT = "other_effect"
    UNKNOWN_EFFECT = "unknown_effect"
    STOP_MOVED = "stop_moved"
    NO_EFFECT = "no_effect"
    ACCESSIBILITY_ISSUE = "accessibility_issue"


@dataclass
class Severity:
    color: str
    priority: int | None
    name: str
    effect: Effect


@dataclass
class DisruptionPeriod:
    begin: datetime
    end: datetime


@dataclass
class Channel:
    id: str
    content_type: str
    name: str


@dataclass
class DisruptionMessage:
    text: str
    channel: Channel


@dataclass
class ImpactedSection:
    section_from: PtObject
    section_to: PtObject
    routes: Route


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
    base_departure_time: str
    base_arrival_time: str
    cause: str
    stop_time_effect: StopTimeEffect  # written as deprecated in the doc
    arrival_status: StopTimeEffect
    departure_status: StopTimeEffect


@dataclass
class ImpactedObject:
    pt_object: PtObject
    impacted_section: ImpactedSection
    impacted_stops: Sequence[ImpactedStop]


@dataclass
class Disruption:
    id: str
    status: DisruptionStatus
    disruption_id: str
    impact_id: str
    severity: Severity
    application_periods: Sequence[DisruptionPeriod]
    messages: Sequence[DisruptionMessage]
    updated_at: datetime
    impacted_objects: Sequence[ImpactedObject]
    cause: str
    category: str
    contributor: str
