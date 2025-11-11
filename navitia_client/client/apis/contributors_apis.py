from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.contributor import ContributorRequest
from navitia_client.entities.response.contributor import Contributor
from navitia_client.entities.response import Pagination


class ContributorsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching contributors APIs.
    Uses the ContributorRequest class to encapsulate query parameters.

    See https://doc.navitia.io/#contributors
    """

    @staticmethod
    def _get_contributors_from_response(
        raw_contributors_response: Any,
    ) -> Sequence[Contributor]:
        """
        Converts raw response data into a list of Contributor objects.

        Parameters
        ----------
        raw_contributors_response : Any
            The raw response data from the API containing contributors' information.

        Returns
        -------
        Sequence[Contributor]
            A list of Contributor objects created from the raw response data.
        """
        contributors = []
        for contributor_data in raw_contributors_response:
            contributors.append(Contributor.from_payload(contributor_data))

        return contributors

    def list_contributors(
        self, region_id: str, request: ContributorRequest
    ) -> Tuple[Sequence[Contributor], Pagination]:
        """
        Retrieves a list of contributors for a specific region.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch contributors from.
        request : ContributorRequest
            The request object containing query parameters (count, start_page).

        Returns
        -------
        Tuple[Sequence[Contributor], Pagination]
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
        """
        Retrieves a list of contributors for a specific dataset in a region.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch contributors from.
        dataset_id : str
            The identifier of the dataset to fetch contributors for.
        request : ContributorRequest
            The request object containing query parameters (count, start_page).

        Returns
        -------
        Tuple[Sequence[Contributor], Pagination]
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
