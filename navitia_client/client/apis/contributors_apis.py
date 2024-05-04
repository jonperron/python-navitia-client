from typing import Any, Sequence

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.contributor import Contributor


class ContributorsApiClient(ApiBaseClient):
    @staticmethod
    def _get_contributors_from_response(
        raw_contributors_response: Any,
    ) -> Sequence[Contributor]:
        contributors = []
        for contributor_data in raw_contributors_response:
            contributors.append(Contributor.from_json(contributor_data))

        return contributors

    def list_contributors(self, region_id: str) -> Sequence[Contributor]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/contributors"
        )
        raw_results = results.json()["contributors"]
        return ContributorsApiClient._get_contributors_from_response(raw_results)

    def get_contributor_on_dataset(
        self, region_id: str, dataset_id: str
    ) -> Sequence[Contributor]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/contributors/{dataset_id}"
        )
        raw_results = results.json()["contributors"]
        return ContributorsApiClient._get_contributors_from_response(raw_results)
