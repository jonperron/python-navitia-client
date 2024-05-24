from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.contributor import Contributor
from navitia_client.entities.pagination import Pagination


class ContributorsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching contributors APIs.

    See https://doc.navitia.io/#contributors

    Methods
    -------
    _get_contributors_from_response(raw_contributors_response: Any) -> Sequence[Contributor]
        A static method to transform raw API response data into a list of Contributor objects.

    list_contributors(region_id: str, start_page: int = 0, count: int = 25) -> Tuple[Sequence[Contributor], Pagination]
        Retrieves a list of contributors for a specified region from the Navitia API.

    get_contributor_on_dataset(region_id: str, dataset_id: str, start_page: int = 0, count: int = 25) -> Tuple[Sequence[Contributor], Pagination]
        Retrieves a list of contributors for a specified dataset in a region from the Navitia API.
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
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Contributor], Pagination]:
        """
        Retrieves a list of contributors for a specific region.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch contributors from.
        start_page : int, optional
            The starting page for pagination (default is 0).
        count : int, optional
            The number of contributors to fetch per page (default is 25).

        Returns
        -------
        Tuple[Sequence[Contributor], Pagination]
            A tuple containing a list of Contributor objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/contributors?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["contributors"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return ContributorsApiClient._get_contributors_from_response(
            raw_results
        ), pagination

    def get_contributor_on_dataset(
        self, region_id: str, dataset_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Contributor], Pagination]:
        """
        Retrieves a list of contributors for a specific dataset in a region.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch contributors from.
        dataset_id : str
            The identifier of the dataset to fetch contributors for.
        start_page : int, optional
            The starting page for pagination (default is 0).
        count : int, optional
            The number of contributors to fetch per page (default is 25).

        Returns
        -------
        Tuple[Sequence[Contributor], Pagination]
            A tuple containing a list of Contributor objects and a Pagination object for managing result pages.
        """
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/contributors/{dataset_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["contributors"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return ContributorsApiClient._get_contributors_from_response(
            raw_results
        ), pagination
