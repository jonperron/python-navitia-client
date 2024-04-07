from dataclasses import dataclass
from typing import Optional

from navitia_client.entities.base_entity import BaseEntity


@dataclass
class Contributor(BaseEntity):
    license: str
    website: Optional[str]
