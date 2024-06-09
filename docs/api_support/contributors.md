# Contributors

A client class to interact with the Navitia API for fetching contributors APIs.

Official documentation: <https://doc.navitia.io/#contributors>

Property: `NavitiaClient.contributors`

Methods:

```python

    list_contributors(region_id: str, start_page: int = 0, count: int = 25) -> Tuple[Collection[Contributor], Pagination]
        Retrieves a list of contributors for a specified region from the Navitia API.

    get_contributor_on_dataset(region_id: str, dataset_id: str, start_page: int = 0, count: int = 25) -> Tuple[Collection[Contributor], Pagination]
        Retrieves a list of contributors for a specified dataset in a region from the Navitia API.
```
