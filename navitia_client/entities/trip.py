from dataclasses import dataclass
from typing import Any

from .base_entity import BaseEntity


@dataclass
class Trip(BaseEntity):
    pass

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Trip":
        return cls(id=payload["id"], name=payload["name"])
