from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
from .base_entity import BaseEntity
from .coord import Coord


@dataclass
class Region(BaseEntity):
    dataset_created_at: Optional[datetime]
    end_production_date: Optional[datetime]
    last_load_at: Optional[datetime]
    shape: Optional[str]
    start_production_date: Optional[datetime]
    status: Optional[str]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Region":
        return cls(
            id=payload["id"],
            name=payload["name"],
            dataset_created_at=datetime.fromisoformat(payload["dataset_created_at"])
            if "dataset_created_at" in payload
            else None,
            end_production_date=datetime.strptime(
                payload["end_production_date"], "%Y%m%d"
            )
            if "end_production_date" in payload
            else None,
            last_load_at=datetime.fromisoformat(payload["last_load_at"])
            if "last_load_at" in payload
            else None,
            shape=payload["shape"],
            start_production_date=datetime.strptime(
                payload["start_production_date"], "%Y%m%d"
            )
            if "end_production_date" in payload
            else None,
            status=payload["status"],
        )


@dataclass
class AdministrativeRegion(BaseEntity):
    label: str
    coord: Coord
    level: int
    zip_code: str

    @staticmethod
    def from_payload(payload: dict[str, Any]) -> "AdministrativeRegion":
        return AdministrativeRegion(
            id=payload["id"],
            name=payload["name"],
            label=payload["label"],
            coord=Coord.from_payload(payload["coord"]),
            level=payload["level"],
            zip_code=payload["zip_code"],
        )
