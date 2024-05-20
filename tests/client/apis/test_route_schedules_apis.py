import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.route_schedules_apis import (
    RouteSchedulesApiClient,
)
from navitia_client.entities.route_schedule import RouteSchedule


@pytest.fixture
def route_schedules_apis():
    return RouteSchedulesApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(RouteSchedulesApiClient, "get_navitia_api")
def test_list_objects_by_region_id_and_path(
    mock_get_navitia_api: MagicMock, route_schedules_apis: RouteSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/route_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    route_schedules = route_schedules_apis.list_route_schedules_by_region_id_and_path(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(route_schedules) == 1
    assert isinstance(route_schedules[0], RouteSchedule)


@patch.object(RouteSchedulesApiClient, "get_navitia_api")
def test_list_objects_by_coordinates(
    mock_get_navitia_api: MagicMock, route_schedules_apis: RouteSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/route_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    route_schedules = route_schedules_apis.list_route_schedules_by_coordinates(
        region_lon=1.1, region_lat=1.2, lon=2.1, lat=2.2
    )

    # Then
    assert len(route_schedules) == 1
    assert isinstance(route_schedules[0], RouteSchedule)
