from typing import Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.isochrone import IsochroneRequest
from navitia_client.entities.response.isochrones import Isochrone


class IsochronesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching isochrones data.

    See https://doc.navitia.io/#isochrones-api

    Methods
    -------
    _get_traffic_reports(url: str, filters: dict) -> Sequence[Isochrone]
        Internal method to fetch isochrone data based on the provided URL and filters.

    list_isochrones_with_region_id(
        region_id: str,
        request: IsochroneRequest
    ) -> Sequence[Isochrone]
        Fetches isochrones data for a specific region based on various parameters.

    list_isochrones(
        request: IsochroneRequest
    ) -> Sequence[Isochrone]
        Fetches isochrones data based on various parameters.
    """

    def _get_traffic_reports(self, url: str, filters: dict) -> Sequence[Isochrone]:
        """
        Internal method to fetch isochrone data based on the provided URL and filters.

        Parameters
        ----------
        url : str
            The API endpoint URL for fetching isochrone data.
        filters : dict
            The query parameters for filtering the isochrone data.

        Returns
        -------
        Sequence[Isochrone]
            A list of Isochrone objects created from the API response.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        isochrones = [
            Isochrone.from_payload(data) for data in results.json()["isochrones"]
        ]
        return isochrones

    def list_isochrones_with_region_id(
        self,
        region_id: str,
        request: IsochroneRequest,
    ) -> Sequence[Isochrone]:
        """
        Fetches isochrones data for a specific region based on various parameters.

        Parameters
        ----------
        region_id : str
            The identifier of the region.
        request : IsochroneRequest
            The request object containing query parameters.

        Returns
        -------
        Sequence[Isochrone]
            A list of Isochrone objects representing the isochrone data.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/isochrones"
        return self._get_traffic_reports(request_url, request.to_filters())

    def list_isochrones(
        self,
        request: IsochroneRequest,
    ) -> Sequence[Isochrone]:
        """
        Fetches isochrones data based on various parameters.

        Parameters
        ----------
        request : IsochroneRequest
            The request object containing query parameters.

        Returns
        -------
        Sequence[Isochrone]
            A list of Isochrone objects representing the isochrone data.
        """
        request_url = f"{self.base_navitia_url}/isochrones"
        return self._get_traffic_reports(request_url, request.to_filters())
