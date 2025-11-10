# Commercial modes

API client for handling 'CommercialMode' entities in the Navitia API.

Official documentation: <https://doc.navitia.io/#pt-ref>

Property: `NavitiaClient.commercial_modes`

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
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Lists commercial modes from a specified region.

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
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Retrieves a specific commercial mode by its ID from a specified region.

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
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Lists commercial modes from specified coordinates.

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
        ) -> Tuple[Sequence[CommercialMode], Pagination]:
            Retrieves a specific commercial mode by its ID from specified coordinates.
```
