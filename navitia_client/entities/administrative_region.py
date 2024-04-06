from dataclasses import dataclass
from datetime import datetime
from typing import Optional
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


@dataclass
class AdministrativeRegion(BaseEntity):
    label: str
    coord: Coord
    level: int
    zip_code: str
