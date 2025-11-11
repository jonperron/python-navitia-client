from dataclasses import dataclass
from typing import Dict, Any, Optional, Sequence

from .base_entity_request import BaseEntityRequest


@dataclass
class PlacesNearbyRequest(BaseEntityRequest):
    """
    Request class for Places Nearby queries.

    Attributes
    ----------
    distance : int, optional
        The distance for nearby search (default is 500).
    type : Sequence[str], optional
        The types of places to include in the search (default is ["stop_area", "stop_point", "poi"]).
    admin_uri : Optional[Sequence[str]], optional
        The administrative URIs to filter by (default is None).
    filter : Optional[str], optional
        Additional filtering criteria (default is None).
    disable_geojson : bool, optional
        Whether to disable GeoJSON format in the response (default is False).
    disable_disruption : bool, optional
        Whether to disable disruption information (default is False).
    depth : int, optional
        The depth of data to retrieve (default is 1).
    add_poi_infos : Sequence[str], optional
        Additional POI information to include (default is ["bss_stands", "car_park"]).
    """

    distance: int = 500
    type: Sequence[str] = ("stop_area", "stop_point", "poi")
    admin_uri: Optional[Sequence[str]] = None
    filter: Optional[str] = None
    disable_geojson: bool = False
    disable_disruption: bool = False
    depth: int = 1
    add_poi_infos: Sequence[str] = ("bss_stands", "car_park")

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the PlacesNearbyRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        filters = {
            "start_page": self.start_page,
            "count": self.count,
            "depth": self.depth,
            "type[]": self.type,
            "distance": self.distance,
            "add_poi_infos[]": self.add_poi_infos,
        }

        if self.disable_geojson:
            filters["disable_geojson"] = self.disable_geojson
        if self.disable_disruption:
            filters["disable_disruption"] = self.disable_disruption
        if self.admin_uri:
            filters["admin_uris[]"] = self.admin_uri
        if self.filter:
            filters["filter"] = self.filter

        return filters
