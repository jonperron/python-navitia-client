import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.vehicle_journey import VehicleJourney
from navitia_client.client.apis.public_transportation_apis import (
    VehicleJourneyApiClient,
)


@pytest.fixture
def vehicle_journeys_apis():
    return VehicleJourneyApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(VehicleJourneyApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, vehicle_journeys_apis: VehicleJourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "vehicle_journeys": [
            {
                "calendars": [
                    {
                        "active_periods": [{"begin": "20240408", "end": "20240409"}],
                        "week_pattern": {
                            "friday": False,
                            "monday": True,
                            "saturday": False,
                            "sunday": False,
                            "thursday": False,
                            "tuesday": False,
                            "wednesday": False,
                        },
                    }
                ],
                "codes": [
                    {
                        "type": "rt_piv",
                        "value": "2024-04-08:81440:1187:rail:international:FERRE",
                    },
                    {"type": "source", "value": "c1a8e28b6c3960f4a3e116d4f16ad62c"},
                ],
                "disruptions": [],
                "headsign": "81440",
                "id": "vehicle_journey:SNCF:2024-04-08:81440:1187:LongDistanceTrain",
                "journey_pattern": {
                    "id": "journey_pattern:0",
                    "name": "journey_pattern:0",
                },
                "name": "81440",
                "stop_times": [
                    {
                        "arrival_time": "045500",
                        "departure_time": "045500",
                        "drop_off_allowed": False,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.967697", "lon": "8.182682"},
                            "equipments": [],
                            "id": "stop_point:SNCF:87212464:LongDistanceTrain",
                            "label": "Lauterbourg " "(Lauterbourg)",
                            "links": [],
                            "name": "Lauterbourg",
                        },
                        "utc_arrival_time": "025500",
                        "utc_departure_time": "025500",
                    },
                    {
                        "arrival_time": "045800",
                        "departure_time": "045830",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.9807", "lon": "8.2128"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191064:LongDistanceTrain",
                            "label": "Berg (Pfalz) " "(Berg (Pfalz))",
                            "links": [],
                            "name": "Berg (Pfalz)",
                        },
                        "utc_arrival_time": "025800",
                        "utc_departure_time": "025830",
                    },
                    {
                        "arrival_time": "050100",
                        "departure_time": "050130",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.9921", "lon": "8.238099999999999"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80646141:LongDistanceTrain",
                            "label": "Neuburg " "(Rhein) " "(Neuburg am " "Rhein)",
                            "links": [],
                            "name": "Neuburg " "(Rhein)",
                        },
                        "utc_arrival_time": "030100",
                        "utc_departure_time": "030130",
                    },
                    {
                        "arrival_time": "050400",
                        "departure_time": "050430",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.016", "lon": "8.253"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191049:LongDistanceTrain",
                            "label": "Hagenbach " "(Hagenbach)",
                            "links": [],
                            "name": "Hagenbach",
                        },
                        "utc_arrival_time": "030400",
                        "utc_departure_time": "030430",
                    },
                    {
                        "arrival_time": "050800",
                        "departure_time": "050830",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.035", "lon": "8.2796"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80646133:LongDistanceTrain",
                            "label": "Maximiliansau "
                            "im Rüsten "
                            "(Wörth am "
                            "Rhein)",
                            "links": [],
                            "name": "Maximiliansau " "im Rüsten",
                        },
                        "utc_arrival_time": "030800",
                        "utc_departure_time": "030830",
                    },
                    {
                        "arrival_time": "051030",
                        "departure_time": "051030",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": False,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.0457", "lon": "8.273199999999999"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191031:LongDistanceTrain",
                            "label": "Wörth (Rhein) " "(Wörth am " "Rhein)",
                            "links": [],
                            "name": "Wörth (Rhein)",
                        },
                        "utc_arrival_time": "031030",
                        "utc_departure_time": "031030",
                    },
                ],
                "trip": {
                    "id": "SNCF:2024-04-08:81440:1187:LongDistanceTrain",
                    "name": "81440",
                },
                "validity_pattern": {
                    "beginning_date": "20240406",
                    "days": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100",
                },
            },
            {
                "calendars": [
                    {
                        "active_periods": [{"begin": "20240408", "end": "20240409"}],
                        "week_pattern": {
                            "friday": False,
                            "monday": True,
                            "saturday": False,
                            "sunday": False,
                            "thursday": False,
                            "tuesday": False,
                            "wednesday": False,
                        },
                    }
                ],
                "codes": [
                    {
                        "type": "rt_piv",
                        "value": "2024-04-08:81441:1187:rail:international:FERRE",
                    },
                    {"type": "source", "value": "d145c983b39d451668cda71221155b44"},
                ],
                "disruptions": [],
                "headsign": "81441",
                "id": "vehicle_journey:SNCF:2024-04-08:81441:1187:LongDistanceTrain",
                "journey_pattern": {
                    "id": "journey_pattern:1",
                    "name": "journey_pattern:1",
                },
                "name": "81441",
                "stop_times": [
                    {
                        "arrival_time": "043900",
                        "departure_time": "043900",
                        "drop_off_allowed": False,
                        "headsign": "81441",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.0457", "lon": "8.273199999999999"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191031:LongDistanceTrain",
                            "label": "Wörth (Rhein) " "(Wörth am " "Rhein)",
                            "links": [],
                            "name": "Wörth (Rhein)",
                        },
                        "utc_arrival_time": "023900",
                        "utc_departure_time": "023900",
                    },
                    {
                        "arrival_time": "045000",
                        "departure_time": "045000",
                        "drop_off_allowed": True,
                        "headsign": "81441",
                        "pickup_allowed": False,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.967697", "lon": "8.182682"},
                            "equipments": [],
                            "id": "stop_point:SNCF:87212464:LongDistanceTrain",
                            "label": "Lauterbourg " "(Lauterbourg)",
                            "links": [],
                            "name": "Lauterbourg",
                        },
                        "utc_arrival_time": "025000",
                        "utc_departure_time": "025000",
                    },
                ],
                "trip": {
                    "id": "SNCF:2024-04-08:81441:1187:LongDistanceTrain",
                    "name": "81441",
                },
                "validity_pattern": {
                    "beginning_date": "20240406",
                    "days": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100",
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
    vehicle_journeys, _ = vehicle_journeys_apis.list_entity_collection_from_region(
        "tuz"
    )

    # Then
    assert len(vehicle_journeys) == 2
    assert isinstance(vehicle_journeys[1], VehicleJourney)


@patch.object(VehicleJourneyApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, vehicle_journeys_apis: VehicleJourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "vehicle_journeys": [
            {
                "calendars": [
                    {
                        "active_periods": [{"begin": "20240408", "end": "20240409"}],
                        "week_pattern": {
                            "friday": False,
                            "monday": True,
                            "saturday": False,
                            "sunday": False,
                            "thursday": False,
                            "tuesday": False,
                            "wednesday": False,
                        },
                    }
                ],
                "codes": [
                    {
                        "type": "rt_piv",
                        "value": "2024-04-08:81440:1187:rail:international:FERRE",
                    },
                    {"type": "source", "value": "c1a8e28b6c3960f4a3e116d4f16ad62c"},
                ],
                "disruptions": [],
                "headsign": "81440",
                "id": "vehicle_journey:SNCF:2024-04-08:81440:1187:LongDistanceTrain",
                "journey_pattern": {
                    "id": "journey_pattern:0",
                    "name": "journey_pattern:0",
                },
                "name": "81440",
                "stop_times": [
                    {
                        "arrival_time": "045500",
                        "departure_time": "045500",
                        "drop_off_allowed": False,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.967697", "lon": "8.182682"},
                            "equipments": [],
                            "id": "stop_point:SNCF:87212464:LongDistanceTrain",
                            "label": "Lauterbourg " "(Lauterbourg)",
                            "links": [],
                            "name": "Lauterbourg",
                        },
                        "utc_arrival_time": "025500",
                        "utc_departure_time": "025500",
                    },
                    {
                        "arrival_time": "045800",
                        "departure_time": "045830",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.9807", "lon": "8.2128"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191064:LongDistanceTrain",
                            "label": "Berg (Pfalz) " "(Berg (Pfalz))",
                            "links": [],
                            "name": "Berg (Pfalz)",
                        },
                        "utc_arrival_time": "025800",
                        "utc_departure_time": "025830",
                    },
                    {
                        "arrival_time": "050100",
                        "departure_time": "050130",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "48.9921", "lon": "8.238099999999999"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80646141:LongDistanceTrain",
                            "label": "Neuburg " "(Rhein) " "(Neuburg am " "Rhein)",
                            "links": [],
                            "name": "Neuburg " "(Rhein)",
                        },
                        "utc_arrival_time": "030100",
                        "utc_departure_time": "030130",
                    },
                    {
                        "arrival_time": "050400",
                        "departure_time": "050430",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.016", "lon": "8.253"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191049:LongDistanceTrain",
                            "label": "Hagenbach " "(Hagenbach)",
                            "links": [],
                            "name": "Hagenbach",
                        },
                        "utc_arrival_time": "030400",
                        "utc_departure_time": "030430",
                    },
                    {
                        "arrival_time": "050800",
                        "departure_time": "050830",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": True,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.035", "lon": "8.2796"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80646133:LongDistanceTrain",
                            "label": "Maximiliansau "
                            "im Rüsten "
                            "(Wörth am "
                            "Rhein)",
                            "links": [],
                            "name": "Maximiliansau " "im Rüsten",
                        },
                        "utc_arrival_time": "030800",
                        "utc_departure_time": "030830",
                    },
                    {
                        "arrival_time": "051030",
                        "departure_time": "051030",
                        "drop_off_allowed": True,
                        "headsign": "81440",
                        "pickup_allowed": False,
                        "skipped_stop": False,
                        "stop_point": {
                            "coord": {"lat": "49.0457", "lon": "8.273199999999999"},
                            "equipments": [],
                            "id": "stop_point:SNCF:80191031:LongDistanceTrain",
                            "label": "Wörth (Rhein) " "(Wörth am " "Rhein)",
                            "links": [],
                            "name": "Wörth (Rhein)",
                        },
                        "utc_arrival_time": "031030",
                        "utc_departure_time": "031030",
                    },
                ],
                "trip": {
                    "id": "SNCF:2024-04-08:81440:1187:LongDistanceTrain",
                    "name": "81440",
                },
                "validity_pattern": {
                    "beginning_date": "20240406",
                    "days": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100",
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
    vehicle_journeys, _ = vehicle_journeys_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(vehicle_journeys) == 1
    assert isinstance(vehicle_journeys[0], VehicleJourney)
