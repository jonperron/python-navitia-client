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
    mock_response.json.return_value = {
        "pagination": {
            "items_on_page": 2,
            "items_per_page": 10,
            "start_page": 0,
            "total_result": 2,
        },
        "places_nearby": [
            {
                "distance": "0",
                "embedded_type": "stop_area",
                "id": "stop_area:SNCF:87758896",
                "name": "Saint-Rémy-lès-Chevreuse " "(Saint-Rémy-lès-Chevreuse)",
                "quality": 0,
                "stop_area": {
                    "administrative_regions": [
                        {
                            "coord": {"lat": "48.7054888", "lon": "2.071109"},
                            "id": "admin:fr:78575",
                            "insee": "78575",
                            "label": "Saint-Rémy-lès-Chevreuse " "(78470)",
                            "level": 8,
                            "name": "Saint-Rémy-lès-Chevreuse",
                            "zip_code": "78470",
                        }
                    ],
                    "codes": [
                        {"type": "source", "value": "87758896"},
                        {"type": "uic", "value": "87758896"},
                    ],
                    "coord": {"lat": "48.702722", "lon": "2.070924"},
                    "id": "stop_area:SNCF:87758896",
                    "label": "Saint-Rémy-lès-Chevreuse " "(Saint-Rémy-lès-Chevreuse)",
                    "links": [],
                    "name": "Saint-Rémy-lès-Chevreuse",
                    "timezone": "Europe/Paris",
                },
            },
            {
                "distance": "0",
                "embedded_type": "stop_point",
                "id": "stop_point:SNCF:87758896:RapidTransit",
                "name": "Saint-Rémy-lès-Chevreuse " "(Saint-Rémy-lès-Chevreuse)",
                "quality": 0,
                "stop_point": {
                    "administrative_regions": [
                        {
                            "coord": {"lat": "48.7054888", "lon": "2.071109"},
                            "id": "admin:fr:78575",
                            "insee": "78575",
                            "label": "Saint-Rémy-lès-Chevreuse " "(78470)",
                            "level": 8,
                            "name": "Saint-Rémy-lès-Chevreuse",
                            "zip_code": "78470",
                        }
                    ],
                    "coord": {"lat": "48.702722", "lon": "2.070924"},
                    "equipments": [],
                    "id": "stop_point:SNCF:87758896:RapidTransit",
                    "label": "Saint-Rémy-lès-Chevreuse " "(Saint-Rémy-lès-Chevreuse)",
                    "links": [],
                    "name": "Saint-Rémy-lès-Chevreuse",
                    "stop_area": {
                        "codes": [
                            {"type": "source", "value": "87758896"},
                            {"type": "uic", "value": "87758896"},
                        ],
                        "coord": {"lat": "48.702722", "lon": "2.070924"},
                        "id": "stop_area:SNCF:87758896",
                        "label": "Saint-Rémy-lès-Chevreuse "
                        "(Saint-Rémy-lès-Chevreuse)",
                        "links": [],
                        "name": "Saint-Rémy-lès-Chevreuse",
                        "timezone": "Europe/Paris",
                    },
                },
            },
        ],
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    places, _ = places_nearby_apis.list_objects(
        region_id="bar", resource_path="stop_area/foo:bar"
    )

    # Then
    assert len(places) == 2
    assert isinstance(places[0], Place)
    assert places[0].embedded_type == "stop_area"
    assert places[1].embedded_type == "stop_point"


@patch.object(PlacesNearbyApiClient, "get_navitia_api")
def test_raise_on_missing_parameters(
    mock_get_navitia_api: MagicMock, places_nearby_apis: PlacesNearbyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get_navitia_api.return_value = mock_response

    # When/Then
    with pytest.raises(ValueError):
        places_nearby_apis.list_objects()


@patch.object(PlacesNearbyApiClient, "get_navitia_api")
def test_raise_on_missing_region_id(
    mock_get_navitia_api: MagicMock, places_nearby_apis: PlacesNearbyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get_navitia_api.return_value = mock_response

    # When/Then
    with pytest.raises(ValueError):
        places_nearby_apis.list_objects(region_id="foo:bar")


@patch.object(PlacesNearbyApiClient, "get_navitia_api")
def test_raise_on_missing_region_coordinates(
    mock_get_navitia_api: MagicMock, places_nearby_apis: PlacesNearbyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {}
    mock_get_navitia_api.return_value = mock_response

    # When/Then
    with pytest.raises(ValueError):
        places_nearby_apis.list_objects(region_lon=2.5, region_lat=3.7)
