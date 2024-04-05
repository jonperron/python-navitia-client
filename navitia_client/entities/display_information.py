from dataclasses import dataclass
from typing import Optional, Sequence

from .equipment import Equiment
from .network import Network
from .physical_mode import CommercialMode, PhysicalMode


@dataclass
class DisplayInformation:
    network: Network
    physical_mode: PhysicalMode
    commercial_mode: CommercialMode
    code: str
    color: str
    text_color: str
    direction: str
    headsign: str
    label: str
    name: str
    trip_short_name: str
    equipments: Sequence[Equiment]
    description: Optional[str]
