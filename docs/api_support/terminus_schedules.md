# Terminus schedules

A client class to interact with the Navitia API for fetching terminus schedules.

Official documentation: <https://doc.navitia.io/#terminus-schedules>

Property: `NavitiaClient.terminus_schedules`

Methods

```python

    list_terminus_schedules_by_region_id_and_path(
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        count: int = 10,
        start_page: int = 0,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        Retrieves terminus schedules for a specified region and resource path from the Navitia API.

    list_terminus_schedules_by_coordinates(
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        count: int = 10,
        start_page: int = 0,
        items_per_schedule: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[TerminusSchedule], Pagination]:
        Retrieves terminus schedules for a specified set of coordinates from the Navitia API.

```
