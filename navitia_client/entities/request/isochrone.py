from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class IsochroneRequest(BaseEntityRequest):
    """
    Request class for Isochrone queries.

    Attributes
    ----------
    from_ : str
        The starting point for the isochrone calculation (required).
    start_datetime : datetime, optional
        The starting date and time for the isochrone calculation (default is datetime.now()).
    boundary_duration : Sequence[int], optional
        List of durations in seconds defining the isochrones boundaries (default is empty list).
    to : Optional[str], optional
        The ending point for the isochrone calculation (default is None).
    first_section_mode : Optional[Sequence[str]], optional
        Modes of transportation for the first section of the journey (default is None).
    last_section_mode : Optional[Sequence[str]], optional
        Modes of transportation for the last section of the journey (default is None).
    min_duration : Optional[int], optional
        The minimum duration for the isochrone calculation (default is None).
    max_duration : Optional[int], optional
        The maximum duration for the isochrone calculation (default is None).
    """

    from_: str
    start_datetime: datetime = field(default_factory=datetime.now)
    boundary_duration: Sequence[int] = field(default_factory=list)
    to: Optional[str] = None
    first_section_mode: Optional[Sequence[str]] = None
    last_section_mode: Optional[Sequence[str]] = None
    min_duration: Optional[int] = None
    max_duration: Optional[int] = None

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the IsochroneRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters: Dict[str, Any] = {
            "datetime": self.start_datetime.isoformat(),
            "boundary_duration[]": self.boundary_duration,
            "from": self.from_,
        }

        if self.to:
            filters["to"] = self.to

        if self.min_duration is not None:
            filters["min_duration"] = self.min_duration

        if self.first_section_mode:
            filters["first_section_mode[]"] = self.first_section_mode

        if self.last_section_mode:
            filters["last_section_mode[]"] = self.last_section_mode

        if self.max_duration is not None:
            filters["max_duration"] = self.max_duration
            # Special logic: if max_duration is set and boundary_duration is empty, remove min_duration
            if len(self.boundary_duration) == 0:
                filters.pop("min_duration", None)

        return filters
