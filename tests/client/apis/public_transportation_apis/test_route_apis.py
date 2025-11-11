import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.line_and_route import Route
from navitia_client.entities.request.public_transportations import RouteRequest
from navitia_client.client.apis.public_transportation_apis import RouteApiClient


@pytest.fixture
def route_apis():
    return RouteApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(RouteApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, route_apis: RouteApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/routes.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    routes, _ = route_apis.list_entity_collection_from_region("tuz", RouteRequest())

    # Then
    assert len(routes) == 2
    assert isinstance(routes[0], Route)
    assert isinstance(routes[1], Route)


@patch.object(RouteApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, route_apis: RouteApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/routes.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    routes, _ = route_apis.get_entity_by_id("tuz", "1", RouteRequest())

    # Then
    assert len(routes) == 2
    assert isinstance(routes[0], Route)
