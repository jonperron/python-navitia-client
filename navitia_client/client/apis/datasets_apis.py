from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.dataset import Dataset
from navitia_client.entities.pagination import Pagination


class DatasetsApiClient(ApiBaseClient):
    @staticmethod
    def _get_datasets_from_response(raw_datasets_response: Any) -> Sequence[Dataset]:
        datasets = []
        for dataset in raw_datasets_response:
            dataset_contributor = dataset.get("contributor")
            if not dataset_contributor:
                continue

            datasets.append(Dataset.from_json(dataset))

        return datasets

    def list_datasets(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Dataset], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/datasets?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["datasets"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return DatasetsApiClient._get_datasets_from_response(raw_results), pagination

    def get_dataset_by_id(
        self, region_id: str, dataset_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Dataset], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/datasets/{dataset_id}?start_page={start_page}&count={count}"
        )
        raw_results = results.json()["datasets"]
        pagination = Pagination.from_json(results.json()["pagination"])
        return DatasetsApiClient._get_datasets_from_response(raw_results), pagination
