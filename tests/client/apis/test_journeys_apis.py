from datetime import datetime
import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.journeys_apis import JourneyApiClient
from navitia_client.entities.response import Journey


@pytest.fixture
def journeys_apis():
    return JourneyApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(JourneyApiClient, "get_navitia_api")
def test_list_covered_areas_with_region_id(
    mock_get_navitia_api: MagicMock, journeys_apis: JourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/journeys.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    journeys = journeys_apis.list_journeys_with_region_id(region_id="bar")

    # Then
    assert len(journeys) == 1
    assert isinstance(journeys[0], Journey)


@patch.object(JourneyApiClient, "get_navitia_api")
def test_list_covered_areas_with_resource_path(
    mock_get_navitia_api: MagicMock, journeys_apis: JourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/journeys.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    journeys = journeys_apis.list_journeys_with_resource_path(resource_path="bar")

    # Then
    assert len(journeys) == 1
    assert isinstance(journeys[0], Journey)


@patch.object(JourneyApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, journeys_apis: JourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/journeys.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    journeys = journeys_apis.list_journeys(from_="foo")

    # Then
    assert len(journeys) == 1
    assert isinstance(journeys[0], Journey)


@patch.object(JourneyApiClient, "get_navitia_api")
def test_list_empty_add_poi_infos_parameter(
    mock_get_navitia_api: MagicMock, journeys_apis: JourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/journeys.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response
    expected_url = "https://api.navitia.io/v1//journeys?datetime=2024-06-01T00:00:00&datetime_represents=departure&traveler_type=standard&data_freshness=realtime&language=en-GB&depth=1&max_duration_to_pt=1800&walking_speed=1.12&bike_speed=4.1&bss_speed=4.1&car_speed=16.8&min_nb_journeys=1&max_nb_journeys=1&count=1&max_nb_transfers=10&min_nb_transfers=0&max_duration=86400&wheelchair=False&direct_path=indifferent&debug=False&free_radius_from=0&free_radius_to=0&timeframe_duration=0&is_journey_schedules=False&from=foo&park_mode=none"

    # When
    journeys_apis.list_journeys(datetime_=datetime(2024, 6, 1), from_="foo")

    # Then
    mock_get_navitia_api.assert_called_with(expected_url)


@patch.object(JourneyApiClient, "get_navitia_api")
def test_list_add_poi_infos_parameter(
    mock_get_navitia_api: MagicMock, journeys_apis: JourneyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/journeys.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response
    expected_url = "https://api.navitia.io/v1//journeys?datetime=2024-06-01T00:00:00&datetime_represents=departure&traveler_type=standard&data_freshness=realtime&language=en-GB&depth=1&max_duration_to_pt=1800&walking_speed=1.12&bike_speed=4.1&bss_speed=4.1&car_speed=16.8&min_nb_journeys=1&max_nb_journeys=1&count=1&max_nb_transfers=10&min_nb_transfers=0&max_duration=86400&wheelchair=False&direct_path=indifferent&debug=False&free_radius_from=0&free_radius_to=0&timeframe_duration=0&is_journey_schedules=False&from=foo&park_mode=none&add_poi_infos[]=bss_stands&add_poi_infos[]=car_parks"

    # When
    journeys_apis.list_journeys(
        datetime_=datetime(2024, 6, 1),
        from_="foo",
        add_poi_infos=["bss_stands", "car_parks"],
    )

    # Then
    mock_get_navitia_api.assert_called_with(expected_url)
