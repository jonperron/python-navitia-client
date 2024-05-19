from dataclasses import dataclass
from typing import Any, Sequence

from navitia_client.entities.network import Network
from navitia_client.entities.vehicle_journey import VehicleJourney


@dataclass
class TrafficReport:
    network: Network
    vehicle_journeys: Sequence[VehicleJourney]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "TrafficReport":
        return cls(
            network=Network.from_payload(payload["network"]),
            vehicle_journeys=[
                VehicleJourney.from_payload(data)
                for data in payload["vehicle_journeys"]
            ],
        )
