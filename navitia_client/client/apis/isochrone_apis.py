from typing import Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.isochrone import IsochroneRequest
from navitia_client.entities.response.isochrones import Isochrone


class IsochronesApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching isochrones data.

    See https://doc.navitia.io/#isochrones-api
    """

    def _get_traffic_reports(self, url: str, filters: dict) -> Sequence[Isochrone]:
        """Fetch isochrone data based on the provided URL and filters.

        Args:
            url: The API endpoint URL for fetching isochrone data.
            filters: The query parameters for filtering the isochrone data.

        Returns:
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
        """Fetch isochrones data for a specific region based on various parameters.

        Args:
            region_id: The identifier of the region.
            request: The request object containing query parameters.

        Returns:
            A list of Isochrone objects representing the isochrone data.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/isochrones"
        return self._get_traffic_reports(request_url, request.to_filters())

    def list_isochrones(
        self,
        request: IsochroneRequest,
    ) -> Sequence[Isochrone]:
        """Fetch isochrones data based on various parameters.

        Args:
            request: The request object containing query parameters.

        Returns:
            A list of Isochrone objects representing the isochrone data.
        """
        request_url = f"{self.base_navitia_url}/isochrones"
        return self._get_traffic_reports(request_url, request.to_filters())
