# Vehicle journeys

A client class to interact with the Navitia API for fetching departure information.

Official documentation: <https://doc.navitia.io/#departures>

Property: `NavitiaClient.departures`

Methods

```python

    list_departures_by_region_id_and_path(
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Collection[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all"
    ) -> Tuple[Collection[Departure], Pagination]
        Retrieves a list of departures for a specified region and resource path from the Navitia API.

    list_departures_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Collection[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all"
    ) -> Tuple[Collection[Departure], Pagination]
        Retrieves a list of departures for a specified location based on coordinates from the Navitia API.
```
