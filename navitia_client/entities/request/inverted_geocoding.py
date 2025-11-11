from dataclasses import dataclass
from typing import Dict, Any

from .base_entity_request import BaseEntityRequest


@dataclass
class InvertedGeocodingRequest(BaseEntityRequest):
    """
    Request class for Inverted Geocoding queries.

    Note: Inverted Geocoding API doesn't accept any additional filters beyond base parameters.
    This class inherits count and start_page from BaseEntityRequest.
    """

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the InvertedGeocodingRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters = {
            "count": self.count,
        }

        return filters
