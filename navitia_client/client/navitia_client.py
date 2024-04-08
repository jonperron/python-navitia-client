from dataclasses import dataclass

from navitia_client.client.apis.contributors_apis import ContributorsApiClient
from navitia_client.client.apis.coverage_apis import CoverageApiClient
from navitia_client.client.apis.datasets_apis import DatasetsApiClient
from navitia_client.client.apis.public_transportation_apis import (
    CommercialModeApiClient,
    CompanyApiClient,
    DisruptionApiClient,
    LineApiClient,
    NetworkApiClient,
    PhysicalModeApiClient,
    RouteApiClient,
    StopAreaApiClient,
    VehicleJourneyApiClient,
)
from navitia_client.client.apis.public_transportation_apis.stop_point_apis import (
    StopPointApiClient,
)

BASE_NAVITIA_URL: str = "https://api.navitia.io/v1/"


@dataclass
class NavitiaClient:
    auth_token: str
    base_navitia_url: str = BASE_NAVITIA_URL

    @property
    def coverage(self) -> CoverageApiClient:
        return CoverageApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def datasets(self) -> DatasetsApiClient:
        return DatasetsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def contributors(self) -> ContributorsApiClient:
        return ContributorsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def networks(self) -> NetworkApiClient:
        return NetworkApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def companies(self) -> CompanyApiClient:
        return CompanyApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def commercial_modes(self) -> CommercialModeApiClient:
        return CommercialModeApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def physical_modes(self) -> PhysicalModeApiClient:
        return PhysicalModeApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def stop_areas(self) -> StopAreaApiClient:
        return StopAreaApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def stop_points(self) -> StopPointApiClient:
        return StopPointApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def lines(self) -> LineApiClient:
        return LineApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def routes(self) -> RouteApiClient:
        return RouteApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def disruptions(self) -> DisruptionApiClient:
        return DisruptionApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def vehicle_journeys(self) -> VehicleJourneyApiClient:
        return VehicleJourneyApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )
