from dataclasses import dataclass
from typing import Any
from navitia_client.entities.base_entity import BaseEntity
from navitia_client.entities.stop_area import StopArea


@dataclass
class Direction(BaseEntity):
    embedded_type: str
    quality: int
    stop_area: StopArea

    @classmethod
    def from_payload(
        cls,
        payload: dict[str, Any],
    ) -> "Direction":
        return cls(
            id=payload["id"],
            name=payload["name"],
            embedded_type=payload["embedded_type"],
            quality=payload["quality"],
            stop_area=StopArea.from_payload(payload["stop_area"]),
        )
