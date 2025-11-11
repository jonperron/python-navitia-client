import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.stop_area import StopPoint
from navitia_client.client.apis.public_transportation_apis import StopPointApiClient


@pytest.fixture
def stop_point_apis():
    return StopPointApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(StopPointApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, stop_point_apis: StopPointApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/stop_points.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    physical_modes, _ = stop_point_apis.list_entity_collection_from_region("bar")

    # Then
    assert len(physical_modes) == 3
    assert isinstance(physical_modes[1], StopPoint)


@patch.object(StopPointApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, stop_point_apis: StopPointApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/stop_points.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    physical_modes, _ = stop_point_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(physical_modes) == 3
    assert isinstance(physical_modes[0], StopPoint)
