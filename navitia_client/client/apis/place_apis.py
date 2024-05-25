from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.place import Place


class PlacesApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching place information.

    See https://doc.navitia.io/#places

    Methods
    -------
    _get_pt_objects_from_response(response: Any) -> Sequence[Place]
        A static method to transform raw API response data into a list of Place objects.

    list_places(
        region_id: str, query: str,
        type: Sequence[str] = ["stop_area", "address", "poi", "administrative_region"],
        disable_geojson: bool = False, depth: int = 1,
        from_lon_lat: Optional[Tuple[float, float]] = None
    ) -> Sequence[Place]
        Retrieves a list of places based on the provided query and region ID from the Navitia API.
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

    def list_places(
        self,
        region_id: str,
        query: str,
        type: Sequence[str] = ["stop_area", "address", "poi", "administrative_region"],
        disable_geojson: bool = False,
        depth: int = 1,
        from_lon_lat: Optional[Tuple[float, float]] = None,
    ) -> Sequence[Place]:
        """
        Retrieves a list of places based on the provided query and region ID from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            query (str): The query string to search for places.
            type (Sequence[str], optional): The types of places to include in the search.
                Defaults to ["stop_area", "address", "poi", "administrative_region"].
            disable_geojson (bool, optional): Whether to disable GeoJSON format in the response.
                Defaults to False.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            from_lon_lat (Optional[Tuple[float, float]], optional): The longitude and latitude
                from which to search for places. Defaults to None.

        Returns:
            Sequence[Place]: A list of Place objects matching the query.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/places?q={query}&type={type}&disable_geojson={disable_geojson}&depth={depth}"
        if from_lon_lat:
            request_url += f"&filter={from_lon_lat[0]};{from_lon_lat[1]}"

        results = self.get_navitia_api(request_url)
        raw_results = results.json()["places"]
        return self._get_pt_objects_from_response(raw_results)
