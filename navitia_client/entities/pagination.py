from dataclasses import dataclass
from typing import Any


@dataclass
class Pagination:
    items_on_page: int
    total_result: int
    items_per_page: int = 25
    start_page: int = 0

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Pagination":
        return cls(
            items_on_page=payload["items_on_page"],
            items_per_page=payload["items_per_page"],
            start_page=payload["start_page"],
            total_result=payload["total_result"],
        )
