from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.place_apis import PlacesApiClient
from navitia_client.entities.place import Place


@pytest.fixture
def places_apis():
    return PlacesApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(PlacesApiClient, "get_navitia_api")
def test_list_contributors(
    mock_get_navitia_api: MagicMock, places_apis: PlacesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "places": [
            {
                "embedded_type": "stop_area",
                "id": "stop_area:SNCF:87758011",
                "name": "La Grande Arche de la Défense (Puteaux)",
                "quality": 70,
                "stop_area": {
                    "administrative_regions": [
                        {
                            "coord": {"lat": "48.8841522", "lon": "2.2368863"},
                            "id": "admin:fr:92062",
                            "insee": "92062",
                            "label": "Puteaux " "(92800)",
                            "level": 8,
                            "name": "Puteaux",
                            "zip_code": "92800",
                        }
                    ],
                    "codes": [
                        {"type": "source", "value": "87758011"},
                        {"type": "uic", "value": "87758011"},
                    ],
                    "coord": {"lat": "48.891718", "lon": "2.238212"},
                    "id": "stop_area:SNCF:87758011",
                    "label": "La Grande Arche de la Défense (Puteaux)",
                    "links": [],
                    "name": "La Grande Arche de la Défense",
                    "timezone": "Europe/Paris",
                },
            }
        ]
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    places = places_apis.list_places(region_id="bar", query="DEFENSE")

    # Then
    assert len(places) == 1
    assert isinstance(places[0], Place)
