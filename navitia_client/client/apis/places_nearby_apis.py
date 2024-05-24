from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.place import Place


class PlacesNearbyApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching nearby places information.

    See https://doc.navitia.io/#places_nearby

    Methods
    -------
    _get_pt_objects_from_response(response: Any) -> Sequence[Place]
        A static method to transform raw API response data into a list of Place objects.

    list_objects_by_region_id_and_path(
        region_id: str, resource_path: str,
        distance: int = 500, type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Sequence[Place], Pagination]
        Retrieves a list of places nearby based on the region ID and resource path from the Navitia API.

    list_objects_by_region_id_and_coordinates(
        region_id: str, lon: float, lat: float,
        distance: int = 500, type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Sequence[Place], Pagination]
        Retrieves a list of places nearby based on the region ID and coordinates from the Navitia API.

    list_objects_by_coordinates(
        region_lon: float, region_lat: float, lon: float, lat: float,
        distance: int = 500, type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Sequence[Place], Pagination]
        Retrieves a list of places nearby based on the coordinates from the Navitia API.

    list_objects_by_object_coordinates_only(
        lon: float, lat: float, distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None, filter: Optional[str] = None,
        disable_geojson: bool = False, disable_disruption: bool = False,
        depth: int = 1, start_page: int = 0, count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"]
    ) -> Tuple[Sequence[Place], Pagination]
        Retrieves a list of places nearby based on the coordinates only from the Navitia API.
    """

    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[Place]:
        """
        Transform raw API response data into a list of Place objects.

        Parameters:
            response (Any): The raw API response data.

        Returns:
            Sequence[Place]: A list of Place objects.
        """
        entities = []
        for entity_data in response:
            entities.append(Place.from_payload(entity_data))

        return entities

    def _get_places_nearby(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Place], Pagination]:
        """
        Fetches nearby places based on the provided URL and filters.

        Parameters:
            url (str): The URL for the API request.
            filters (dict): Filters to be applied to the API request.

        Returns:
            Tuple[Sequence[Place], Pagination]: A tuple containing a list of nearby Place objects
                and pagination information.
        """
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["places_nearby"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_pt_objects_from_response(raw_results), pagination

    def list_objects_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        """
        Retrieves a list of places nearby based on the region ID and resource path from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            resource_path (str): The resource path.
            distance (int, optional): The distance for nearby search. Defaults to 500.
            type (Sequence[str], optional): The types of places to include in the search.
                Defaults to ["stop_area", "stop_point", "poi"].
            admin_uri (Optional[Sequence[str]], optional): The administrative URIs to filter by.
                Defaults to None.
            filter (Optional[str], optional): Additional filtering criteria. Defaults to None.
            disable_geojson (bool, optional): Whether to disable GeoJSON format in the response.
                Defaults to False.
            disable_disruption (bool, optional): Whether to disable disruption information.
                Defaults to False.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            start_page (int, optional): The starting page for pagination. Defaults to 0.
            count (int, optional): The number of items per page. Defaults to 25.
            add_poi_infos (Sequence[str], optional): Additional POI information to include.
                Defaults to ["bss_stands", "car_park"].

        Returns:
            Tuple[Sequence[Place], Pagination]: A tuple containing a list of nearby Place objects
                and pagination information.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/places_nearby"

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)

    def list_objects_by_region_id_and_coordinates(
        self,
        region_id: str,
        lon: float,
        lat: float,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        """
        Retrieves a list of places nearby based on the region ID and coordinates from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            distance (int, optional): The distance for nearby search. Defaults to 500.
            type (Sequence[str], optional): The types of places to include in the search.
                Defaults to ["stop_area", "stop_point", "poi"].
            admin_uri (Optional[Sequence[str]], optional): The administrative URIs to filter by.
                Defaults to None.
            filter (Optional[str], optional): Additional filtering criteria. Defaults to None.
            disable_geojson (bool, optional): Whether to disable GeoJSON format in the response.
                Defaults to False.
            disable_disruption (bool, optional): Whether to disable disruption information.
                Defaults to False.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            start_page (int, optional): The starting page for pagination. Defaults to 0.
            count (int, optional): The number of items per page. Defaults to 25.
            add_poi_infos (Sequence[str], optional): Additional POI information to include.
                Defaults to ["bss_stands", "car_park"].

        Returns:
            Tuple[Sequence[Place], Pagination]: A tuple containing a list of nearby Place objects
                and pagination information.
        """
        request_url = (
            f"{self.base_navitia_url}/coverage/{region_id}/{lon};{lat}/places_nearby"
        )

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)

    def list_objects_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        """
        Retrieves a list of places nearby based on the provided coordinates from the Navitia API.

        Parameters:
            region_lon (float): The longitude coordinate of the region.
            region_lat (float): The latitude coordinate of the region.
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            distance (int, optional): The distance for nearby search. Defaults to 500.
            type (Sequence[str], optional): The types of places to include in the search.
                Defaults to ["stop_area", "stop_point", "poi"].
            admin_uri (Optional[Sequence[str]], optional): The administrative URIs to filter by.
                Defaults to None.
            filter (Optional[str], optional): Additional filtering criteria. Defaults to None.
            disable_geojson (bool, optional): Whether to disable GeoJSON format in the response.
                Defaults to False.
            disable_disruption (bool, optional): Whether to disable disruption information.
                Defaults to False.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            start_page (int, optional): The starting page for pagination. Defaults to 0.
            count (int, optional): The number of items per page. Defaults to 25.
            add_poi_infos (Sequence[str], optional): Additional POI information to include.
                Defaults to ["bss_stands", "car_park"].

        Returns:
            Tuple[Sequence[Place], Pagination]: A tuple containing a list of nearby Place objects
                and pagination information.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/places_nearby"

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)

    def list_objects_by_object_coordinates_only(
        self,
        lon: float,
        lat: float,
        distance: int = 500,
        type: Sequence[str] = ["stop_area", "stop_point", "poi"],
        admin_uri: Optional[Sequence[str]] = None,
        filter: Optional[str] = None,
        disable_geojson: bool = False,
        disable_disruption: bool = False,
        depth: int = 1,
        start_page: int = 0,
        count: int = 25,
        add_poi_infos: Sequence[str] = ["bss_stands", "car_park"],
    ) -> Tuple[Sequence[Place], Pagination]:
        """
        Retrieves a list of places nearby based on the provided coordinates from the Navitia API.

        Parameters:
            lon (float): The longitude coordinate.
            lat (float): The latitude coordinate.
            distance (int, optional): The distance for nearby search. Defaults to 500.
            type (Sequence[str], optional): The types of places to include in the search.
                Defaults to ["stop_area", "stop_point", "poi"].
            admin_uri (Optional[Sequence[str]], optional): The administrative URIs to filter by.
                Defaults to None.
            filter (Optional[str], optional): Additional filtering criteria. Defaults to None.
            disable_geojson (bool, optional): Whether to disable GeoJSON format in the response.
                Defaults to False.
            disable_disruption (bool, optional): Whether to disable disruption information.
                Defaults to False.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            start_page (int, optional): The starting page for pagination. Defaults to 0.
            count (int, optional): The number of items per page. Defaults to 25.
            add_poi_infos (Sequence[str], optional): Additional POI information to include.
                Defaults to ["bss_stands", "car_park"].

        Returns:
            Tuple[Sequence[Place], Pagination]: A tuple containing a list of nearby Place objects
                and pagination information.
        """
        request_url = f"{self.base_navitia_url}/coverage/{lon};{lat}/places_nearby"

        if not request_url:
            raise ValueError(
                "Region id, region coordinates or coordinates must be provided."
            )

        filters = {
            "start_page": start_page,
            "count": count,
            "depth": depth,
            "type[]": type,
            "distance": distance,
            "disable_geojson": disable_geojson,
            "disable_disruption": disable_disruption,
            "add_poi_infos[]": add_poi_infos,
        }

        if admin_uri:
            filters["admin_uris[]"] = admin_uri

        if filter:
            filters["filter"] = filter

        return self._get_places_nearby(request_url, filters)
