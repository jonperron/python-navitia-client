import pytest
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
from navitia_client.client.navitia_client import NavitiaClient


@pytest.fixture
def navitia_client():
    auth_token = "test_token"
    base_navitia_url = "http://api.navitia.io/v1/"
    return NavitiaClient(auth_token=auth_token, base_navitia_url=base_navitia_url)


def test_coverage_client(navitia_client):
    assert isinstance(navitia_client.coverage, CoverageApiClient)


def test_datasets_client(navitia_client):
    assert isinstance(navitia_client.datasets, DatasetsApiClient)


def test_contributors_client(navitia_client):
    assert isinstance(navitia_client.contributors, ContributorsApiClient)


def test_networks_client(navitia_client):
    assert isinstance(navitia_client.networks, NetworkApiClient)


def test_companies_client(navitia_client):
    assert isinstance(navitia_client.companies, CompanyApiClient)


def test_commercial_modes_client(navitia_client):
    assert isinstance(navitia_client.commercial_modes, CommercialModeApiClient)


def test_physical_modes_client(navitia_client):
    assert isinstance(navitia_client.physical_modes, PhysicalModeApiClient)


def test_stop_areas_client(navitia_client):
    assert isinstance(navitia_client.stop_areas, StopAreaApiClient)


def test_stop_points_client(navitia_client):
    assert isinstance(navitia_client.stop_points, StopPointApiClient)


def test_lines_client(navitia_client):
    assert isinstance(navitia_client.lines, LineApiClient)


def test_routes_client(navitia_client):
    assert isinstance(navitia_client.routes, RouteApiClient)


def test_disruptions_client(navitia_client):
    assert isinstance(navitia_client.disruptions, DisruptionApiClient)


def test_vehicle_journeys_client(navitia_client):
    assert isinstance(navitia_client.vehicle_journeys, VehicleJourneyApiClient)


def test_pt_objects_client(navitia_client):
    assert isinstance(navitia_client.pt_objects, PublicTransportObjectsApiClient)


def test_places_client(navitia_client):
    assert isinstance(navitia_client.places, PlacesApiClient)


def test_places_nearby_client(navitia_client):
    assert isinstance(navitia_client.places_nearby, PlacesNearbyApiClient)


def test_inverted_geocoding_client(navitia_client):
    assert isinstance(navitia_client.inverted_geocoding, InvertedGeocodingApiClient)


def test_route_schedules_client(navitia_client):
    assert isinstance(navitia_client.route_schedules, RouteSchedulesApiClient)


def test_stop_schedules_client(navitia_client):
    assert isinstance(navitia_client.stop_schedules, StopSchedulesApiClient)


def test_terminus_schedules_client(navitia_client):
    assert isinstance(navitia_client.terminus_schedules, TerminusSchedulesApiClient)


def test_departures_client(navitia_client):
    assert isinstance(navitia_client.departures, DepartureApiClient)


def test_arrivals_client(navitia_client):
    assert isinstance(navitia_client.arrivals, ArrivalApiClient)


def test_line_reports_client(navitia_client):
    assert isinstance(navitia_client.line_reports, LineReportsApiClient)


def test_traffic_reports_client(navitia_client):
    assert isinstance(navitia_client.traffic_reports, TrafficReportsApiClient)


def test_journeys_client(navitia_client):
    assert isinstance(navitia_client.journeys, JourneyApiClient)


def test_isochrones_client(navitia_client):
    assert isinstance(navitia_client.isochrones, IsochronesApiClient)


def test_raw_client(navitia_client):
    assert isinstance(navitia_client.raw, RawClient)
