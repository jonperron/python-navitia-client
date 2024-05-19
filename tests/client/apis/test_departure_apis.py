import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.departure_apis import (
    DepartureApiClient,
)
from navitia_client.entities.departure import Departure


@pytest.fixture
def departure_apis():
    return DepartureApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(DepartureApiClient, "get_navitia_api")
def test_list_objects(
    mock_get_navitia_api: MagicMock, departure_apis: DepartureApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/departures.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    terminus_schedules, _ = departure_apis.list_departures(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(terminus_schedules) == 10
    assert isinstance(terminus_schedules[0], Departure)


@patch.object(DepartureApiClient, "get_navitia_api")
def test_raise_on_missing_region_coordinates(
    mock_get_navitia_api: MagicMock, departure_apis: DepartureApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get_navitia_api.return_value = mock_response

    # When/Then
    with pytest.raises(ValueError):
        departure_apis.list_departures(
            region_id="bar",
        )
