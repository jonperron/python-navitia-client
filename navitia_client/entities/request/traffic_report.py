from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class TrafficReportRequest(BaseEntityRequest):
    """
    Request class for Traffic Report queries.

    Attributes
    ----------
    since : Optional[datetime], optional
        The start datetime for the reports (default is None).
    until : Optional[datetime], optional
        The end datetime for the reports (default is None).
    depth : int, optional
        The depth of data to retrieve (default is 1).
    forbidden_uris : Optional[Sequence[str]], optional
        Forbidden URIs (default is None).
    disable_geojson : bool, optional
        Whether to disable GeoJSON in the response (default is False).
    """

    since: Optional[datetime] = None
    until: Optional[datetime] = None
    depth: int = 1
    forbidden_uris: Optional[Sequence[str]] = None
    disable_geojson: bool = False

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the TrafficReportRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters: Dict[str, Any] = {
            "count": self.count,
            "depth": self.depth,
        }

        if self.disable_geojson:
            filters["disable_geojson"] = self.disable_geojson
        if self.forbidden_uris:
            filters["forbidden_uris[]"] = self.forbidden_uris
        if self.since:
            filters["since"] = self.since.isoformat()
        if self.until:
            filters["until"] = self.until.isoformat()

        return filters
