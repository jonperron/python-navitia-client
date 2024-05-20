import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.places_nearby_apis import PlacesNearbyApiClient
from navitia_client.entities.place import Place


@pytest.fixture
def places_nearby_apis():
    return PlacesNearbyApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(PlacesNearbyApiClient, "get_navitia_api")
def test_list_objects(
    mock_get_navitia_api: MagicMock, places_nearby_apis: PlacesNearbyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/places_nearby.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    places, _ = places_nearby_apis.list_objects_by_region_id_and_path(
        region_id="bar", resource_path="stop_area/foo:bar"
    )

    # Then
    assert len(places) == 2
    assert isinstance(places[0], Place)
    assert places[0].embedded_type == "stop_area"
    assert places[1].embedded_type == "stop_point"
