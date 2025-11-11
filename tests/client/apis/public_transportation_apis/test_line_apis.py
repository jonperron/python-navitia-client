import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.line_and_route import Line
from navitia_client.entities.request.public_transportations import LineRequest
from navitia_client.client.apis.public_transportation_apis import LineApiClient


@pytest.fixture
def line_apis():
    return LineApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(LineApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, line_apis: LineApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/line.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    lines, _ = line_apis.list_entity_collection_from_region("tuz", LineRequest())

    # Then
    assert len(lines) == 2
    assert isinstance(lines[0], Line)


@patch.object(LineApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, line_apis: LineApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/line.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    lines, _ = line_apis.get_entity_by_id("tuz", "1", LineRequest())

    # Then
    assert len(lines) == 2
    assert isinstance(lines[0], Line)
