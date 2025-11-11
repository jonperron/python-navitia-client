from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.dataset import DatasetRequest
from navitia_client.entities.response.dataset import Dataset
from navitia_client.entities.response import Pagination


class DatasetsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching dataset information.
    Uses the DatasetRequest class to encapsulate query parameters.

    See https://doc.navitia.io/#datasets
    """

    @staticmethod
    def _get_datasets_from_response(raw_datasets_response: Any) -> Sequence[Dataset]:
        """
        Converts raw response data into a list of Dataset objects.

        Parameters
        ----------
        raw_datasets_response : Any
            The raw response data from the API containing datasets' information.

        Returns
        -------
        Sequence[Dataset]
            A list of Dataset objects created from the raw response data.
        """
        datasets = []
        for dataset in raw_datasets_response:
            dataset_contributor = dataset.get("contributor")
            if not dataset_contributor:
                continue

            datasets.append(Dataset.from_payload(dataset))

        return datasets

    def list_datasets(
        self, region_id: str, request: DatasetRequest
    ) -> Tuple[Sequence[Dataset], Pagination]:
        """
        Retrieves a list of datasets for a specified region from the Navitia API.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch datasets from.
        request : DatasetRequest
            The request object containing query parameters (count, start_page).

        Returns
        -------
        Tuple[Sequence[Dataset], Pagination]
            A tuple containing a list of Dataset objects and a Pagination object for managing result pages.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/datasets"
        results = self.get_navitia_api(
            url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["datasets"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return DatasetsApiClient._get_datasets_from_response(raw_results), pagination

    def get_dataset_by_id(
        self, region_id: str, dataset_id: str, request: DatasetRequest
    ) -> Tuple[Sequence[Dataset], Pagination]:
        """
        Retrieves information about a specific dataset by its ID within a region.

        Parameters
        ----------
        region_id : str
            The identifier of the region to fetch the dataset from.
        dataset_id : str
            The identifier of the dataset to fetch.
        request : DatasetRequest
            The request object containing query parameters (count, start_page).

        Returns
        -------
        Tuple[Sequence[Dataset], Pagination]
            A tuple containing a list of Dataset objects and a Pagination object for managing result pages.
        """
        url = f"{self.base_navitia_url}/coverage/{region_id}/datasets/{dataset_id}"
        results = self.get_navitia_api(
            url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["datasets"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return DatasetsApiClient._get_datasets_from_response(raw_results), pagination
