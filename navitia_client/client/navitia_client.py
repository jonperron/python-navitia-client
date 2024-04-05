from dataclasses import dataclass
from navitia_client.client.apis.coverage_apis import CoverageApiClient

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
