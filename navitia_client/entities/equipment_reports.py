from dataclasses import dataclass

from .line import Line
from .equipment import StopAreaEquipments


@dataclass
class EquipmentReports:
    line: Line
    stop_area_equipments: StopAreaEquipments
