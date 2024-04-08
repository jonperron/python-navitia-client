from dataclasses import dataclass
from typing import Any

from .base_entity import BaseEntity


@dataclass
class Company(BaseEntity):
    pass

    @staticmethod
    def from_json(payload: Any) -> "Company":
        return Company(
            id=payload.get("id"),
            name=payload.get("name"),
        )
