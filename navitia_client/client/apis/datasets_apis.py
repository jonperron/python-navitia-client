from datetime import datetime
from typing import Any, Sequence

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.contributor import Contributor
from navitia_client.entities.dataset import Dataset


class DatasetsApiClient(ApiBaseClient):
    @staticmethod
    def _get_regions_from_response(raw_datasets_response: Any) -> Sequence[Dataset]:
        datasets = []
        for dataset in raw_datasets_response:
            dataset_contributor = dataset.get("contributor")
            if not dataset_contributor:
                continue

            datasets.append(
                Dataset(
                    contributor=Contributor(
                        id=dataset_contributor.get("id"),
                        name=dataset_contributor.get("name"),
                        license=dataset_contributor.get("license"),
                        website=dataset_contributor.get("website"),
                    ),
                    description=dataset.get("description"),
                    end_validation_date=datetime.strptime(
                        dataset.get("end_validation_date"), "%Y%m%dT%H%M%S"
                    ),
                    id=dataset.get("id"),
                    realtime_level=dataset.get("realtime_level"),
                    start_validation_date=datetime.strptime(
                        dataset.get("start_validation_date"), "%Y%m%dT%H%M%S"
                    ),
                    system=dataset.get("system"),
                )
            )

        return datasets

    def list_datasets(self) -> Sequence[Dataset]:
        results = self.get_navitia_api(f"{self.base_navitia_url}/datasets")
        raw_results = results.json()["datasets"]
        return DatasetsApiClient._get_regions_from_response(raw_results)

    def get_dataset_by_id(self, dataset_id: str) -> Sequence[Dataset]:
        results = self.get_navitia_api(f"{self.base_navitia_url}/coverage/{dataset_id}")
        raw_results = results.json()["datasets"]
        return DatasetsApiClient._get_regions_from_response(raw_results)
