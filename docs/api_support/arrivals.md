# Arrivals

A client class to interact with the Navitia API for fetching arrival information.

Official documentation: <https://doc.navitia.io/#arrivals>

Property: `NavitiaClient.arrivals`

Methods

```python

    list_arrivals_by_region_id_and_path(
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        count: int = 10,
        start_page: int = 0,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all"
    ) -> Tuple[Sequence[Arrival], Pagination]
        Retrieves a list of arrivals for a specific region and resource path.

    list_arrivals_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        count: int = 10,
        start_page: int = 0,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all"
    ) -> Tuple[Sequence[Arrival], Pagination]
        Retrieves a list of arrivals for specific coordinates.
```

````
