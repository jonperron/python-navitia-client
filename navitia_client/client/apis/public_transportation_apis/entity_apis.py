from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Sequence, Tuple, TypeVar

from navitia_client.entities.company import Company
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.line_and_route import Line, Route
from navitia_client.entities.network import Network
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.physical_mode import CommercialMode, PhysicalMode
from navitia_client.entities.stop_area import StopArea, StopPoint
from navitia_client.entities.vehicle_journey import VehicleJourney

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
    """
    Abstract base class for API clients dealing with entities in the Navitia API.

    Attributes
    ----------
    entity_name : str
        Name of the entity.
    get_navitia_api : method
        Method to get the Navitia API.

    Methods
    -------
    _get_entity_from_response(raw_entity_response: Any) -> Sequence[TEntity]:
        Static method to extract entity instances from the raw API response.

    _generate_filter_query(filters: dict[str, Any]) -> str:
        Generate query string from provided filters.

    _get_entity_results(
        url: str,
        entity: str,
        filters: dict[str, Any]
    ) -> Tuple[Sequence[TEntity], Pagination]:
        Fetch entity results from the API.

    list_entity_collection_from_region(
        region_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[TEntity], Pagination]:
        Abstract method to list entities for a given region.

    get_entity_by_id(
        region_id: str,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[TEntity], Pagination]:
        Abstract method to get an entity by its ID in a given region.

    list_entity_collection_from_coordinates(
        lon: float,
        lat: float,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[TEntity], Pagination]:
        Abstract method to list entities for given geographic coordinates.

    get_entity_by_id_and_coordinates(
        lon: float,
        lat: float,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[TEntity], Pagination]:
        Abstract method to get an entity by its ID for given geographic coordinates.
    """

    entity_name: str
    get_navitia_api: Any

    @staticmethod
    @abstractmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[TEntity]:
        """
        Static method to extract entity instances from the raw API response.

        Parameters
        ----------
        raw_entity_response : Any
            Raw API response containing entity data.

        Returns
        -------
        Sequence[TEntity]
            List of entity instances.
        """
        raise NotImplementedError

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """
        Generate query string from provided filters.

        Parameters
        ----------
        filters : dict[str, Any]
            Dictionary of filters.

        Returns
        -------
        str
            Query string.
        """
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_entity_results(
        self, url: str, entity: str, filters: dict[str, Any]
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """
        Fetch entity results from the API.

        Parameters
        ----------
        url : str
            API endpoint URL.
        entity : str
            Name of the entity.
        filters : dict[str, Any]
            Dictionary of filters.

        Returns
        -------
        Tuple[Sequence[TEntity], Pagination]
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
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """
        List entities for a given region.

        Parameters
        ----------
        region_id : str
            ID of the region.
        start_page : int, optional
            Starting page number (default is 0).
        count : int, optional
            Number of items per page (default is 25).
        depth : int, optional
            Search depth (default is 1).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Line headsign.

        Returns
        -------
        Tuple[Sequence[TEntity], Pagination]
            List of entities and pagination information.
        """
        raise NotImplementedError

    @abstractmethod
    def get_entity_by_id(
        self,
        region_id: str,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """
        Get an entity by its ID in a given region.

        Parameters
        ----------
        region_id : str
            ID of the region.
        object_id : str
            ID of the entity.
        start_page : int, optional
            Starting page number (default is 0).
        count : int, optional
            Number of items per page (default is 25).
        depth : int, optional
            Search depth (default is 1).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Line headsign.

        Returns
        -------
        Tuple[Sequence[TEntity], Pagination]
            List of entities and pagination information.
        """
        raise NotImplementedError

    @abstractmethod
    def list_entity_collection_from_coordinates(
        self,
        lon: float,
        lat: float,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """
        List entities for given geographic coordinates.

        Parameters
        ----------
        lon : float
            Longitude.
        lat : float
            Latitude.
        start_page : int, optional
            Starting page number (default is 0).
        count : int, optional
            Number of items per page (default is 25).
        depth : int, optional
            Search depth (default is 1).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Line headsign.

        Returns
        -------
        Tuple[Sequence[TEntity], Pagination]
            List of entities and pagination information.
        """
        raise NotImplementedError

    @abstractmethod
    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """
        Get an entity by its ID for given geographic coordinates.

        Parameters
        ----------
        lon : float
            Longitude.
        lat : float
            Latitude.
        object_id : str
            ID of the entity.
        start_page : int, optional
            Starting page number (default is 0).
        count : int, optional
            Number of items per page (default is 25).
        depth : int, optional
            Search depth (default is 1).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Line headsign.

        Returns
        -------
        Tuple[Sequence[TEntity], Pagination]
            List of entities and pagination information.
        """
        raise NotImplementedError
