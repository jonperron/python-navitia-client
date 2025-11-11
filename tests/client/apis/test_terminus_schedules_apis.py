import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.terminus_schedules_apis import (
    TerminusSchedulesApiClient,
)
from navitia_client.entities.request.terminus_schedule import TerminusScheduleRequest
from navitia_client.entities.response.stop_schedule import TerminusSchedule


@pytest.fixture
def terminus_schedules_apis():
    return TerminusSchedulesApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(TerminusSchedulesApiClient, "get_navitia_api")
def test_list_objects_by_region_id_and_path(
    mock_get_navitia_api: MagicMock, terminus_schedules_apis: TerminusSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/terminus_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response
    request = TerminusScheduleRequest()

    # When
    terminus_schedules, _ = (
        terminus_schedules_apis.list_terminus_schedules_by_region_id_and_path(
            region_id="bar", resource_path="foo:bar:fuzz", request=request
        )
    )

    # Then
    assert len(terminus_schedules) == 2
    assert isinstance(terminus_schedules[0], TerminusSchedule)


@patch.object(TerminusSchedulesApiClient, "get_navitia_api")
def test_list_objects_by_coordinates(
    mock_get_navitia_api: MagicMock, terminus_schedules_apis: TerminusSchedulesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/terminus_schedules.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response
    request = TerminusScheduleRequest()

    # When
    terminus_schedules, _ = (
        terminus_schedules_apis.list_terminus_schedules_by_coordinates(
            region_lon=1.1, region_lat=1.2, lon=2.1, lat=2.2, request=request
        )
    )

    # Then
    assert len(terminus_schedules) == 2
    assert isinstance(terminus_schedules[0], TerminusSchedule)
