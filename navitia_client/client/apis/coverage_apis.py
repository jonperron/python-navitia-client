from typing import Any, Sequence

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.administrative_region import Region


class CoverageApiClient(ApiBaseClient):
    @staticmethod
    def _get_regions_from_response(raw_regions_response: Any) -> Sequence[Region]:
        regions = []
        for region_data in raw_regions_response:
            regions.append(Region.from_json(region_data))
        return regions

    def list_covered_areas(self) -> Sequence[Region]:
        results = self.get_navitia_api(f"{self.base_navitia_url}/coverage")
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)
        return regions

    def get_region_by_id(self, region_id: str) -> Sequence[Region]:
        results = self.get_navitia_api(f"{self.base_navitia_url}/coverage/{region_id}")
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)

        return regions

    def get_region_by_coordinates(self, lon: float, lat: float) -> Sequence[Region]:
        results = self.get_navitia_api(f"{self.base_navitia_url}/coverage/{lon};{lat}")
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)

        return regions
