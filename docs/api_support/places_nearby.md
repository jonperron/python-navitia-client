# Places nearby

A client class to interact with the Navitia API for fetching nearby places information.

Official documentation: <https://doc.navitia.io/#places-nearby>

Property: `NavitiaClient.places_nearby`

Methods

```python

    list_objects_by_region_id_and_path(
        region_id: str, resource_path: str,
        distance: int = 500, type: Collection[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Collection[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Collection[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Collection[Place], Pagination]
        Retrieves a list of places nearby based on the region ID and resource path from the Navitia API.

    list_objects_by_region_id_and_coordinates(
        region_id: str, lon: float, lat: float,
        distance: int = 500, type: Collection[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Collection[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Collection[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Collection[Place], Pagination]
        Retrieves a list of places nearby based on the region ID and coordinates from the Navitia API.

    list_objects_by_coordinates(
        region_lon: float, region_lat: float, lon: float, lat: float,
        distance: int = 500, type: Collection[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Collection[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Collection[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Collection[Place], Pagination]
        Retrieves a list of places nearby based on the coordinates from the Navitia API.

    list_objects_by_object_coordinates_only(
        lon: float, lat: float, distance: int = 500,
        type: Collection[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Collection[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Collection[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Collection[Place], Pagination]
        Retrieves a list of places nearby based on the coordinates only from the Navitia API.

```
