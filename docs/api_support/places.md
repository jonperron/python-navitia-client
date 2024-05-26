# Places

A client class to interact with the Navitia API for fetching place information.

Official documentation: <https://doc.navitia.io/#places>

Property: `NavitiaClient.places`

Methods

```python

    list_places(
        region_id: str, query: str,
        type: Sequence[str] = ["stop_area", "address", "poi", "administrative_region"],
        disable_geojson: bool = False, depth: int = 1,
        from_lon_lat: Optional[Tuple[float, float]] = None
    ) -> Sequence[Place]
        Retrieves a list of places based on the provided query and region ID from the Navitia API.
```
