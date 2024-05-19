from typing import Any, Sequence, Tuple

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.administrative_region import Region
from navitia_client.entities.pagination import Pagination


class CoverageApiClient(ApiBaseClient):
    @staticmethod
    def _get_regions_from_response(raw_regions_response: Any) -> Sequence[Region]:
        regions = []
        for region_data in raw_regions_response:
            regions.append(Region.from_payload(region_data))
        return regions

    def list_covered_areas(
        self, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Region], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage?start_page={start_page}&count={count}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        pagination = Pagination.from_payload(results.json()["pagination"])
        return regions, pagination

    def get_region_by_id(
        self, region_id: str, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Region], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{region_id}?start_page={start_page}&count={count}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        pagination = Pagination.from_payload(results.json()["pagination"])
        return regions, pagination

    def get_region_by_coordinates(
        self, lon: float, lat: float, start_page: int = 0, count: int = 25
    ) -> Tuple[Sequence[Region], Pagination]:
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/{lon};{lat}?start_page={start_page}&count={count}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        pagination = Pagination.from_payload(results.json()["pagination"])
        return regions, pagination
