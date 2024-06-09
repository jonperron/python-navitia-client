#  Coverage

A client class to interact with the Navitia API for fetching coverage area information.

Official documentation: <https://doc.navitia.io/#coverage>

Property: `NavitiaClient.coverage`


Methods:

```python
    list_covered_areas(start_page: int = 0, count: int = 25) -> Tuple[Collection[Region], Pagination]
        Retrieves a list of covered areas from the Navitia API.

    get_coverage_by_region_id(region_id: str, start_page: int = 0, count: int = 25) -> Tuple[Collection[Region], Pagination]
        Retrieves information about a specific region by its ID.

    get_coverage_by_region_coordinates_and_coordinates(lon: float, lat: float, start_page: int = 0, count: int = 25) -> Tuple[Collection[Region], Pagination]
        Retrieves information about a region based on coordinates.
```
