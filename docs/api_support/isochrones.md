# Isochrones

A client class to interact with the Navitia API for performing inverted geocoding operations.

Official documentation: <https://doc.navitia.io/#isochrones-api>

Property: `NavitiaClient.isochrones`

Methods

```python

    list_isochrones_with_region_id(
        from_: str,
        region_id: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Collection[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Collection[str]] = None,
        last_section_mode: Optional[Collection[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None
    ) -> Collection[Isochrone]
        Fetches isochrones data for a specific region based on various parameters.

    list_isochrones(
        from_: str,
        start_datetime: datetime = datetime.now(),
        boundary_duration: Collection[int] = [],
        to: Optional[str] = None,
        first_section_mode: Optional[Collection[str]] = None,
        last_section_mode: Optional[Collection[str]] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None
    ) -> Collection[Isochrone]
        Fetches isochrones data based on various parameters.
```
