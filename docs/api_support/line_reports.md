# Line reports

A client class to interact with the Navitia API for fetching line reports.

Official documentation: <https://doc.navitia.io/#line-reports>

Property: `NavitiaClient.line_reports`

Methods

```python

    list_line_reports(
        region_id: Optional[str] = None,
        resource_path: Optional[str] = None,
        since: Optional[datetime] = None,
        until: Optional[datetime] = None,
        count: int = 25,
        depth: int = 1,
        forbidden_uris: Optional[Collection[str]] = None,
        disable_geojson: bool = False
    ) -> Tuple[Collection[Disruption], Collection[LineReport]]:
        Lists line reports based on specified criteria.
```
