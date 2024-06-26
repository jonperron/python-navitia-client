import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.stop_schedules_apis import (
    StopSchedulesApiClient,
)
from navitia_client.entities.stop_schedule import StopSchedule


@pytest.fixture
def stop_schedules_apis():
    return StopSchedulesApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(StopSchedulesApiClient, "get_navitia_api")
def test_list_objects_by_region_id_and_path(
    mock_get_navitia_api: MagicMock, stop_schedules_apis: StopSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/stop_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    stop_schedules, _ = stop_schedules_apis.list_stop_schedules_by_region_id_and_path(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(stop_schedules) == 1
    assert isinstance(stop_schedules[0], StopSchedule)


@patch.object(StopSchedulesApiClient, "get_navitia_api")
def test_list_objects_by_coordinates(
    mock_get_navitia_api: MagicMock, stop_schedules_apis: StopSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/stop_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    stop_schedules, _ = stop_schedules_apis.list_stop_schedules_by_coordinates(
        region_lon=1.1, region_lat=1.2, lon=2.1, lat=2.2
    )

    # Then
    assert len(stop_schedules) == 1
    assert isinstance(stop_schedules[0], StopSchedule)
