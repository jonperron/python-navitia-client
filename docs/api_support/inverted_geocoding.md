# Inverted geocoding

A client class to interact with the Navitia API for performing inverted geocoding operations.

Official documentation: <https://doc.navitia.io/#coord>

Property: `NavitiaClient.inverted_geocoding`

Methods

```python

    get_address_and_region_from_coordinates(lon: float, lat: float) -> Sequence[Place]
        Retrieves address and region information based on given coordinates.

    get_address_and_region_from_id(id: str) -> Sequence[Place]
        Retrieves address and region information based on a given place ID.

    get_address_from_region_coordinates_and_coordinates(region_lon: float, region_lat: float, lon: float, lat: float) -> Sequence[Place]
        Retrieves address information based on region coordinates and specific coordinates.

    get_address_from_region_coordinates_and_id(region_lon: float, region_lat: float, id: str) -> Sequence[Place]
        Retrieves address information based on region coordinates and a specific place ID.

    get_address_from_region_id_and_coordinates(region_id: str, lon: float, lat: float) -> Sequence[Place]
        Retrieves address information based on a region ID and specific coordinates.

    get_address_from_region_id_and_id(region_id: str, id: str) -> Sequence[Place]
        Retrieves address information based on a region ID and a specific place ID.
```
