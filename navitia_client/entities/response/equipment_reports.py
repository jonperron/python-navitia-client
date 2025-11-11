from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from .line_and_route import Line
from .equipment import StopAreaEquipments


@dataclass
class EquipmentReports:
    line: Optional[Line] = None
    stop_area_equipments: List[StopAreaEquipments] = field(default_factory=list)

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "EquipmentReports":
        """
        Create an EquipmentReports instance from API payload data.

        Parameters:
            data: Dictionary containing equipment report data from the API

        Returns:
            EquipmentReports: An instance of EquipmentReports
        """
        line = Line.from_payload(data["line"]) if "line" in data else None
        stop_area_equipments = [
            StopAreaEquipments.from_payload(item)
            for item in data.get("stop_area_equipments", [])
        ]

        return cls(line=line, stop_area_equipments=stop_area_equipments)
