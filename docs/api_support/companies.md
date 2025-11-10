#   Companies

API client for handling 'Company' entities in the Navitia API.

Official documentation: <https://doc.navitia.io/#pt-ref>

Property: `NavitiaClient.companies`

Methods:

```python
    list_entity_collection_from_region(
        region_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        disable_geojson: bool = False,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        disable_disruption: bool = False
    ) -> Tuple[Sequence[Company], Pagination]:
        List companies for a given region.

    get_entity_by_id(
        region_id: str,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        disable_geojson: bool = False,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        disable_disruption: bool = False
    ) -> Tuple[Sequence[Company], Pagination]:
        Get a company by its ID in a given region.

    list_entity_collection_from_coordinates(
        lon: float,
        lat: float,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        disable_geojson: bool = False,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        disable_disruption: bool = False
    ) -> Tuple[Sequence[Company], Pagination]:
        List companies for given geographic coordinates.

    get_entity_by_id_and_coordinates(
        lon: float,
        lat: float,
        object_id: str,
        start_page: int = 0,
        count: int = 25,
        depth: int = 1,
        disable_geojson: bool = False,
        odt: str = "all",
        distance: int = 200,
        headsign: Optional[str] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        disable_disruption: bool = False
    ) -> Tuple[Sequence[Company], Pagination]:
        Get a company by its ID for given geographic coordinates.
```
