from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class LineReportRequest(BaseEntityRequest):
    """
    Request class for Line Report queries.

    Attributes
    ----------
    since : Optional[datetime], optional
        Filter line reports since this date and time (default is None).
    until : Optional[datetime], optional
        Filter line reports until this date and time (default is None).
    depth : int, optional
        The depth of the query (default is 1).
    forbidden_uris : Optional[Sequence[str]], optional
        List of URIs to forbid (default is None).
    disable_geojson : bool, optional
        Whether to disable GeoJSON output (default is False).
    """

    since: Optional[datetime] = None
    until: Optional[datetime] = None
    depth: int = 1
    forbidden_uris: Optional[Sequence[str]] = None
    disable_geojson: bool = False

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the LineReportRequest instance into a dictionary of filters.

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
