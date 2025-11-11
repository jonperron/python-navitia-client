import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.arrival_apis import (
    ArrivalApiClient,
)
from navitia_client.entities.response.arrival import Arrival


@pytest.fixture
def arrival_apis():
    return ArrivalApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(ArrivalApiClient, "get_navitia_api")
def test_list_objects_by_id_and_path(
    mock_get_navitia_api: MagicMock, arrival_apis: ArrivalApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/arrivals.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    arrivals, _ = arrival_apis.list_arrivals_by_region_id_and_path(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(arrivals) == 10
    assert isinstance(arrivals[0], Arrival)


@patch.object(ArrivalApiClient, "get_navitia_api")
def test_list_objects_by_coordinates(
    mock_get_navitia_api: MagicMock, arrival_apis: ArrivalApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/arrivals.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    arrivals, _ = arrival_apis.list_arrivals_by_coordinates(
        region_lon=1.1, region_lat=2.2, lat=1.3, lon=2.3
    )

    # Then
    assert len(arrivals) == 10
    assert isinstance(arrivals[0], Arrival)
