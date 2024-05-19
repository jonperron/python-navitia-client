from dataclasses import dataclass
from typing import Any, Sequence

from .base_entity import BaseEntity
from .coord import Coord
from .administrative_region import AdministrativeRegion


@dataclass
class Address(BaseEntity):
    label: str
    coord: Coord
    house_number: int
    administrative_regions: Sequence[AdministrativeRegion]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Address":
        return Address(
            id=payload["id"],
            name=payload["name"],
            label=payload["label"],
            coord=Coord.from_payload(payload["coord"]),
            house_number=payload["house_number"],
            administrative_regions=[
                AdministrativeRegion.from_payload(data)
                for data in payload["administrative_regions)"]
            ],
        )
