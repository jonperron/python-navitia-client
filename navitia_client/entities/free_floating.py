from dataclasses import dataclass
from typing import Dict, Any, Optional

from .coord import Coord


@dataclass
class FreeFloating:
    """
    Represents a free-floating shared mobility vehicle (bike, scooter, car, etc.).

    Attributes:
        public_id: Public identifier of the vehicle
        provider_name: Name of the service provider
        id: Identifier of the vehicle
        type: Type of vehicle (bike, scooter, car, etc.)
        propulsion: Type of propulsion (electric, human, etc.)
        battery: Battery level in percentage (0-100)
        distance: Distance from the search point in meters
        deeplink: Deep link URL to the provider's app
        coord: Coordinates of the vehicle
    """

    public_id: str
    provider_name: str
    id: str
    type: str
    propulsion: Optional[str] = None
    battery: Optional[int] = None
    distance: Optional[int] = None
    deeplink: Optional[str] = None
    coord: Optional[Coord] = None

    @classmethod
    def from_payload(cls, data: Dict[str, Any]) -> "FreeFloating":
        """
        Create a FreeFloating instance from API payload data.

        Parameters:
            data: Dictionary containing free floating data from the API

        Returns:
            FreeFloating: An instance of FreeFloating
        """
        coord = None
        if "coord" in data:
            coord = Coord.from_payload(data["coord"])

        return cls(
            public_id=data.get("public_id", ""),
            provider_name=data.get("provider_name", ""),
            id=data.get("id", ""),
            type=data.get("type", ""),
            propulsion=data.get("propulsion"),
            battery=data.get("battery"),
            distance=data.get("distance"),
            deeplink=data.get("deeplink"),
            coord=coord,
        )
