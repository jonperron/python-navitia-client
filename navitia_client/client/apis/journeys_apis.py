from typing import Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.journey import JourneyRequest
from navitia_client.entities.response import Journey


class JourneyApiClient(ApiBaseClient):
    """A client class to interact with the Navitia API for fetching journey data.

    See https://doc.navitia.io/#journeys
    """

    def _get_journeys(self, url: str, filters: dict) -> Sequence[Journey]:
        """Internal method to fetch journey data based on the provided URL and filters.

        Args:
            url: The API endpoint URL for fetching journey data.
            filters: The query parameters for filtering the journey data.

        Returns:
            A list of Journey objects created from the API response.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        journeys = [Journey.from_payload(data) for data in results.json()["journeys"]]
        return journeys

    def list_journeys(
        self,
        request: JourneyRequest,
    ) -> Sequence[Journey]:
        """Fetch journey data based on various parameters.

        Args:
            request: Journey request containing all query parameters.

        Returns:
            A list of Journey objects representing the journey results.
        """
        request_url = f"{self.base_navitia_url}/journeys"

        return self._get_journeys(request_url, request.to_filters())

    def list_journeys_with_region_id(
        self,
        region_id: str,
        request: JourneyRequest,
    ) -> Sequence[Journey]:
        """Fetch journey data for a specific region based on various parameters.

        Args:
            region_id: The ID of the region to fetch journey data for.
            request: Journey request containing all query parameters.

        Returns:
            A list of Journey objects representing the journey results for the specified region.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/journeys"

        return self._get_journeys(request_url, request.to_filters())

    def list_journeys_with_resource_path(
        self,
        resource_path: str,
        request: JourneyRequest,
    ) -> Sequence[Journey]:
        """Fetch journey data for a specific resource path based on various parameters.

        Args:
            resource_path: The resource path to fetch journey data for.
            request: Journey request containing all query parameters.

        Returns:
            A list of Journey objects representing the journey results for the specified resource path.
        """
        request_url = f"{self.base_navitia_url}/coverage/{resource_path}/journeys"

        return self._get_journeys(request_url, request.to_filters())
