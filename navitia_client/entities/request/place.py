from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence, Tuple

from .base_entity_request import BaseEntityRequest


@dataclass
class PlaceRequest(BaseEntityRequest):
    """
    Request class for Place queries.

    Attributes
    ----------
    query : str
        The search query string for places.
    type : Sequence[str], optional
        The types of places to search for (default is ["stop_area", "address", "poi", "administrative_region"]).
    disable_geojson : bool, optional
        Whether to disable GeoJSON in the response (default is False).
    depth : int, optional
        The depth of data to retrieve (default is 1).
    from_lon_lat : Optional[Tuple[float, float]], optional
        Longitude and latitude coordinates to filter from (default is None).
    """

    query: str
    type: Sequence[str] = ("stop_area", "address", "poi", "administrative_region")
    disable_geojson: bool = False
    depth: int = 1
    from_lon_lat: Optional[Tuple[float, float]] = None

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the PlaceRequest instance into a dictionary of filters.

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

        if self.disable_geojson:
            filters["disable_geojson"] = self.disable_geojson
        if self.from_lon_lat:
            filters["filter"] = f"{self.from_lon_lat[0]};{self.from_lon_lat[1]}"

        return filters
