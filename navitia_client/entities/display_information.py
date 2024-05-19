from dataclasses import dataclass
from typing import Any, Optional, Sequence

from .equipment import Equipment


@dataclass
class DisplayInformation:
    network: str
    physical_mode: Optional[str]
    commercial_mode: Optional[str]
    code: str
    color: str
    text_color: str
    direction: str
    headsign: Optional[str]
    label: Optional[str]
    name: str
    trip_short_name: Optional[str]
    equipments: Optional[Sequence[Equipment]]
    description: Optional[str]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "DisplayInformation":
        return cls(
            network=payload["network"],
            physical_mode=payload.get("physical_mode"),
            commercial_mode=payload.get("commercial_mode"),
            code=payload["code"],
            color=payload["color"],
            text_color=payload["text_color"],
            direction=payload["direction"],
            headsign=payload.get("headsign"),
            label=payload.get("label"),
            name=payload["name"],
            trip_short_name=payload.get("trip_short_name"),
            equipments=[
                Equipment(equipment_data) for equipment_data in payload["equipments"]
            ]
            if payload.get("equipments")
            else None,
            description=payload.get("description"),
        )
