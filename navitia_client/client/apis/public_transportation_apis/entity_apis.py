from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, Tuple, TypeVar

from navitia_client.entities.company import Company
from navitia_client.entities.disruption import (
    Disruption,
)
from navitia_client.entities.line_and_route import Line, Route
from navitia_client.entities.network import Network
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.physical_mode import (
    CommercialMode,
    PhysicalMode,
)
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
    @staticmethod
    @abstractmethod
    def _get_entity_from_response(
        raw_entity_response: Any,
    ) -> Sequence[TEntity]:
        """Collection of objects of a region"""
        raise NotImplementedError

    @abstractmethod
    def list_entity_collection_from_region(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """Information about a specific object"""
        raise NotImplementedError

    @abstractmethod
    def get_entity_by_id(
        self, region_id: str, object_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[TEntity], Pagination]:
        raise NotImplementedError

    @abstractmethod
    def list_entity_collection_from_coordinates(
        self, lon: float, lat: float, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """Collection of objects of a region, navitia guesses the region from coordinates"""
        raise NotImplementedError

    @abstractmethod
    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
    ) -> Tuple[Sequence[TEntity], Pagination]:
        """Information about a specific object, navitia guesses the region from coordinates"""
        raise NotImplementedError
