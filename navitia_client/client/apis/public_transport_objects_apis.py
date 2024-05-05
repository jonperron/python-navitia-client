from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pt_object import PtObject


class PublicTransportObjectsApiClient(ApiBaseClient):
    @staticmethod
    def _get_pt_objects_from_response(response: Any) -> Sequence[PtObject]:
        pt_objects = []
        for pt_objects_data in response:
            pt_objects.append(PtObject.from_json(pt_objects_data))

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
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/pt_objects?q={query}&type={type}&disable_disruption={disable_disruption}&depth={depth}"
        if post_query_filter:
            request_url += f"&filter={post_query_filter}"

        results = self.get_navitia_api(request_url)
        raw_results = results.json()["pt_objects"]
        return self._get_pt_objects_from_response(raw_results)
