from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.place import Place


class InvertedGeocodingApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for performing inverted geocoding operations.

    See https://doc.navitia.io/#coord

    Methods
    -------
    _get_regions_from_response(response: Any) -> Sequence[Place]
        A static method to transform raw API response data into a list of Place objects.

    get_address_and_region_from_coordinates(lon: float, lat: float) -> Sequence[Place]
        Retrieves address and region information based on given coordinates.

    get_address_and_region_from_id(id: str) -> Sequence[Place]
        Retrieves address and region information based on a given place ID.

    get_address_from_region_coordinates_and_coordinates(region_lon: float, region_lat: float, lon: float, lat: float) -> Sequence[Place]
        Retrieves address information based on region coordinates and specific coordinates.

    get_address_from_region_coordinates_and_id(region_lon: float, region_lat: float, id: str) -> Sequence[Place]
        Retrieves address information based on region coordinates and a specific place ID.

    get_address_from_region_id_and_coordinates(region_id: str, lon: float, lat: float) -> Sequence[Place]
        Retrieves address information based on a region ID and specific coordinates.

    get_address_from_region_id_and_id(region_id: str, id: str) -> Sequence[Place]
        Retrieves address information based on a region ID and a specific place ID.
    """

    @staticmethod
    def _get_regions_from_response(response: Any) -> Sequence[Place]:
        """
        Converts raw response data into a list of Place objects.

        Parameters
        ----------
        response : Any
            The raw response data from the API containing places' information.

        Returns
        -------
        Sequence[Place]
            A list of Place objects created from the raw response data.
        """
        entities = []
        for entity_data in response:
            entities.append(Place.from_payload(entity_data))

        return entities

    def get_address_and_region_from_coordinates(
        self, lon: float, lat: float
    ) -> Sequence[Place]:
        """
        Retrieves address and region information based on given coordinates.

        Parameters
        ----------
        lon : float
            The longitude of the location.
        lat : float
            The latitude of the location.

        Returns
        -------
        Sequence[Place]
            A list of Place objects representing the address and region information.
        """
        result = self.get_navitia_api(f"{self.base_navitia_url}/places/{lon};{lat}")
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_and_region_from_id(self, id: str) -> Sequence[Place]:
        """
        Retrieves address and region information based on a given place ID.

        Parameters
        ----------
        id : str
            The identifier of the place.

        Returns
        -------
        Sequence[Place]
            A list of Place objects representing the address and region information.
        """
        result = self.get_navitia_api(f"{self.base_navitia_url}/places/{id}")
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_coordinates_and_coordinates(
        self, region_lon: float, region_lat: float, lon: float, lat: float
    ) -> Sequence[Place]:
        """
        Retrieves address information based on region coordinates and specific coordinates.

        Parameters
        ----------
        region_lon : float
            The longitude of the region.
        region_lat : float
            The latitude of the region.
        lon : float
            The longitude of the specific location.
        lat : float
            The latitude of the specific location.

        Returns
        -------
        Sequence[Place]
            A list of Place objects representing the address information.
        """
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/places/{lon};{lat}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_coordinates_and_id(
        self, region_lon: float, region_lat: float, id: str
    ) -> Sequence[Place]:
        """
        Retrieves address information based on region coordinates and a specific place ID.

        Parameters
        ----------
        region_lon : float
            The longitude of the region.
        region_lat : float
            The latitude of the region.
        id : str
            The identifier of the place.

        Returns
        -------
        Sequence[Place]
            A list of Place objects representing the address information.
        """
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/places/{id}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_id_and_coordinates(
        self, region_id: str, lon: float, lat: float
    ) -> Sequence[Place]:
        """
        Retrieves address information based on a region ID and specific coordinates.

        Parameters
        ----------
        region_id : str
            The identifier of the region.
        lon : float
            The longitude of the specific location.
        lat : float
            The latitude of the specific location.

        Returns
        -------
        Sequence[Place]
            A list of Place objects representing the address information.
        """
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/places/{lon};{lat}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places

    def get_address_from_region_id_and_id(
        self, region_id: str, id: str
    ) -> Sequence[Place]:
        """
        Retrieves address information based on a region ID and a specific place ID.

        Parameters
        ----------
        region_id : str
            The identifier of the region.
        id : str
            The identifier of the place.

        Returns
        -------
        Sequence[Place]
            A list of Place objects representing the address information.
        """
        result = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/places/{id}"
        )
        places = self._get_regions_from_response(result.json()["places"])
        return places
