# Public Transport objects

A client class to interact with the Navitia API for fetching public transport objects.

Official documentation: <https://doc.navitia.io/#pt-objects>

Property: `NavitiaClient.pt_objects`

Methods

```python

    list_public_transport_objects(
        region_id: str,
        query: str,
        type: Collection[str] = [
            "network",
            "commercial_mode",
            "line",
            "route",
            "stop_area",
        ],
        disable_disruption: bool = False,
        depth: int = 1,
        post_query_filter: Optional[str] = None,
    ) -> Collection[PtObject]:
        Retrieves a list of public transport objects for a specified region from the Navitia API.

```
