from typing import Any, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.request.public_transport_object import (
    PublicTransportObjectRequest,
)
from navitia_client.entities.response.pt_object import PtObject


class PublicTransportObjectsApiClient(ApiBaseClient):
    """Client class to interact with the Navitia API for fetching public transport objects.

    See https://doc.navitia.io/#pt-objects
    """

    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[PtObject]:
        """Transform raw API response data into a list of PtObject objects.

        Args:
            response: The raw API response data.

        Returns:
            A sequence of PtObject objects.
        """
        pt_objects = []
        for pt_objects_data in response:
            pt_objects.append(PtObject.from_payload(pt_objects_data))

        return pt_objects

    def list_public_transport_objects(
        self,
        region_id: str,
        request: PublicTransportObjectRequest,
    ) -> Sequence[PtObject]:
        """Retrieve a list of public transport objects for a specified region.

        Args:
            region_id: The region ID.
            request: The request object containing query parameters.

        Returns:
            A sequence of PtObject objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/pt_objects"
        results = self.get_navitia_api(
            request_url + self._generate_filter_query(request.to_filters())
        )
        raw_results = results.json()["pt_objects"]
        return self._get_pt_objects_from_response(raw_results)
