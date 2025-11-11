from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class DepartureRequest(BaseEntityRequest):
    """
    Request class for Departure entities.

    Attributes
    ----------
    from_datetime : datetime, optional
        The starting datetime for fetching departures (default is current datetime).
    duration : int, optional
        The duration in seconds for which to fetch departures (default is 86400 seconds).
    depth : int, optional
        The depth of the search (default is 1).
    count : int, optional
        Maximum number of results (default is 10, inherited from BaseEntityRequest).
    start_page : int, optional
        The page number to start from (default is 0, inherited from BaseEntityRequest).
    forbidden_uris : Optional[Sequence[str]], optional
        A list of URIs to exclude from the search (default is None).
    data_freshness : str, optional
        The freshness of the data to fetch, either "realtime" or "base_schedule" (default is "realtime").
    disable_geojson : bool, optional
        Whether to disable geoJSON in the response (default is False).
    direction_type : str, optional
        The direction type of the departures to fetch, e.g., "all", "forward", "backward" (default is "all").
    """

    from_datetime: datetime = field(default_factory=datetime.now)
    duration: int = 86400
    depth: int = 1
    forbidden_uris: Optional[Sequence[str]] = None
    data_freshness: str = "realtime"
    disable_geojson: bool = False
    direction_type: str = "all"

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the DepartureRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters = {
            "from_datetime": self.from_datetime,
            "duration": self.duration,
            "depth": self.depth,
            "count": self.count,
            "start_page": self.start_page,
            "data_freshness": self.data_freshness,
            "direction_type": self.direction_type,
        }

        if self.disable_geojson:
            filters["disable_geojson"] = self.disable_geojson
        if self.forbidden_uris:
            filters["forbidden_uris[]"] = self.forbidden_uris

        return filters
