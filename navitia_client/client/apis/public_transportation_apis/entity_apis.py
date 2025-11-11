from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, Tuple, TypeVar

from navitia_client.entities.request.base_entity_request import BasePTEntityRequest
from navitia_client.entities.response.company import Company
from navitia_client.entities.response.disruption import Disruption
from navitia_client.entities.response.line_and_route import Line, Route
from navitia_client.entities.response.network import Network
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.physical_mode import CommercialMode, PhysicalMode
from navitia_client.entities.response.stop_area import StopArea, StopPoint
from navitia_client.entities.response.vehicle_journey import VehicleJourney

TEntity = TypeVar(
    "TEntity",
    Network,
    Line,
    Route,
    StopPoint,
    StopArea,
    CommercialMode,
    PhysicalMode,
    Disruption,
    Company,
    VehicleJourney,
)


class EntityApi(Generic[TEntity], ABC):
    """Abstract base class for API clients dealing with entities in the Navitia API.

    This class provides common functionality for all PT entity API clients including
    methods to fetch entities by region, coordinates, or ID.

    Attributes:
        entity_name: Name of the entity.
        get_navitia_api: Method to get the Navitia API.
    """

    entity_name: str
    get_navitia_api: Any

    @staticmethod
    @abstractmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[TEntity]:
        """Extract entity instances from the raw API response.

        Args:
            raw_entity_response: Raw API response containing entity data.

        Returns:
            List of entity instances.
        """
        raise NotImplementedError

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string from provided filters.

        Args:
            filters: Dictionary of filters.

        Returns:
            Query string.
        """
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_entity_results(
        self, url: str, entity: str, filters: dict[str, Any]
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """Fetch entity results from the API.

        Args:
            url: API endpoint URL.
            entity: Name of the entity.
            filters: Dictionary of filters.

        Returns:
            List of entity instances and pagination information.
        """
        query_string = self._generate_filter_query(filters)
        results = self.get_navitia_api(url + query_string)
        raw_results = results.json()[entity]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_entity_from_response(raw_results), pagination

    @abstractmethod
    def list_entity_collection_from_region(
        self,
        region_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """List entities for a given region.

        Args:
            region_id: ID of the region.
            request: Request parameters for filtering.

        Returns:
            List of entities and pagination information.
        """
        raise NotImplementedError

    @abstractmethod
    def get_entity_by_id(
        self,
        region_id: str,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """Get an entity by its ID in a given region.

        Args:
            region_id: ID of the region.
            object_id: ID of the entity.
            request: Request parameters for filtering.

        Returns:
            List of entities and pagination information.
        """
        raise NotImplementedError

    @abstractmethod
    def list_entity_collection_from_coordinates(
        self,
        lon: float,
        lat: float,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """List entities for given geographic coordinates.

        Args:
            lon: Longitude.
            lat: Latitude.
            request: Request parameters for filtering.

        Returns:
            List of entities and pagination information.
        """
        raise NotImplementedError

    @abstractmethod
    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """Get an entity by its ID for given geographic coordinates.

        Args:
            lon: Longitude.
            lat: Latitude.
            object_id: ID of the entity.
            request: Request parameters for filtering.

        Returns:
            List of entities and pagination information.
        """
        raise NotImplementedError
