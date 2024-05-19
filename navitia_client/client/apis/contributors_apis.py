from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.contributor import Contributor
from navitia_client.entities.pagination import Pagination


class ContributorsApiClient(ApiBaseClient):
    @staticmethod
    def _get_contributors_from_response(
        raw_contributors_response: Any,
    ) -> Sequence[Contributor]:
        contributors = []
        for contributor_data in raw_contributors_response:
            contributors.append(Contributor.from_payload(contributor_data))

        return contributors

    def list_contributors(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Contributor], Pagination]:
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
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/contributors/{dataset_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["contributors"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return ContributorsApiClient._get_contributors_from_response(
            raw_results
        ), pagination
