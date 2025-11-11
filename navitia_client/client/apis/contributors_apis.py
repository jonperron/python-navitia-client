from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.contributor import ContributorRequest
from navitia_client.entities.response.contributor import Contributor
from navitia_client.entities.response import Pagination


class ContributorsApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching contributors.

    See https://doc.navitia.io/#contributors
    """

    @staticmethod
    def _get_contributors_from_response(
        raw_contributors_response: Any,
    ) -> Sequence[Contributor]:
        """Convert raw response data into a list of Contributor objects.

        Args:
            raw_contributors_response: The raw response data from the API containing contributors' information.

        Returns:
            A list of Contributor objects created from the raw response data.
        """
        contributors = []
        for contributor_data in raw_contributors_response:
            contributors.append(Contributor.from_payload(contributor_data))

        return contributors

    def list_contributors(
        self, region_id: str, request: ContributorRequest
    ) -> Tuple[Sequence[Contributor], Pagination]:
        """Retrieve a list of contributors for a specific region.

        Args:
            region_id: The identifier of the region to fetch contributors from.
            request: The request object containing query parameters.

        Returns:
            A tuple containing a list of Contributor objects and a Pagination object for managing result pages.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/contributors"
        results = self.get_navitia_api(
            url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["contributors"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return ContributorsApiClient._get_contributors_from_response(
            raw_results
        ), pagination

    def get_contributor_on_dataset(
        self, region_id: str, dataset_id: str, request: ContributorRequest
    ) -> Tuple[Sequence[Contributor], Pagination]:
        """Retrieve a list of contributors for a specific dataset in a region.

        Args:
            region_id: The identifier of the region to fetch contributors from.
            dataset_id: The identifier of the dataset to fetch contributors for.
            request: The request object containing query parameters.

        Returns:
            A tuple containing a list of Contributor objects and a Pagination object for managing result pages.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/contributors/{dataset_id}"
        results = self.get_navitia_api(
            url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["contributors"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return ContributorsApiClient._get_contributors_from_response(
            raw_results
        ), pagination
