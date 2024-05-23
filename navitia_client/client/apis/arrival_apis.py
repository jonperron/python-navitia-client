from datetime import datetime
from typing import Any, Optional, Sequence, Tuple
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.pagination import Pagination
from navitia_client.entities.arrival import Arrival


class ArrivalApiClient(ApiBaseClient):
    @staticmethod
    def _get_departure_objects_from_response(
        response: Any,
    ) -> Sequence[Arrival]:
        arrivals = []
        for arrival_data in response:
            arrivals.append(Arrival.from_payload(arrival_data))

        return arrivals

    def _get_departures(
        self, url: str, filters: dict
    ) -> Tuple[Sequence[Arrival], Pagination]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        raw_results = results.json()["arrivals"]
        pagination = Pagination.from_payload(results.json()["pagination"])
        return self._get_departure_objects_from_response(raw_results), pagination

    def list_arrivals_by_region_id_and_path(
        self,
        region_id: str,
        resource_path: str,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[Arrival], Pagination]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/{resource_path}/terminus_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_departures(request_url, filters)

    def list_arrivals_by_coordinates(
        self,
        region_lon: float,
        region_lat: float,
        lon: float,
        lat: float,
        from_datetime: datetime = datetime.now(),
        duration: int = 86400,
        depth: int = 1,
        forbidden_uris: Optional[Sequence[str]] = None,
        data_freshness: str = "realtime",
        disable_geojson: bool = False,
        direction_type: str = "all",
    ) -> Tuple[Sequence[Arrival], Pagination]:
        # List of objects near the resource, navitia guesses the region from coordinates
        request_url = f"{self.base_navitia_url}/coverage/{region_lon};{region_lat}/coords/{lon};{lat}/terminus_schedules"

        filters = {
            "from_datetime": from_datetime,
            "duration": duration,
            "depth": depth,
            "disable_geojson": disable_geojson,
            "forbidden_uris[]": forbidden_uris,
            "data_freshness": data_freshness,
            "direction_type": direction_type,
        }

        return self._get_departures(request_url, filters)
