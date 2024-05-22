import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.journeys_apis import JourneyApiClient
from navitia_client.entities.journey import Journey


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
