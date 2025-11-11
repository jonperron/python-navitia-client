from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class EquipmentReportRequest(BaseEntityRequest):
    """
    Request class for Equipment Report queries.

    Attributes
    ----------
    depth : int, optional
        Json response depth (default is 1).
    filter : Optional[str], optional
        A filter to refine your request (default is None).
    forbidden_uris : Optional[Sequence[str]], optional
        If you want to avoid lines, modes, networks, etc (default is None).
    """

    depth: int = 1
    filter: Optional[str] = None
    forbidden_uris: Optional[Sequence[str]] = None

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the EquipmentReportRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters: Dict[str, Any] = {
            "count": self.count,
            "depth": self.depth,
            "start_page": self.start_page,
        }

        if self.filter:
            filters["filter"] = self.filter
        if self.forbidden_uris:
            filters["forbidden_uris[]"] = self.forbidden_uris

        return filters
