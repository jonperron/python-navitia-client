# Traffic reports

A client class to interact with the Navitia API for fetching traffic reports.

Official documentation: <https://doc.navitia.io/#traffic-reports>

Property: `NavitiaClient.traffic_reports`

Methods

```python

    list_traffic_reports(
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        count: int = 25,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        disable_geojson: bool = False,
    ) -> Tuple[Sequence[Disruption], Sequence[TrafficReport], Pagination]:
        Retrieves traffic reports for a specified region and resource path from the Navitia API.

```
