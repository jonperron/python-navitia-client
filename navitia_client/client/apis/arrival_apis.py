from typing import Any, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.arrival import ArrivalRequest
from navitia_client.entities.response import Pagination
from navitia_client.entities.response.arrival import Arrival


class ArrivalApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching arrival information.

    See https://doc.navitia.io/#arrivals
    """

    @staticmethod
    def _get_arrival_objects_from_response(
        response: Any,
    ) -> Sequence[Arrival]:
        """Convert raw response data into a list of Arrival objects.

        Args:
            response: The raw response data from the API containing arrivals' information.

        Returns:
            A list of Arrival objects created from the raw response data.
        """

        arrivals = []
        for arrival_data in response:
            arrivals.append(Arrival.from_payload(arrival_data))

        return arrivals

    def _get_arrivals(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Arrival], Pagination]:
        """Fetch arrivals based on a given URL and filters.

        Args:
            url: The URL for the API request.
            filters: The filters to apply to the API request.

        Returns:
            A tuple containing a list of Arrival objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["arrivals"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_arrival_objects_from_response(raw_results), pagination

    def list_arrivals_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        request: ArrivalRequest,
    ) -> Tuple[Sequence[Arrival], Pagination]:
        """Retrieve a list of arrivals for a specific region and resource path.

        Args:
            region_id: The identifier of the region to fetch arrivals from.
            resource_path: The resource path within the region to fetch arrivals for.
            request: The ArrivalRequest containing filters and parameters for the query.

        Returns:
            A tuple containing a list of Arrival objects and a Pagination object for managing result pages.
        """
        request_url = (
            f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/arrivals"
        )

        return self._get_arrivals(request_url, request.to_filters())

    def list_arrivals_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        request: ArrivalRequest,
    ) -> Tuple[Sequence[Arrival], Pagination]:
        """Retrieve a list of arrivals for specific coordinates.

        Args:
            region_lon: The longitude of the region to fetch arrivals from.
            region_lat: The latitude of the region to fetch arrivals from.
            lon: The longitude of the specific location to fetch arrivals for.
            lat: The latitude of the specific location to fetch arrivals for.
            request: The ArrivalRequest containing filters and parameters for the query.

        Returns:
            A tuple containing a list of Arrival objects and a Pagination object for managing result pages.
        """
        # List of objects near the resource, navitia guesses the region from coordinates
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/arrivals"

        return self._get_arrivals(request_url, request.to_filters())
