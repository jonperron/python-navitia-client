from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.physical_mode import CommercialMode


class CommercialModeApiClient(ApiBaseClient, EntityApi[CommercialMode]):
    """
    API client for handling 'CommercialMode' entities in the Navitia API.

    See https://doc.navitia.io/#pt-ref

    Attributes:
        entity_name (str): The name of the entity.
        get_navitia_api: A method to get the Navitia API.

    Methods:
        _get_entity_from_response(raw_entity_response: Any) -> Sequence[CommercialMode]:
            Extracts CommercialMode entities from the API response.

        list_entity_collection_from_region(
            region_id: str,
            start_page: int = 0,
            count: int = 25,
            depth: int = 1,
            odt: str = "all",
            distance: int = 200,
            headsign: Optional[str] = None,
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Lists commercial modes from a specified region.

        get_entity_by_id(
            region_id: str,
            object_id: str,
            start_page: int = 0,
            count: int = 25,
            depth: int = 1,
            odt: str = "all",
            distance: int = 200,
            headsign: Optional[str] = None,
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Retrieves a specific commercial mode by its ID from a specified region.

        list_entity_collection_from_coordinates(
            lon: float,
            lat: float,
            start_page: int = 0,
            count: int = 25,
            depth: int = 1,
            odt: str = "all",
            distance: int = 200,
            headsign: Optional[str] = None,
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Lists commercial modes from specified coordinates.

        get_entity_by_id_and_coordinates(
            lon: float,
            lat: float,
            object_id: str,
            start_page: int = 0,
            count: int = 25,
            depth: int = 1,
            odt: str = "all",
            distance: int = 200,
            headsign: Optional[str] = None,
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Retrieves a specific commercial mode by its ID from specified coordinates.
    """

    entity_name: str = "commercial_modes"
    get_navitia_api = ApiBaseClient.get_navitia_api

    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[CommercialMode]:
        """
        Extracts CommercialMode entities from the API response.

        Parameters:
            raw_entity_response (Any): The raw response from the API.

        Returns:
            Sequence[CommercialMode]: A sequence of CommercialMode objects.
        """
        entities = []
        for entity in raw_entity_response:
            entities.append(CommercialMode.from_payload(entity))
        return entities

    def list_entity_collection_from_region(
        self,
        region_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """
        Lists commercial modes from a specified region.

        Parameters:
            region_id (str): The ID of the region.
            start_page (int): The starting page for pagination. Defaults to 0.
            count (int): The number of results per page. Defaults to 25.
            depth (int): The depth of data to retrieve. Defaults to 1.
            odt (str): The object detail type. Defaults to "all".
            distance (int): The distance in meters for filtering. Defaults to 200.
            headsign (Optional[str]): The headsign for filtering. Defaults to None.

        Returns:
            Tuple[Sequence[CommercialMode], Pagination]: A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "odt": odt,
            "distance": distance,
        }

        if headsign is not None:
            filters["headsign"] = headsign
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, filters)

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
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """
        Retrieves a specific commercial mode by its ID from a specified region.

        Parameters:
            region_id (str): The ID of the region.
            object_id (str): The ID of the commercial mode.
            start_page (int): The starting page for pagination. Defaults to 0.
            count (int): The number of results per page. Defaults to 25.
            depth (int): The depth of data to retrieve. Defaults to 1.
            odt (str): The object detail type. Defaults to "all".
            distance (int): The distance in meters for filtering. Defaults to 200.
            headsign (Optional[str]): The headsign for filtering. Defaults to None.

        Returns:
            Tuple[Sequence[CommercialMode], Pagination]: A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "odt": odt,
            "distance": distance,
        }

        if headsign is not None:
            filters["headsign"] = headsign

        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, filters)

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
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """
        Lists commercial modes from specified coordinates.

        Parameters:
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            start_page (int): The starting page for pagination. Defaults to 0.
            count (int): The number of results per page. Defaults to 25.
            depth (int): The depth of data to retrieve. Defaults to 1.
            odt (str): The object detail type. Defaults to "all".
            distance (int): The distance in meters for filtering. Defaults to 200.
            headsign (Optional[str]): The headsign for filtering. Defaults to None.

        Returns:
            Tuple[Sequence[CommercialMode], Pagination]: A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "odt": odt,
            "distance": distance,
        }

        if headsign is not None:
            filters["headsign"] = headsign

        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, filters)

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
    ) -> Tuple[Sequence[CommercialMode], Pagination]:
        """
        Retrieves a specific commercial mode by its ID from specified coordinates.

        Parameters:
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            object_id (str): The ID of the commercial mode.
            start_page (int): The starting page for pagination. Defaults to 0.
            count (int): The number of results per page. Defaults to 25.
            depth (int): The depth of data to retrieve. Defaults to 1.
            odt (str): The object detail type. Defaults to "all".
            distance (int): The distance in meters for filtering. Defaults to 200.
            headsign (Optional[str]): The headsign for filtering. Defaults to None.

        Returns:
            Tuple[Sequence[CommercialMode], Pagination]: A tuple containing a sequence of CommercialMode objects and Pagination object.
        """
        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "odt": odt,
            "distance": distance,
        }

        if headsign is not None:
            filters["headsign"] = headsign

        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, filters)
