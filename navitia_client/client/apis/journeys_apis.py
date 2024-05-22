from datetime import datetime
from typing import Any, Optional, Sequence
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.journey import Journey


class JourneyApiClient(ApiBaseClient):
    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string regarding provided filters"""
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def _get_journeys(self, url: str, filters: dict) -> Sequence[Journey]:
        results = self.get_navitia_api(url + self._generate_filter_query(filters))
        journeys = [Journey.from_payload(data) for data in results.json()["journeys"]]
        return journeys

    def list_journeys(
        self,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Sequence[str] = [],
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0,
    ) -> Sequence[Journey]:
        request_url = f"{self.base_navitia_url}/journeys"

        filters = {
            "datetime": datetime_.isoformat(),
            "datetime_represents": datetime_represents,
            "traveler_type": traveler_type,
            "data_freshness": data_freshness,
            "language": language,
            "depth": depth,
            "max_duration_to_pt": max_duration_to_pt,
            "walking_speed": walking_speed,
            "bike_speed": bike_speed,
            "bss_speed": bss_speed,
            "car_speed": car_speed,
            "min_nb_journeys": min_nb_journeys,
            "max_nb_journeys": max_nb_journeys,
            "count": count,
            "max_nb_transfers": max_nb_transfers,
            "min_nb_transfers": min_nb_transfers,
            "max_duration": max_duration,
            "wheelchair": wheelchair,
            "direct_path": direct_path,
            "add_poi_infos[]": add_poi_infos,
            "debug": debug,
            "free_radius_from": free_radius_from,
            "free_radius_to": free_radius_to,
            "timeframe_duration": timeframe_duration,
        }

        if from_:
            filters["from"] = from_

        if to_:
            filters["to"] = to_

        if forbidden_uris:
            filters["forbidden_uris[]"] = forbidden_uris

        if allowed_id:
            filters["allowed_id[]"] = allowed_id

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if any([direct_path_mode, first_section_mode]):
            filters["direct_path_mode[]"] = direct_path_mode or first_section_mode

        return self._get_journeys(request_url, filters)

    def list_journeys_with_region_id(
        self,
        region_id: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Sequence[str] = [],
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0,
    ) -> Sequence[Journey]:
        request_url = f"{self.base_navitia_url}/coverage/{region_id}/journeys"

        filters = {
            "datetime": datetime_.isoformat(),
            "datetime_represents": datetime_represents,
            "traveler_type": traveler_type,
            "data_freshness": data_freshness,
            "language": language,
            "depth": depth,
            "max_duration_to_pt": max_duration_to_pt,
            "walking_speed": walking_speed,
            "bike_speed": bike_speed,
            "bss_speed": bss_speed,
            "car_speed": car_speed,
            "min_nb_journeys": min_nb_journeys,
            "max_nb_journeys": max_nb_journeys,
            "count": count,
            "max_nb_transfers": max_nb_transfers,
            "min_nb_transfers": min_nb_transfers,
            "max_duration": max_duration,
            "wheelchair": wheelchair,
            "direct_path": direct_path,
            "add_poi_infos[]": add_poi_infos,
            "debug": debug,
            "free_radius_from": free_radius_from,
            "free_radius_to": free_radius_to,
            "timeframe_duration": timeframe_duration,
        }

        if from_:
            filters["from"] = from_

        if to_:
            filters["to"] = to_

        if forbidden_uris:
            filters["forbidden_uris[]"] = forbidden_uris

        if allowed_id:
            filters["allowed_id[]"] = allowed_id

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if any([direct_path_mode, first_section_mode]):
            filters["direct_path_mode[]"] = direct_path_mode or first_section_mode

        return self._get_journeys(request_url, filters)

    def list_journeys_with_resource_path(
        self,
        resource_path: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Sequence[str] = [],
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0,
    ) -> Sequence[Journey]:
        request_url = f"{self.base_navitia_url}/coverage/{resource_path}/journeys"

        filters = {
            "datetime": datetime_.isoformat(),
            "datetime_represents": datetime_represents,
            "traveler_type": traveler_type,
            "data_freshness": data_freshness,
            "language": language,
            "depth": depth,
            "max_duration_to_pt": max_duration_to_pt,
            "walking_speed": walking_speed,
            "bike_speed": bike_speed,
            "bss_speed": bss_speed,
            "car_speed": car_speed,
            "min_nb_journeys": min_nb_journeys,
            "max_nb_journeys": max_nb_journeys,
            "count": count,
            "max_nb_transfers": max_nb_transfers,
            "min_nb_transfers": min_nb_transfers,
            "max_duration": max_duration,
            "wheelchair": wheelchair,
            "direct_path": direct_path,
            "add_poi_infos[]": add_poi_infos,
            "debug": debug,
            "free_radius_from": free_radius_from,
            "free_radius_to": free_radius_to,
            "timeframe_duration": timeframe_duration,
        }

        if from_:
            filters["from"] = from_

        if to_:
            filters["to"] = to_

        if forbidden_uris:
            filters["forbidden_uris[]"] = forbidden_uris

        if allowed_id:
            filters["allowed_id[]"] = allowed_id

        if first_section_mode:
            filters["first_section_mode[]"] = first_section_mode

        if last_section_mode:
            filters["last_section_mode[]"] = last_section_mode

        if any([direct_path_mode, first_section_mode]):
            filters["direct_path_mode[]"] = direct_path_mode or first_section_mode

        return self._get_journeys(request_url, filters)
