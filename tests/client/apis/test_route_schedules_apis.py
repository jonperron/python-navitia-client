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
def test_list_objects(
    mock_get_navitia_api: MagicMock, route_schedules_apis: RouteSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/route_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    route_schedules = route_schedules_apis.list_route_schedules(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(route_schedules) == 1
    assert isinstance(route_schedules[0], RouteSchedule)


@patch.object(RouteSchedulesApiClient, "get_navitia_api")
def test_raise_on_missing_region_coordinates(
    mock_get_navitia_api: MagicMock, route_schedules_apis: RouteSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get_navitia_api.return_value = mock_response

    # When/Then
    with pytest.raises(ValueError):
        route_schedules_apis.list_route_schedules(
            region_id="bar",
        )
