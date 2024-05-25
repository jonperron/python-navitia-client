from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.physical_mode import PhysicalMode


class PhysicalModeApiClient(ApiBaseClient, EntityApi[PhysicalMode]):
    """
    API client for handling 'PhysicalMode' entities in the Navitia API.

    See https://doc.navitia.io/#pt-ref

    Attributes
    ----------
    entity_name : str
        Name of the entity ('physical_modes').
    get_navitia_api : method
        Method to get the Navitia API.

    Methods
    -------
    _get_entity_from_response(raw_entity_response: Any) -> Sequence[PhysicalMode]:
        Static method to extract PhysicalMode instances from the raw API response.

    list_entity_collection_from_region(
        region_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        List physical modes for a given region.

    get_entity_by_id(
        region_id: str,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        Get a physical mode by its ID in a given region.

    list_entity_collection_from_coordinates(
        lon: float,
        lat: float,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        List physical modes for given geographic coordinates.

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
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        Get a physical mode by its ID for given geographic coordinates.
    """

    entity_name: str = "physical_modes"
    get_navitia_api = ApiBaseClient.get_navitia_api

    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[PhysicalMode]:
        """
        Static method to extract PhysicalMode instances from the raw API response.

        Parameters
        ----------
        raw_entity_response : Any
            Raw API response containing PhysicalMode data.

        Returns
        -------
        Sequence[PhysicalMode]
            List of PhysicalMode instances.
        """
        entities = []
        for entity in raw_entity_response:
            entities.append(PhysicalMode.from_payload(entity))
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
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """
        List physical modes for a given region.

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
            Physical mode headsign.

        Returns
        -------
        Tuple[Sequence[PhysicalMode], Pagination]
            List of PhysicalMode instances and pagination information.
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
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """
        Get a physical mode by its ID in a given region.

        Parameters
        ----------
        region_id : str
            ID of the region.
        object_id : str
            ID of the physical mode.
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
            Physical mode headsign.

        Returns
        -------
        Tuple[Sequence[PhysicalMode], Pagination]
            List of PhysicalMode instances and pagination information.
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
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """
        List physical modes for given geographic coordinates.

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
            Physical mode headsign.

        Returns
        -------
        Tuple[Sequence[PhysicalMode], Pagination]
            List of PhysicalMode instances and pagination information.
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
    ) -> Tuple[Sequence[PhysicalMode], Pagination]:
        """
        Get a physical mode by its ID for given geographic coordinates.

        Parameters
        ----------
        lon : float
            Longitude.
        lat : float
            Latitude.
        object_id : str
            ID of the physical mode.
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
            Physical mode headsign.

        Returns
        -------
        Tuple[Sequence[PhysicalMode], Pagination]
            List of PhysicalMode instances and pagination information.
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
