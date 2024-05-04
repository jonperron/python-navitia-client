import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.line_and_route import Line
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
    mock_response.json.return_value = {
        "lines": [
            {
                "closing_time": "220430",
                "code": "",
                "codes": [],
                "color": "",
                "commercial_mode": {"id": "commercial_mode:barS", "name": "bar foo"},
                "geojson": {"coordinates": [], "type": "MultiLineString"},
                "id": "line:foo:FR:Line::0000000:",
                "links": [],
                "name": "Lauterbourg - Woerth Rhein",
                "network": {"id": "network:foo:barS", "links": [], "name": "bar foo"},
                "opening_time": "043900",
                "physical_modes": [
                    {
                        "id": "physical_mode:LongDistanceTrain",
                        "name": "Train grande vitesse",
                    }
                ],
                "routes": [
                    {
                        "direction": {
                            "embedded_type": "stop_area",
                            "id": "stop_area:foo:0000000",
                            "name": "Lauterbourg (Lauterbourg)",
                            "quality": 0,
                            "stop_area": {
                                "codes": [
                                    {"type": "source", "value": "0000000"},
                                    {"type": "uic", "value": "0000000"},
                                ],
                                "coord": {"lat": "48.967697", "lon": "8.182682"},
                                "id": "stop_area:foo:0000000",
                                "label": "Lauterbourg " "(Lauterbourg)",
                                "links": [],
                                "name": "Lauterbourg",
                                "timezone": "Europe/Paris",
                            },
                        },
                        "direction_type": "forward",
                        "geojson": {"coordinates": [], "type": "MultiLineString"},
                        "id": "route:foo:FR:Line::0000000:",
                        "is_frequence": "False",
                        "links": [],
                        "name": "Lauterbourg - Woerth Rhein",
                    }
                ],
                "text_color": "",
            },
            {
                "closing_time": "214900",
                "code": "",
                "codes": [],
                "color": "",
                "commercial_mode": {"id": "commercial_mode:barS", "name": "bar foo"},
                "geojson": {"coordinates": [], "type": "MultiLineString"},
                "id": "line:foo:CSR:0000000",
                "links": [],
                "name": "Marseille Saint-Charles - Frankfurt am Main Hbf",
                "network": {"id": "network:foo:barS", "links": [], "name": "bar foo"},
                "opening_time": "081200",
                "physical_modes": [
                    {
                        "id": "physical_mode:LongDistanceTrain",
                        "name": "Train grande vitesse",
                    }
                ],
                "routes": [
                    {
                        "direction": {
                            "embedded_type": "stop_area",
                            "id": "stop_area:foo:0000000",
                            "name": "Marseille Saint-Charles " "(Marseille)",
                            "quality": 0,
                            "stop_area": {
                                "codes": [
                                    {"type": "source", "value": "0000000"},
                                    {"type": "uic", "value": "0000000"},
                                ],
                                "coord": {"lat": "43.302666", "lon": "5.380407"},
                                "id": "stop_area:foo:0000000",
                                "label": "Marseille " "Saint-Charles " "(Marseille)",
                                "links": [],
                                "name": "Marseille " "Saint-Charles",
                                "timezone": "Europe/Paris",
                            },
                        },
                        "direction_type": "forward",
                        "geojson": {"coordinates": [], "type": "MultiLineString"},
                        "id": "route:foo:CSR:0000000",
                        "is_frequence": "False",
                        "links": [],
                        "name": "Marseille Saint-Charles - Frankfurt am Main " "Hbf",
                    }
                ],
                "text_color": "",
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
    lines, _ = line_apis.list_entity_collection_from_region("tuz")

    # Then
    assert len(lines) == 2
    assert isinstance(lines[0], Line)


@patch.object(LineApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, line_apis: LineApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "lines": [
            {
                "closing_time": "220430",
                "code": "",
                "codes": [],
                "color": "",
                "commercial_mode": {"id": "commercial_mode:barS", "name": "bar foo"},
                "geojson": {"coordinates": [], "type": "MultiLineString"},
                "id": "line:foo:FR:Line::0000000:",
                "links": [],
                "name": "Lauterbourg - Woerth Rhein",
                "network": {"id": "network:foo:barS", "links": [], "name": "bar foo"},
                "opening_time": "043900",
                "physical_modes": [
                    {
                        "id": "physical_mode:LongDistanceTrain",
                        "name": "Train grande vitesse",
                    }
                ],
                "routes": [
                    {
                        "direction": {
                            "embedded_type": "stop_area",
                            "id": "stop_area:foo:0000000",
                            "name": "Lauterbourg (Lauterbourg)",
                            "quality": 0,
                            "stop_area": {
                                "codes": [
                                    {"type": "source", "value": "0000000"},
                                    {"type": "uic", "value": "0000000"},
                                ],
                                "coord": {"lat": "48.967697", "lon": "8.182682"},
                                "id": "stop_area:foo:87212464",
                                "label": "Lauterbourg " "(Lauterbourg)",
                                "links": [],
                                "name": "Lauterbourg",
                                "timezone": "Europe/Paris",
                            },
                        },
                        "direction_type": "forward",
                        "geojson": {"coordinates": [], "type": "MultiLineString"},
                        "id": "route:foo:FR:Line::0000000:",
                        "is_frequence": "False",
                        "links": [],
                        "name": "Lauterbourg - Woerth Rhein",
                    }
                ],
                "text_color": "",
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
    lines, _ = line_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(lines) == 1
    assert isinstance(lines[0], Line)
