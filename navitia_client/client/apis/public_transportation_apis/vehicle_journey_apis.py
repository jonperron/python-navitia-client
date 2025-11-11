from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.apis.public_transportation_apis.entity_apis import EntityApi
from navitia_client.entities.request.base_entity_request import BasePTEntityRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.vehicle_journey import VehicleJourney


class VehicleJourneyApiClient(ApiBaseClient, EntityApi[VehicleJourney]):
    """
    API client for handling 'VehicleJourney' entities in the Navitia API.

    See https://doc.navitia.io/#pt-ref

    Attributes
    ----------
    entity_name : str
        Name of the entity ('stop_points').
    get_navitia_api : method
        Method to get the Navitia API.

    Methods
    -------
    _get_entity_from_response(raw_entity_response: Any) -> Sequence[VehicleJourney]:
        Static method to extract VehicleJourney instances from the raw API response.

    list_entity_collection_from_region(
        region_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        List vehicle journeys for a given region.

    get_entity_by_id(
        region_id: str,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        Get a vehicle journey by its ID in a given region.

    list_entity_collection_from_coordinates(
        lon: float,
        lat: float,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        List vehicle journeys for given geographic coordinates.

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
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        Get a vehicle journey by its ID for given geographic coordinates.
    """

    entity_name: str = "vehicle_journeys"
    get_navitia_api = ApiBaseClient.get_navitia_api

    @staticmethod
    def _get_entity_from_response(raw_entity_response: Any) -> Sequence[VehicleJourney]:
        """
        Static method to extract VehicleJourney instances from the raw API response.

        Parameters
        ----------
        raw_entity_response : Any
            Raw API response containing VehicleJourney data.

        Returns
        -------
        Sequence[VehicleJourney]
            List of VehicleJourney instances.
        """
        entities = []
        for entity in raw_entity_response:
            entities.append(VehicleJourney.from_payload(entity))
        return entities

    def list_entity_collection_from_region(
        self,
        region_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        """
        List vehicle journeys for a given region.

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
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Headsign.
        since : Optional[str], optional
            Filter objects active after this datetime (format: YYYYMMDDThhmmss).
        until : Optional[str], optional
            Filter objects active before this datetime (format: YYYYMMDDThhmmss).
        disable_disruption : bool, optional
            Whether to disable disruptions in the response (default is False).

        Returns
        -------
        Tuple[Sequence[VehicleJourney], Pagination]
            List of VehicleJourney instances and pagination information.
        """

        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id(
        self,
        region_id: str,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        """
        Get a vehicle journey by its ID in a given region.

        Parameters
        ----------
        region_id : str
            ID of the region.
        object_id : str
            ID of the vehicle journey.
        start_page : int, optional
            Starting page number (default is 0).
        count : int, optional
            Number of items per page (default is 25).
        depth : int, optional
            Search depth (default is 1).
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Headsign.
        since : Optional[str], optional
            Filter objects active after this datetime (format: YYYYMMDDThhmmss).
        until : Optional[str], optional
            Filter objects active before this datetime (format: YYYYMMDDThhmmss).
        disable_disruption : bool, optional
            Whether to disable disruptions in the response (default is False).

        Returns
        -------
        Tuple[Sequence[VehicleJourney], Pagination]
            List of VehicleJourney instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def list_entity_collection_from_coordinates(
        self,
        lon: float,
        lat: float,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        """
        List vehicle journeys for given geographic coordinates.

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
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Headsign.
        since : Optional[str], optional
            Filter objects active after this datetime (format: YYYYMMDDThhmmss).
        until : Optional[str], optional
            Filter objects active before this datetime (format: YYYYMMDDThhmmss).
        disable_disruption : bool, optional
            Whether to disable disruptions in the response (default is False).

        Returns
        -------
        Tuple[Sequence[VehicleJourney], Pagination]
            List of VehicleJourney instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())

    def get_entity_by_id_and_coordinates(
        self,
        lon: float,
        lat: float,
        object_id: str,
        request: BasePTEntityRequest,
    ) -> Tuple[Sequence[VehicleJourney], Pagination]:
        """
        Get a vehicle journey by its ID for given geographic coordinates.

        Parameters
        ----------
        lon : float
            Longitude.
        lat : float
            Latitude.
        object_id : str
            ID of the vehicle journey.
        start_page : int, optional
            Starting page number (default is 0).
        count : int, optional
            Number of items per page (default is 25).
        depth : int, optional
            Search depth (default is 1).
        disable_geojson : bool, optional
            Whether to disable GeoJSON in the response (default is False).
        odt : str, optional
            ODT type filter (default is "all").
        distance : int, optional
            Maximum search distance (default is 200).
        headsign : Optional[str], optional
            Headsign.
        since : Optional[str], optional
            Filter objects active after this datetime (format: YYYYMMDDThhmmss).
        until : Optional[str], optional
            Filter objects active before this datetime (format: YYYYMMDDThhmmss).
        disable_disruption : bool, optional
            Whether to disable disruptions in the response (default is False).

        Returns
        -------
        Tuple[Sequence[VehicleJourney], Pagination]
            List of VehicleJourney instances and pagination information.
        """
        url = f"{self.base_navitia_url}/coverage/{lon};{lat}/{self.entity_name}/{object_id}"
        return self._get_entity_results(url, self.entity_name, request.to_filters())
