import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.inverted_geocoding_apis import (
    InvertedGeocodingApiClient,
)
from navitia_client.entities.response.place import Place


@pytest.fixture
def inverted_geocoding_apis():
    return InvertedGeocodingApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(InvertedGeocodingApiClient, "get_navitia_api")
def test_list_objects(
    mock_get_navitia_api: MagicMock, inverted_geocoding_apis: InvertedGeocodingApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/inverted_geocoding.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    places = inverted_geocoding_apis.get_address_from_region_id_and_id(
        region_id="foo", id="bar"
    )

    # Then
    assert len(places) == 1
    assert isinstance(places[0], Place)
