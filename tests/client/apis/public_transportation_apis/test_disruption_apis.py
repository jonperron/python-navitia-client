import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.disruption import Disruption
from navitia_client.client.apis.public_transportation_apis import DisruptionApiClient


@pytest.fixture
def disruption_apis():
    return DisruptionApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(DisruptionApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, disruption_apis: DisruptionApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "disruptions": [
            {
                "application_periods": [
                    {"begin": "20240408T071300", "end": "20240408T103800"}
                ],
                "cause": "",
                "contributor": "realtime.foo.piv",
                "disruption_id": "184019c6-e73d-4806-b1bd-8d01d396833f",
                "disruption_uri": "184019c6-e73d-4806-b1bd-8d01d396833f",
                "id": "184019c6-e73d-4806-b1bd-8d01d396833f",
                "impact_id": "184019c6-e73d-4806-b1bd-8d01d396833f",
                "impacted_objects": [
                    {
                        "impacted_stops": [
                            {
                                "amended_arrival_time": "071300",
                                "amended_departure_time": "071300",
                                "arrival_status": "unchanged",
                                "base_arrival_time": "071300",
                                "base_departure_time": "071300",
                                "cause": "",
                                "departure_status": "unchanged",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "48.844945", "lon": "2.373481"},
                                    "equipments": [],
                                    "id": "stop_point:foo:87686006:LongDistanceTrain",
                                    "label": "Paris "
                                    "- "
                                    "Gare "
                                    "de "
                                    "Lyon "
                                    "- "
                                    "Hall "
                                    "1 "
                                    "& "
                                    "2 "
                                    "(Paris)",
                                    "links": [],
                                    "name": "Paris "
                                    "- "
                                    "Gare "
                                    "de "
                                    "Lyon "
                                    "- "
                                    "Hall "
                                    "1 "
                                    "& "
                                    "2",
                                },
                                "stop_time_effect": "unchanged",
                            },
                            {
                                "amended_arrival_time": "091100",
                                "amended_departure_time": "092600",
                                "arrival_status": "delayed",
                                "base_arrival_time": "090100",
                                "base_departure_time": "090600",
                                "cause": "Saturation " "des " "voies en " "gare",
                                "departure_status": "delayed",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "45.721109", "lon": "5.074969"},
                                    "equipments": [],
                                    "id": "stop_point:foo:87762906:LongDistanceTrain",
                                    "label": "Lyon "
                                    "Saint-Exupéry "
                                    "TGV "
                                    "(Colombier-Saugnieu)",
                                    "links": [],
                                    "name": "Lyon " "Saint-Exupéry " "TGV",
                                },
                                "stop_time_effect": "delayed",
                            },
                            {
                                "amended_arrival_time": "103800",
                                "amended_departure_time": "103800",
                                "arrival_status": "delayed",
                                "base_arrival_time": "101300",
                                "base_departure_time": "101300",
                                "cause": "Saturation " "des " "voies en " "gare",
                                "departure_status": "unchanged",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "45.191491", "lon": "5.714548"},
                                    "equipments": [],
                                    "id": "stop_point:foo:87747006:LongDistanceTrain",
                                    "label": "Grenoble " "(Grenoble)",
                                    "links": [],
                                    "name": "Grenoble",
                                },
                                "stop_time_effect": "delayed",
                            },
                        ],
                        "pt_object": {
                            "embedded_type": "trip",
                            "id": "foo:2024-04-08:6905:1187:LongDistanceTrain",
                            "name": "foo:2024-04-08:6905:1187:LongDistanceTrain",
                            "quality": 0,
                            "trip": {
                                "id": "foo:2024-04-08:6905:1187:LongDistanceTrain",
                                "name": "6905",
                            },
                        },
                    }
                ],
                "messages": [
                    {
                        "channel": {
                            "content_type": "",
                            "id": "rt",
                            "name": "rt",
                            "types": ["web", "mobile"],
                        },
                        "text": "Saturation des voies en gare",
                    }
                ],
                "severity": {
                    "color": "#000000",
                    "effect": "SIGNIFICANT_DELAYS",
                    "name": "trip delayed",
                    "priority": 42,
                },
                "status": "past",
                "updated_at": "20240409T071857",
                "uri": "184019c6-e73d-4806-b1bd-8d01d396833f",
            },
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
            },
            {
                "application_periods": [
                    {"begin": "20240407T213900", "end": "20240407T224900"}
                ],
                "cause": "",
                "contributor": "realtime.foo.piv",
                "disruption_id": "000000",
                "disruption_uri": "d240df5f-acfb-48c5-add3-b8ea49e66f89",
                "id": "000000",
                "impact_id": "000000",
                "impacted_objects": [
                    {
                        "impacted_stops": [
                            {
                                "amended_arrival_time": "213900",
                                "amended_departure_time": "213900",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "46.167616", "lon": "-1.151875"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:Train",
                                    "label": "La "
                                    "Rochelle "
                                    "Porte "
                                    "Dauphine "
                                    "(La "
                                    "Rochelle)",
                                    "links": [],
                                    "name": "La " "Rochelle " "Porte " "Dauphine",
                                },
                                "stop_time_effect": "added",
                            },
                            {
                                "amended_arrival_time": "214900",
                                "amended_departure_time": "214900",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "46.152705", "lon": "-1.145853"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:Coach",
                                    "label": "La " "Rochelle " "(La " "Rochelle)",
                                    "links": [],
                                    "name": "La " "Rochelle",
                                },
                                "stop_time_effect": "added",
                            },
                            {
                                "amended_arrival_time": "215700",
                                "amended_departure_time": "215700",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "46.12761", "lon": "-1.128293"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:Train",
                                    "label": "Aytré " "Plage " "(Aytré)",
                                    "links": [],
                                    "name": "Aytré " "Plage",
                                },
                                "stop_time_effect": "added",
                            },
                            {
                                "amended_arrival_time": "220800",
                                "amended_departure_time": "220800",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "46.107785", "lon": "-1.115622"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:Train",
                                    "label": "Angoulins " "sur " "Mer " "(Angoulins)",
                                    "links": [],
                                    "name": "Angoulins " "sur " "Mer",
                                },
                                "stop_time_effect": "added",
                            },
                            {
                                "amended_arrival_time": "222300",
                                "amended_departure_time": "222300",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "46.078282", "lon": "-1.091118"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:Train",
                                    "label": "Châtelaillon " "(Châtelaillon-Plage)",
                                    "links": [],
                                    "name": "Châtelaillon",
                                },
                                "stop_time_effect": "added",
                            },
                            {
                                "amended_arrival_time": "223700",
                                "amended_departure_time": "223700",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "45.992563", "lon": "-1.026912"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:Train",
                                    "label": "Saint-Laurent-de-la-Prée "
                                    "- "
                                    "Fouras "
                                    "(Saint-Laurent-de-la-Prée)",
                                    "links": [],
                                    "name": "Saint-Laurent-de-la-Prée " "- " "Fouras",
                                },
                                "stop_time_effect": "added",
                            },
                            {
                                "amended_arrival_time": "224900",
                                "amended_departure_time": "224900",
                                "arrival_status": "added",
                                "cause": "",
                                "departure_status": "added",
                                "is_detour": False,
                                "stop_point": {
                                    "coord": {"lat": "45.947189", "lon": "-0.963556"},
                                    "equipments": [],
                                    "id": "stop_point:foo:000000:LongDistanceTrain",
                                    "label": "Rochefort " "(Rochefort)",
                                    "links": [],
                                    "name": "Rochefort",
                                },
                                "stop_time_effect": "added",
                            },
                        ],
                        "pt_object": {
                            "embedded_type": "trip",
                            "id": "PIV:REALTIME:000000:000000:coach:railReplacementCoach:ROUTIER",
                            "name": "PIV:REALTIME:000000:000000:coach:railReplacementCoach:ROUTIER",
                            "quality": 0,
                            "trip": {
                                "id": "PIV:REALTIME:000000:000000:000000:coach:railReplacementCoach:ROUTIER",
                                "name": "79010",
                            },
                        },
                    }
                ],
                "severity": {
                    "color": "#000000",
                    "effect": "ADDITIONAL_SERVICE",
                    "name": "additional service",
                    "priority": 42,
                },
                "status": "past",
                "updated_at": "20240409T071857",
                "uri": "d240df5f-acfb-48c5-add3-b8ea49e66f89",
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
    disruptions, _ = disruption_apis.list_entity_collection_from_region("tuz")

    # Then
    assert len(disruptions) == 3
    assert isinstance(disruptions[0], Disruption)
    assert isinstance(disruptions[1], Disruption)
    assert isinstance(disruptions[2], Disruption)


@patch.object(DisruptionApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, disruption_apis: DisruptionApiClient
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
    disruptions, _ = disruption_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(disruptions) == 1
    assert isinstance(disruptions[0], Disruption)
