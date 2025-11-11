from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict, Any

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
class Label:
    label: str

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "Label":
        return cls(label=data.get("label", ""))


@dataclass
class Period:
    begin: str
    end: str

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "Period":
        return cls(begin=data.get("begin", ""), end=data.get("end", ""))


@dataclass
class EquipmentAvailability:
    status: str
    cause: Optional[Label] = None
    effect: Optional[Label] = None
    periods: Optional[List[Period]] = None
    updated_at: Optional[str] = None

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "EquipmentAvailability":
        cause = Label.from_payload(data["cause"]) if "cause" in data else None
        effect = Label.from_payload(data["effect"]) if "effect" in data else None
        periods = [Period.from_payload(p) for p in data.get("periods", [])]

        return cls(
            status=data.get("status", "unknown"),
            cause=cause,
            effect=effect,
            periods=periods if periods else None,
            updated_at=data.get("updated_at"),
        )


@dataclass
class EquipmentDetails(BaseEntity):
    embedded_type: str
    current_availability: Optional[EquipmentAvailability] = None

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "EquipmentDetails":
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            embedded_type=data.get("embedded_type", ""),
            current_availability=EquipmentAvailability.from_payload(
                data["current_availability"]
            )
            if "current_availability" in data
            else None,
        )


@dataclass
class StopAreaEquipments:
    equipment_details: List[EquipmentDetails]
    stop_area: Optional[StopArea] = None

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "StopAreaEquipments":
        equipment_details = [
            EquipmentDetails.from_payload(item)
            for item in data.get("equipment_details", [])
        ]
        stop_area = (
            StopArea.from_payload(data["stop_area"]) if "stop_area" in data else None
        )

        return cls(equipment_details=equipment_details, stop_area=stop_area)
