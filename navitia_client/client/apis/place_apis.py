from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.place import PlaceRequest
from navitia_client.entities.response.place import Place


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
        request: PlaceRequest,
    ) -> Sequence[Place]:
        """
        Retrieves a list of places based on the provided query and region ID from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            request (PlaceRequest): The request object containing query parameters.

        Returns:
            Sequence[Place]: A list of Place objects matching the query.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/places"
        results = self.get_navitia_api(
            request_url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["places"]
        return self._get_pt_objects_from_response(raw_results)
