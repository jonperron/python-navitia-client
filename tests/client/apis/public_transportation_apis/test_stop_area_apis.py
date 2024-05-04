import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.stop_area import StopArea
from navitia_client.client.apis.public_transportation_apis import StopAreaApiClient


@pytest.fixture
def stop_area_apis():
    return StopAreaApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(StopAreaApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, stop_area_apis: StopAreaApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "stop_areas": [
            {
                "codes": [{"type": "secondary_id", "value": "foo"}],
                "coord": {"lat": "0", "lon": "0"},
                "id": "stop_area:bar:00000",
                "label": "",
                "links": [],
                "name": "",
                "timezone": "Europe/Paris",
            },
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "50.776351", "lon": "6.083862"},
                        "id": "admin:osm:relation:62564",
                        "insee": "",
                        "label": "Aachen",
                        "level": 8,
                        "name": "Aachen",
                        "zip_code": "",
                    }
                ],
                "codes": [
                    {"type": "source", "value": "80153452"},
                    {"type": "uic", "value": "80153452"},
                ],
                "coord": {"lat": "50.7675", "lon": "6.0912"},
                "id": "stop_area:foo:000000",
                "label": "Aachen Hbf (Aachen)",
                "links": [],
                "name": "Aachen Hbf",
                "timezone": "Europe/Paris",
            },
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "49.6977145", "lon": "1.7646826"},
                        "id": "admin:fr:60001",
                        "insee": "60001",
                        "label": "Abancourt (60220)",
                        "level": 8,
                        "name": "Abancourt",
                        "zip_code": "60220",
                    }
                ],
                "codes": [
                    {"type": "source", "value": "87313759"},
                    {"type": "uic", "value": "87313759"},
                ],
                "coord": {"lat": "49.685621", "lon": "1.774297"},
                "id": "stop_area:bar:00000000",
                "label": "Abancourt (Abancourt)",
                "links": [],
                "name": "Abancourt",
                "timezone": "Europe/Paris",
            },
        ],
        "pagination": {
            "items_on_page": 25,
            "items_per_page": 25,
            "start_page": 0,
            "total_result": 99,
        },
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    physical_modes, _ = stop_area_apis.list_entity_collection_from_region("bar")

    # Then
    assert len(physical_modes) == 3
    assert isinstance(physical_modes[1], StopArea)


@patch.object(StopAreaApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, stop_area_apis: StopAreaApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "stop_areas": [
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "49.6977145", "lon": "1.7646826"},
                        "id": "admin:fr:60001",
                        "insee": "60001",
                        "label": "Abancourt (60220)",
                        "level": 8,
                        "name": "Abancourt",
                        "zip_code": "60220",
                    }
                ],
                "codes": [
                    {"type": "source", "value": "87313759"},
                    {"type": "uic", "value": "87313759"},
                ],
                "coord": {"lat": "49.685621", "lon": "1.774297"},
                "id": "stop_area:bar:00000000",
                "label": "Abancourt (Abancourt)",
                "links": [],
                "name": "Abancourt",
                "timezone": "Europe/Paris",
            },
        ],
        "pagination": {
            "items_on_page": 25,
            "items_per_page": 25,
            "start_page": 0,
            "total_result": 99,
        },
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    physical_modes, _ = stop_area_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(physical_modes) == 1
    assert isinstance(physical_modes[0], StopArea)
