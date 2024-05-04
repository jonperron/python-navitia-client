import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.stop_area import StopPoint
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
    mock_response.json.return_value = {
        "stop_points": [
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "43.4255303", "lon": "6.7694244"},
                        "id": "admin:fr:83118",
                        "insee": "83118",
                        "label": "Saint-Raphaël " "(83530-83700)",
                        "level": 8,
                        "name": "Saint-Raphaël",
                        "zip_code": "83530;83700",
                    }
                ],
                "coord": {"lat": "43.43137", "lon": "6.8565"},
                "equipments": [],
                "id": "stop_point:SNCF:87757559:Train",
                "label": "Agay (Saint-Raphaël)",
                "links": [],
                "name": "Agay",
                "stop_area": {
                    "codes": [
                        {"type": "source", "value": "87757559"},
                        {"type": "uic", "value": "87757559"},
                    ],
                    "coord": {"lat": "43.43137", "lon": "6.8565"},
                    "id": "stop_area:SNCF:87757559",
                    "label": "Agay (Saint-Raphaël)",
                    "links": [],
                    "name": "Agay",
                    "timezone": "Europe/Paris",
                },
            },
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "43.3134787", "lon": "3.4771629"},
                        "id": "admin:fr:34003",
                        "insee": "34003",
                        "label": "Agde (34300)",
                        "level": 8,
                        "name": "Agde",
                        "zip_code": "34300",
                    }
                ],
                "coord": {"lat": "43.31728", "lon": "3.466203"},
                "equipments": [],
                "id": "stop_point:SNCF:87781278:LongDistanceTrain",
                "label": "Agde (Agde)",
                "links": [],
                "name": "Agde",
                "stop_area": {
                    "codes": [
                        {"type": "source", "value": "87781278"},
                        {"type": "uic", "value": "87781278"},
                    ],
                    "coord": {"lat": "43.31728", "lon": "3.466203"},
                    "id": "stop_area:SNCF:87781278",
                    "label": "Agde (Agde)",
                    "links": [],
                    "name": "Agde",
                    "timezone": "Europe/Paris",
                },
            },
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "43.3134787", "lon": "3.4771629"},
                        "id": "admin:fr:34003",
                        "insee": "34003",
                        "label": "Agde (34300)",
                        "level": 8,
                        "name": "Agde",
                        "zip_code": "34300",
                    }
                ],
                "coord": {"lat": "43.31728", "lon": "3.466203"},
                "equipments": [],
                "id": "stop_point:SNCF:87781278:Train",
                "label": "Agde (Agde)",
                "links": [],
                "name": "Agde",
                "stop_area": {
                    "codes": [
                        {"type": "source", "value": "87781278"},
                        {"type": "uic", "value": "87781278"},
                    ],
                    "coord": {"lat": "43.31728", "lon": "3.466203"},
                    "id": "stop_area:SNCF:87781278",
                    "label": "Agde (Agde)",
                    "links": [],
                    "name": "Agde",
                    "timezone": "Europe/Paris",
                },
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
    mock_response.json.return_value = {
        "stop_points": [
            {
                "administrative_regions": [
                    {
                        "coord": {"lat": "43.3134787", "lon": "3.4771629"},
                        "id": "admin:fr:34003",
                        "insee": "34003",
                        "label": "Agde (34300)",
                        "level": 8,
                        "name": "Agde",
                        "zip_code": "34300",
                    }
                ],
                "coord": {"lat": "43.31728", "lon": "3.466203"},
                "equipments": [],
                "id": "stop_point:SNCF:87781278:Train",
                "label": "Agde (Agde)",
                "links": [],
                "name": "Agde",
                "stop_area": {
                    "codes": [
                        {"type": "source", "value": "87781278"},
                        {"type": "uic", "value": "87781278"},
                    ],
                    "coord": {"lat": "43.31728", "lon": "3.466203"},
                    "id": "stop_area:SNCF:87781278",
                    "label": "Agde (Agde)",
                    "links": [],
                    "name": "Agde",
                    "timezone": "Europe/Paris",
                },
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
    physical_modes, _ = stop_point_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(physical_modes) == 1
    assert isinstance(physical_modes[0], StopPoint)
