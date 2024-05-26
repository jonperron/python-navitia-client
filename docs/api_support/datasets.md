# Datasets

A client class to interact with the Navitia API for fetching dataset information.

Official documentation: <https://doc.navitia.io/#datasets>

Property: `NavitiaClient.datasets`

Methods:

```python
    list_datasets(region_id: str, start_page: int = 0, count: int = 25) -> Tuple[Sequence[Dataset], Pagination]
        Retrieves a list of datasets for a specified region from the Navitia API.

    get_dataset_by_id(region_id: str, dataset_id: str, start_page: int = 0, count: int = 25) -> Tuple[Sequence[Dataset], Pagination]
        Retrieves information about a specific dataset by its ID within a region.
    """
```
