from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pt_object import PtObject


class PublicTransportObjectsApiClient(ApiBaseClient):
    """
    A client class to interact with the Navitia API for fetching public transport objects.

    See https://doc.navitia.io/#pt-objects

    Methods
    -------
    _get_pt_objects_from_response(response: Any) -> Sequence[PtObject]:
        A static method to transform raw API response data into a list of PtObject objects.

    list_public_transport_objects(
        region_id: str,
        query: str,
        type: Sequence[str] = [
            "network",
            "commercial_mode",
            "line",
            "route",
            "stop_area",
        ],
        disable_disruption: bool = False,
        depth: int = 1,
        post_query_filter: Optional[str] = None,
    ) -> Sequence[PtObject]:
        Retrieves a list of public transport objects for a specified region from the Navitia API.
    """

    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[PtObject]:
        """
        Static method to transform raw API response data into a list of PtObject objects.

        Parameters:
            response (Any): The raw API response data.

        Returns:
            Sequence[PtObject]: A sequence of PtObject objects.
        """
        pt_objects = []
        for pt_objects_data in response:
            pt_objects.append(PtObject.from_payload(pt_objects_data))

        return pt_objects

    def list_public_transport_objects(
        self,
        region_id: str,
        query: str,
        type: Sequence[str] = [
            "network",
            "commercial_mode",
            "line",
            "route",
            "stop_area",
        ],
        disable_disruption: bool = False,
        depth: int = 1,
        post_query_filter: Optional[str] = None,
    ) -> Sequence[PtObject]:
        """
        Retrieves a list of public transport objects for a specified region from the Navitia API.

        Parameters:
            region_id (str): The region ID.
            query (str): The search query.
            type (Sequence[str], optional): The types of public transport objects to include
                in the search. Defaults to ["network", "commercial_mode", "line", "route", "stop_area"].
            disable_disruption (bool, optional): Whether to disable disruption information in the response.
                Defaults to False.
            depth (int, optional): The depth of data to retrieve. Defaults to 1.
            post_query_filter (Optional[str], optional): Additional filtering criteria. Defaults to None.

        Returns:
            Sequence[PtObject]: A sequence of PtObject objects.
        """
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/pt_objects?q={query}&type={type}&disable_disruption={disable_disruption}&depth={depth}"
        if post_query_filter:
            request_url += f"&filter={post_query_filter}"

        results = self.get_navitia_api(request_url)
        raw_results = results.json()["pt_objects"]
        return self._get_pt_objects_from_response(raw_results)
