from dataclasses import dataclass

from navitia_client.client.apis.arrival_apis import ArrivalApiClient
from navitia_client.client.apis.contributors_apis import ContributorsApiClient
from navitia_client.client.apis.coverage_apis import CoverageApiClient
from navitia_client.client.apis.datasets_apis import DatasetsApiClient
from navitia_client.client.apis.departure_apis import DepartureApiClient
from navitia_client.client.apis.inverted_geocoding_apis import (
    InvertedGeocodingApiClient,
)
from navitia_client.client.apis.isochrone_apis import IsochronesApiClient
from navitia_client.client.apis.journeys_apis import JourneyApiClient
from navitia_client.client.apis.line_report_apis import LineReportsApiClient
from navitia_client.client.apis.place_apis import PlacesApiClient
from navitia_client.client.apis.places_nearby_apis import PlacesNearbyApiClient
from navitia_client.client.apis.public_transport_objects_apis import (
    PublicTransportObjectsApiClient,
)
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
from navitia_client.client.apis.route_schedules_apis import RouteSchedulesApiClient
from navitia_client.client.apis.stop_schedules_apis import StopSchedulesApiClient
from navitia_client.client.apis.terminus_schedules_apis import (
    TerminusSchedulesApiClient,
)
from navitia_client.client.apis.traffic_report_apis import TrafficReportsApiClient
from navitia_client.client.raw.raw_client import RawClient

BASE_NAVITIA_URL: str = "https://api.navitia.io/v1/"


