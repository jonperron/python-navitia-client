from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from navitia_client.entities.contributor import Contributor


@dataclass
class Dataset:
    contributor: Contributor
    description: Optional[str]
    end_validation_date: datetime
    id: str
    realtime_level: str
    start_validation_date: datetime
    system: Optional[str]
