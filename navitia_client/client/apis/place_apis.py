from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.place import PlaceRequest
from navitia_client.entities.response.place import Place


class PlacesApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching place information.

    See https://doc.navitia.io/#places
    """

    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[Place]:
        """Transform raw API response data into a list of Place objects.

        Args:
            response: The raw API response data.

        Returns:
            A list of Place objects.
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
        """Retrieve a list of places based on the provided query and region ID.

        Args:
            region_id: The region ID.
            request: The request object containing query parameters.

        Returns:
            A list of Place objects matching the query.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/places"
        results = self.get_navitia_api(
            request_url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["places"]
        return self._get_pt_objects_from_response(raw_results)
