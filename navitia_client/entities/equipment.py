from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .base_entity import BaseEntity
from .stop_area import StopArea


class Equipment(Enum):
    WHEELCHAIR_ACCESSIBILITY = "has_wheelchair_accessibility"
    BIKE_ACCEPTED = "has_bike_accepted"
    AIR_CONDITIONED = "has_air_conditioned"
    VISUAL_ANNOUNCEMENT = "has_visual_announcement"
    AUDIBLE_ANNOUNCEMENT = "has_audible_announcement"
    APPROPRIATE_ESCORT = "has_appropriate_escort"
    APPROPRIATE_SIGNAGE = "has_appropriate_signage"
    SCHOOL_VEHICLE = "has_school_vehicle"
    WHEELCHAR_BOARDING = "has_wheelchair_boarding"
    SHELTERED = "has_sheltered"
    ELEVATOR = "has_elevator"
    ESCALATOR = "has_escalator"
    BIKE_DEPOT = "has_bike_depot"


@dataclass
class EquipmentAvailability:
    status: str
    cause: Optional[str]
    effect: Optional[str]
    periods: Optional[dict[str, str]]


@dataclass
class EquipmentDetails(BaseEntity):
    current_availability: EquipmentAvailability
    embedded_type: str


@dataclass
class StopAreaEquipments:
    equiment_details: EquipmentDetails
    stop_area: StopArea
