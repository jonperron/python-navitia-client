from dataclasses import dataclass
from typing import Any

from .base_entity import BaseEntity


@dataclass
class Trip(BaseEntity):
    pass

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "Trip":
        return Trip(id=payload["id"], name=payload["name"])
