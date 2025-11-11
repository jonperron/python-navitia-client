from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Sequence

from .base_entity import BaseEntity


class PhysicalModeId(Enum):
    AIR = "physical_mode:Air"
    BOAT = "physical_mode:Boat"
    BUS = "physical_mode:Bus"
    BUS_RAPID_TRANSIT = "physical_mode:BusRapidTransit"
    COACH = "physical_mode:Coach"
    FERRY = "physical_mode:Ferry"
    FUNICULAR = "physical_mode:Funicular"
    LOCAL_TRAIN = "physical_mode:LocalTrain"
    LONG_DISTANCE_TRAIN = "physical_mode:LongDistanceTrain"
    METRO = "physical_mode:Metro"
    RAIL_SHUTTLE = "physical_mode:RailShuttle"
    RAPID_TRANSIT = "physical_mode:RapidTransit"
    SHUTTLE = "physical_mode:Shuttle"
    SUSPENDED_CAR_CABLE = "physical_mode:SuspendedCableCar"
    TAXI = "physical_mode:Taxi"
    TRAIN = "physical_mode:Train"
    TRAMWAY = "physical_mode:Tramway"


@dataclass
class CommercialMode(BaseEntity):
    physical_modes: Optional[Sequence["PhysicalMode"]]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "CommercialMode":
        physical_modes = (
            [
                PhysicalMode.from_payload(physical_mode)
                for physical_mode in payload["physical_modes"]
            ]
            if "physical_modes" in payload
            else None
        )

        return cls(
            id=payload["id"],
            name=payload["name"],
            physical_modes=physical_modes,
        )


@dataclass
class CO2EmissionRate(BaseEntity):
    pass

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "CO2EmissionRate":
        return cls(
            id=payload["id"],
            name=payload["name"],
        )


@dataclass
class PhysicalMode:
    id: PhysicalModeId
    name: str
    co2_emission_rate: Optional[CO2EmissionRate]
    commercial_modes: Optional[Sequence[CommercialMode]]

    @classmethod
    def from_payload(
        cls,
        payload: dict[str, Any],
    ) -> "PhysicalMode":
        co2_emission_rate = (
            payload["co2_emission_rate"] if "co2_emission_rate" in payload else None
        )

        commercial_modes = (
            [
                CommercialMode.from_payload(commercial_mode)
                for commercial_mode in payload["commercial_modes"]
            ]
            if "commercial_modes" in payload
            else None
        )

        return cls(
            id=payload["id"],
            name=payload["name"],
            co2_emission_rate=co2_emission_rate,
            commercial_modes=commercial_modes,
        )
