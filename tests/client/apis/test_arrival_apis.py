import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.arrival_apis import (
    ArrivalApiClient,
)
from navitia_client.entities.arrival import Arrival


@pytest.fixture
def arrival_apis():
    return ArrivalApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(ArrivalApiClient, "get_navitia_api")
def test_list_objects(
    mock_get_navitia_api: MagicMock, arrival_apis: ArrivalApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/arrivals.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    arrivals, _ = arrival_apis.list_arrivals(
        region_id="bar", resource_path="foo:bar:fuzz"
    )

    # Then
    assert len(arrivals) == 10
    assert isinstance(arrivals[0], Arrival)


@patch.object(ArrivalApiClient, "get_navitia_api")
def test_raise_on_missing_region_coordinates(
    mock_get_navitia_api: MagicMock, arrival_apis: ArrivalApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get_navitia_api.return_value = mock_response

    # When/Then
    with pytest.raises(ValueError):
        arrival_apis.list_arrivals(
            region_id="bar",
        )
