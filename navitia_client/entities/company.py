from dataclasses import dataclass
from typing import Any

from .base_entity import BaseEntity


@dataclass
class Company(BaseEntity):
    pass

    @classmethod
    def from_json(cls, payload: Any) -> "Company":
        return cls(
            id=payload.get("id"),
            name=payload.get("name"),
        )
