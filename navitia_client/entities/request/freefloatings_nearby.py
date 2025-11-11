from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class FreefloatingsNearbyRequest(BaseEntityRequest):
    """
    Request class for Freefloatings Nearby queries.

    Attributes
    ----------
    distance : int, optional
        Search radius in meters (default is 500).
    type : Optional[Sequence[str]], optional
        The type of shared mobility vehicles to return (e.g., bike, scooter, car) (default is None).
    """

    distance: int = 500
    type: Optional[Sequence[str]] = None

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the FreefloatingsNearbyRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters: Dict[str, Any] = {
            "distance": self.distance,
            "count": self.count,
        }

        if self.type:
            filters["type[]"] = self.type

        return filters
