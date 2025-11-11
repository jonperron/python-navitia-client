import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.departure_apis import (
    DepartureApiClient,
)
from navitia_client.entities.response.departure import Departure


@pytest.fixture
def departure_apis():
    return DepartureApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(DepartureApiClient, "get_navitia_api")
def test_list_objects_by_region_id_and_path(
    mock_get_navitia_api: MagicMock, departure_apis: DepartureApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/departures.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    departures, _ = departure_apis.list_departures_by_region_id_and_path(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(departures) == 10
    assert isinstance(departures[0], Departure)


@patch.object(DepartureApiClient, "get_navitia_api")
def test_list_objects_by_coordinates(
    mock_get_navitia_api: MagicMock, departure_apis: DepartureApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/departures.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    departures, _ = departure_apis.list_departures_by_coordinates(
        region_lon=1.1, region_lat=1.2, lon=2.1, lat=2.2
    )

    # Then
    assert len(departures) == 10
    assert isinstance(departures[0], Departure)
