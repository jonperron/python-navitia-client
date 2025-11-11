import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.place_apis import PlacesApiClient
from navitia_client.entities.request.place import PlaceRequest
from navitia_client.entities.response.place import Place


@pytest.fixture
def places_apis():
    return PlacesApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(PlacesApiClient, "get_navitia_api")
def test_list_objects(
    mock_get_navitia_api: MagicMock, places_apis: PlacesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/places.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)
    mock_get_navitia_api.return_value = mock_response

    # When
    request = PlaceRequest(query="DEFENSE")
    places = places_apis.list_places(region_id="bar", request=request)

    # Then
    assert len(places) == 1
    assert isinstance(places[0], Place)
