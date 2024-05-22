from dataclasses import dataclass
from typing import Any, Optional, Sequence
from navitia_client.entities.base_entity import BaseEntity
from navitia_client.entities.link import Link


@dataclass
class Cost:
    value: str
    currency: Optional[str]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Cost":
        return cls(
            value=payload["value"],
            currency=payload.get("currencty"),
        )


@dataclass
class Fare:
    total: Cost
    found: bool
    links: Sequence[Link]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Fare":
        return cls(
            total=Cost.from_payload(payload["total"]),
            found=bool(payload["found"]),
            links=[Link.from_payload(data) for data in payload["links"]],
        )


@dataclass
class Ticket(BaseEntity):
    found: bool
    cost: Cost
    links: Sequence[Link]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Ticket":
        return cls(
            id=payload["id"],
            name=payload["name"],
            found=bool(payload["found"]),
            cost=Cost.from_payload(payload["cost"]),
            links=[Link.from_payload(data) for data in payload["links"]],
        )
