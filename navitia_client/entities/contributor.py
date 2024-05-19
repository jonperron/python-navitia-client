from dataclasses import dataclass
from typing import Any, Optional

from navitia_client.entities.base_entity import BaseEntity


@dataclass
class Contributor(BaseEntity):
    license: str
    website: Optional[str]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Contributor":
        return cls(
            id=payload["id"],
            name=payload["name"],
            license=payload["license"],
            website=payload["website"],
        )
