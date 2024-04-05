from dataclasses import dataclass
from enum import Enum
from typing import Sequence

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
    physical_mode: Sequence["PhysicalMode"]


@dataclass
class PhysicalMode:
    id: PhysicalModeId
    name: str
    commercial_modes: Sequence[CommercialMode]
