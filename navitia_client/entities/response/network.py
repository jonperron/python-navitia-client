from dataclasses import dataclass
from typing import Any

from .base_entity import BaseEntity


@dataclass
class Network(BaseEntity):
    pass

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Network":
        return cls(
            id=payload["id"],
            name=payload["name"],
        )
