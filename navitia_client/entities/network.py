from dataclasses import dataclass
from typing import Any

from .base_entity import BaseEntity


@dataclass
class Network(BaseEntity):
    pass

    @staticmethod
    def from_json(payload: Any) -> "Network":
        return Network(
            id=payload.get("id"),
            name=payload.get("name"),
        )
