from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.line_report_apis import LineReportsApiClient
from navitia_client.entities.disruption import Disruption
from navitia_client.entities.line_report import LineReport


@pytest.fixture
def line_reports_apis():
    return LineReportsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(LineReportsApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, line_reports_apis: LineReportsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "disruptions": [
            {
                "application_periods": [
                    {"begin": "20240408T040700", "end": "20240408T054700"}
                ],
                "cause": "",
                "contributor": "realtime.foo.piv",
                "disruption_id": "7e964de5-b7f0-4760-8095-5203ac2708a1",
                "disruption_uri": "7e964de5-b7f0-4760-8095-5203ac2708a1",
                "id": "000000",
                "impact_id": "000000",
                "impacted_objects": [
                    {
                        "pt_object": {
                            "embedded_type": "trip",
                            "id": "foo:2024-04-08:000000:1187:Coach",
                            "name": "foo:2024-04-08:33000000208:1187:Coach",
                            "quality": 0,
                            "trip": {
                                "id": "foo:2024-04-08:33208:1187:Coach",
                                "name": "33208",
                            },
                        }
                    }
                ],
                "severity": {
                    "color": "#000000",
                    "effect": "NO_SERVICE",
                    "name": "trip canceled",
                    "priority": 42,
                },
                "status": "past",
                "updated_at": "20240409T071857",
                "uri": "000000",
            }
        ],
        "line_reports": [
            {
                "line": {
                    "closing_time": "220430",
                    "code": "",
                    "codes": [],
                    "color": "",
                    "commercial_mode": {
                        "id": "commercial_mode:barS",
                        "name": "bar foo",
                    },
                    "geojson": {"coordinates": [], "type": "MultiLineString"},
                    "id": "line:foo:FR:Line::0000000:",
                    "links": [],
                    "name": "Lauterbourg - Woerth Rhein",
                    "network": {
                        "id": "network:foo:barS",
                        "links": [],
                        "name": "bar foo",
                    },
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
                                    "label": "Lauterbourg (Lauterbourg)",
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
                "pt_objects": [
                    {
                        "embedded_type": "stop_area",
                        "id": "stop_area:SNCF:87758896",
                        "name": "Saint-Rémy-lès-Chevreuse (Saint-Rémy-lès-Chevreuse)",
                        "quality": 70,
                        "stop_area": {
                            "administrative_regions": [
                                {
                                    "coord": {"lat": "48.7054888", "lon": "2.071109"},
                                    "id": "admin:fr:78575",
                                    "insee": "78575",
                                    "label": "Saint-Rémy-lès-Chevreuse (78470)",
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
                            "label": "Saint-Rémy-lès-Chevreuse (Saint-Rémy-lès-Chevreuse)",
                            "links": [],
                            "name": "Saint-Rémy-lès-Chevreuse",
                            "timezone": "Europe/Paris",
                        },
                    }
                ],
            }
        ],
    }

    mock_get_navitia_api.return_value = mock_response

    # When
    disruptions, line_reports = line_reports_apis.list_line_reports(
        region_id="bar", resource_path="foo"
    )

    # Then
    assert len(disruptions) == 1
    assert isinstance(disruptions[0], Disruption)
    assert len(line_reports) == 1
    assert isinstance(line_reports[0], LineReport)
