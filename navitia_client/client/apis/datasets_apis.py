from typing import Any, Sequence

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.dataset import Dataset


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

    def list_datasets(self, region_id: str) -> Sequence[Dataset]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/datasets"
        )
        raw_results = results.json()["datasets"]
        return DatasetsApiClient._get_datasets_from_response(raw_results)

    def get_dataset_by_id(self, region_id: str, dataset_id: str) -> Sequence[Dataset]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}/datasets/{dataset_id}"
        )
        raw_results = results.json()["datasets"]
        return DatasetsApiClient._get_datasets_from_response(raw_results)