@dataclass
class NavitiaClient:
    """
    Navitia API client for accessing various endpoints.

    Attributes
    ----------
    auth_token : str
        Authorization token for accessing the API.
    base_navitia_url : str
        Base URL of the Navitia API.

    Methods
    -------
    coverage -> CoverageApiClient:
        Get an instance of CoverageApiClient for accessing coverage-related endpoints.
    datasets -> DatasetsApiClient:
        Get an instance of DatasetsApiClient for accessing dataset-related endpoints.
    contributors -> ContributorsApiClient:
        Get an instance of ContributorsApiClient for accessing contributor-related endpoints.
    networks -> NetworkApiClient:
        Get an instance of NetworkApiClient for accessing network-related endpoints.
    companies -> CompanyApiClient:
        Get an instance of CompanyApiClient for accessing company-related endpoints.
    commercial_modes -> CommercialModeApiClient:
        Get an instance of CommercialModeApiClient for accessing commercial mode-related endpoints.
    physical_modes -> PhysicalModeApiClient:
        Get an instance of PhysicalModeApiClient for accessing physical mode-related endpoints.
    stop_areas -> StopAreaApiClient:
        Get an instance of StopAreaApiClient for accessing stop area-related endpoints.
    stop_points -> StopPointApiClient:
        Get an instance of StopPointApiClient for accessing stop point-related endpoints.
    lines -> LineApiClient:
        Get an instance of LineApiClient for accessing line-related endpoints.
    routes -> RouteApiClient:
        Get an instance of RouteApiClient for accessing route-related endpoints.
    disruptions -> DisruptionApiClient:
        Get an instance of DisruptionApiClient for accessing disruption-related endpoints.
    vehicle_journeys -> VehicleJourneyApiClient:
        Get an instance of VehicleJourneyApiClient for accessing vehicle journey-related endpoints.
    pt_objects -> PublicTransportObjectsApiClient:
        Get an instance of PublicTransportObjectsApiClient for accessing public transport object-related endpoints.
    places -> PlacesApiClient:
        Get an instance of PlacesApiClient for accessing places-related endpoints.
    places_nearby -> PlacesNearbyApiClient:
        Get an instance of PlacesNearbyApiClient for accessing nearby places-related endpoints.
    inverted_geocoding -> InvertedGeocodingApiClient:
        Get an instance of InvertedGeocodingApiClient for accessing inverted geocoding-related endpoints.
    route_schedules -> RouteSchedulesApiClient:
        Get an instance of RouteSchedulesApiClient for accessing route schedules-related endpoints.
    stop_schedules -> StopSchedulesApiClient:
        Get an instance of StopSchedulesApiClient for accessing stop schedules-related endpoints.
    terminus_schedules -> TerminusSchedulesApiClient:
        Get an instance of TerminusSchedulesApiClient for accessing terminus schedules-related endpoints.
    departures -> DepartureApiClient:
        Get an instance of DepartureApiClient for accessing departure-related endpoints.
    arrivals -> ArrivalApiClient:
        Get an instance of ArrivalApiClient for accessing arrival-related endpoints.
    line_reports -> LineReportsApiClient:
        Get an instance of LineReportsApiClient for accessing line reports-related endpoints.
    traffic_reports -> TrafficReportsApiClient:
        Get an instance of TrafficReportsApiClient for accessing traffic reports-related endpoints.
    journeys -> JourneyApiClient:
        Get an instance of JourneyApiClient for accessing journey-related endpoints.
    isochrones -> IsochronesApiClient:
        Get an instance of IsochronesApiClient for accessing isochrone-related endpoints.
    """

    auth_token: str
    base_navitia_url: str = BASE_NAVITIA_URL

    @property
    def coverage(self) -> CoverageApiClient:
        """Get an instance of CoverageApiClient for accessing coverage-related endpoints."""
        return CoverageApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def datasets(self) -> DatasetsApiClient:
        """Get an instance of DatasetsApiClient for accessing dataset-related endpoints."""
        return DatasetsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def contributors(self) -> ContributorsApiClient:
        """Get an instance of ContributorsApiClient for accessing contributor-related endpoints."""
        return ContributorsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def networks(self) -> NetworkApiClient:
        """Get an instance of NetworkApiClient for accessing network-related endpoints."""
        return NetworkApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def companies(self) -> CompanyApiClient:
        """Get an instance of CompanyApiClient for accessing company-related endpoints."""
        return CompanyApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def commercial_modes(self) -> CommercialModeApiClient:
        """Get an instance of CommercialModeApiClient for accessing commercial mode-related endpoints."""
        return CommercialModeApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def physical_modes(self) -> PhysicalModeApiClient:
        """Get an instance of PhysicalModeApiClient for accessing physical mode-related endpoints."""
        return PhysicalModeApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def stop_areas(self) -> StopAreaApiClient:
        """Get an instance of StopAreaApiClient for accessing stop area-related endpoints."""
        return StopAreaApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def stop_points(self) -> StopPointApiClient:
        """Get an instance of StopPointApiClient for accessing stop point-related endpoints."""
        return StopPointApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def lines(self) -> LineApiClient:
        """Get an instance of LineApiClient for accessing line-related endpoints."""
        return LineApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def routes(self) -> RouteApiClient:
        """Get an instance of RouteApiClient for accessing route-related endpoints."""
        return RouteApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def disruptions(self) -> DisruptionApiClient:
        """Get an instance of DisruptionApiClient for accessing disruption-related endpoints."""
        return DisruptionApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def vehicle_journeys(self) -> VehicleJourneyApiClient:
        """Get an instance of VehicleJourneyApiClient for accessing vehicle-related endpoints."""
        return VehicleJourneyApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def pt_objects(self) -> PublicTransportObjectsApiClient:
        """Get an instance of PublicTransportObjectsApiClient for accessing public-transport-related endpoints."""
        return PublicTransportObjectsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def places(self) -> PlacesApiClient:
        """Get an instance of PlacesApiClient for accessing places-related endpoints"""
        return PlacesApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def places_nearby(self) -> PlacesNearbyApiClient:
        """Get an instance of PlacesNearbyApiClient for accessing nearby-places-related endpoints."""
        return PlacesNearbyApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def inverted_geocoding(self) -> InvertedGeocodingApiClient:
        """Get an instance of InvertedGeocodingApiClient for accessing inverted-geocoding-related endpoints."""
        return InvertedGeocodingApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def route_schedules(self) -> RouteSchedulesApiClient:
        """Get an instance of RouteSchedulesApiClient for accessing routes-related endpoints."""
        return RouteSchedulesApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def stop_schedules(self) -> StopSchedulesApiClient:
        """Get an instance of StopSchedulesApiClient for accessing stop-schedules-related endpoints."""
        return StopSchedulesApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def terminus_schedules(self) -> TerminusSchedulesApiClient:
        """Get an instance of TerminusSchedulesApiClient for accessing terminate-schedules-related endpoints."""
        return TerminusSchedulesApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def departures(self) -> DepartureApiClient:
        """Get an instance of DepartureApiClient for accessing departures-related endpoints."""
        return DepartureApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def arrivals(self) -> ArrivalApiClient:
        """Get an instance of ArrivalApiClient for accessing arrivals-related endpoints."""
        return ArrivalApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def line_reports(self) -> LineReportsApiClient:
        """Get an instance of LineReportsApiClient for accessing line-reports-related endpoints."""
        return LineReportsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def traffic_reports(self) -> TrafficReportsApiClient:
        """Get an instance of TrafficReportsApiClient for accessing traffic-reports-related endpoints."""
        return TrafficReportsApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def journeys(self) -> JourneyApiClient:
        """Get an instance of JourneyApiClient for accessing journey-related endpoints."""
        return JourneyApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def isochrones(self) -> IsochronesApiClient:
        """Get an instance of IsochronesApiClient for accessing isochrones-related endpoints."""
        return IsochronesApiClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )

    @property
    def raw(self) -> RawClient:
        """Get an instance of RawClient for accessing APIs and get raw response"""
        return RawClient(
            auth_token=self.auth_token, base_navitia_url=self.base_navitia_url
        )
