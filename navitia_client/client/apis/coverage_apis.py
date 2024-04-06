from datetime import datetime
from typing import Any, Sequence

from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.entities.administrative_region import Region


class CoverageApiClient(ApiBaseClient):
    @staticmethod
    def _get_regions_from_response(raw_regions_response: Any) -> Sequence[Region]:
        regions = []
        for region in raw_regions_response:
            regions.append(
                Region(
                    id=region.get("id"),
                    name=region.get("name"),
                    dataset_created_at=datetime.fromisoformat(
                        region.get("dataset_created_at")
                    )
                    if region.get("dataset_created_at")
                    else None,
                    end_production_date=datetime.strptime(
                        region.get("end_production_date"), "%Y%m%d"
                    )
                    if region.get("end_production_date")
                    else None,
                    last_load_at=datetime.fromisoformat(region.get("last_load_at"))
                    if region.get("last_load_at")
                    else None,
                    shape=region.get("shape"),
                    start_production_date=datetime.strptime(
                        region.get("start_production_date"), "%Y%m%d"
                    )
                    if region.get("end_production_date")
                    else None,
                    status=region.get("status"),
                )
            )
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
        results = self.get_navitia_api(
            f"{self.base_navitia_url}/coverage/"
            + "{"
            + "{0};{1}".format(lon, lat)
            + "}"
        )
        result_regions = results.json()["regions"]
        regions = CoverageApiClient._get_regions_from_response(result_regions)

        return regions
