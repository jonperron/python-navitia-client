from typing import Any, Optional, Collection, Type

from navitia_client.entities.line_and_route import Line, Route
from navitia_client.entities.network import Network
from navitia_client.entities.physical_mode import CommercialMode, PhysicalMode
from navitia_client.entities.vehicle_journey import VehicleJourney


class Link:
    lines: Optional[Collection[Line]] = None
    vehicle_journeys: Optional[Collection[VehicleJourney]] = None
    routes: Optional[Collection[Route]] = None
    commercial_modes: Optional[Collection[CommercialMode]] = None
    physical_modes: Optional[Collection[PhysicalMode]] = None
    networks: Optional[Collection[Network]] = None

    @staticmethod
    def _build_entity_list_from_payload(
        entity_class: Type, payload: list[dict[str, Any]]
    ) -> Collection[Any]:
        return [entity_class.from_payload(item) for item in payload]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "Link":
        entity_mapping = {
            "lines": Line,
            "vehicle_journeys": VehicleJourney,
            "routes": Route,
            "commercial_modes": CommercialMode,
            "physical_modes": PhysicalMode,
            "networks": Network,
        }

        obj = cls()

        for key, entity_class in entity_mapping.items():
            if key in payload:
                setattr(
                    obj,
                    key,
                    cls._build_entity_list_from_payload(entity_class, payload[key]),
                )

        return obj
