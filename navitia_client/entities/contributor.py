from dataclasses import dataclass
from typing import Any, Optional

from navitia_client.entities.base_entity import BaseEntity


@dataclass
class Contributor(BaseEntity):
    license: str
    website: Optional[str]

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "Contributor":
        return Contributor(
            id=payload["id"],
            name=payload["name"],
            license=payload["license"],
            website=payload["website"],
        )
