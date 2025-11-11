from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseEntityRequest(ABC):
    """
    Base class for entity requests.

    count : int, optional
        Maximum number of results (default is 10).
    start_page : int, optional
        The page number to start from (default is 0).

    """

    count: int = 10
    start_page: int = 0

    @abstractmethod
    def to_filters(self) -> Dict[str, Any]:
        pass


class BasePTEntityRequest(BaseEntityRequest):
    """
    Base class for public transport entity requests.
    Inherits from BaseEntityRequest.
        depth : int, optional
            Search depth (default is 1).
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Line headsign.
        since : Optional[str], optional
            To be used only on "vehicle_journeys" and "disruptions" collection, to filter on a period.
        until : Optional[str], optional
           To be used only on "vehicle_journeys" and "disruptions" collection, to filter on a period.

    """

    depth: int = 1
    odt: str = "all"
    distance: int = 200
    headsign: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    disable_geojson: bool = False
    disable_disruption: bool = False
