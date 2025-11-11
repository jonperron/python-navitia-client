from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class PublicTransportObjectRequest(BaseEntityRequest):
    """
    Request class for Public Transport Object queries.

    Attributes
    ----------
    query : str
        The search query string for public transport objects.
    type : Sequence[str], optional
        The types of objects to search for (default is ["network", "commercial_mode", "line", "route", "stop_area"]).
    disable_disruption : bool, optional
        Whether to disable disruption information (default is False).
    depth : int, optional
        The depth of data to retrieve (default is 1).
    post_query_filter : Optional[str], optional
        Additional filtering criteria (default is None).
    """

    query: str
    type: Sequence[str] = ("network", "commercial_mode", "line", "route", "stop_area")
    disable_disruption: bool = False
    depth: int = 1
    post_query_filter: Optional[str] = None

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the PublicTransportObjectRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters = {
            "q": self.query,
            "type": self.type,
            "depth": self.depth,
        }

        if self.disable_disruption:
            filters["disable_disruption"] = self.disable_disruption
        if self.post_query_filter:
            filters["filter"] = self.post_query_filter

        return filters
