from dataclasses import dataclass
from typing import Any, Sequence


@dataclass
class PathItem:
    length: int
    name: str
    duration: int
    direction: int

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "PathItem":
        return cls(
            length=payload["length"],
            name=payload["name"],
            duration=payload["duration"],
            direction=payload["direction"],
        )


@dataclass
class Path:
    segments: Sequence[PathItem]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Path":
        return cls(
            segments=[PathItem.from_payload(data) for data in payload["path_items"]]
        )
