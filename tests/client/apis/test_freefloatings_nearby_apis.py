import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.freefloatings_nearby_apis import (
    FreefloatingsNearbyApiClient,
)


@pytest.fixture
def freefloatings_nearby_apis():
    return FreefloatingsNearbyApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(FreefloatingsNearbyApiClient, "get_navitia_api")
def test_list_freefloatings_nearby(
    mock_get_navitia_api: MagicMock,
    freefloatings_nearby_apis: FreefloatingsNearbyApiClient,
) -> None:
    """
    Test that list_freefloatings_nearby returns free floatings and pagination.
    """
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/freefloatings_nearby.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    free_floatings, pagination = freefloatings_nearby_apis.list_freefloatings_nearby(
        region_id="fr-idf", lon=2.3522, lat=48.8566
    )

    # Then
    assert len(free_floatings) == 2
    assert free_floatings[0].public_id == "scooter_12345"
    assert free_floatings[0].provider_name == "Lime"
    assert free_floatings[0].type == "scooter"
    assert free_floatings[0].propulsion == "electric"
    assert free_floatings[0].battery == 85
    assert free_floatings[0].distance == 120
    assert free_floatings[0].coord is not None
    assert free_floatings[0].coord.lat == "48.8560"
    assert free_floatings[0].coord.lon == "2.3500"
    assert pagination.total_result == 2
    assert pagination.items_on_page == 2


@patch.object(FreefloatingsNearbyApiClient, "get_navitia_api")
def test_list_freefloatings_nearby_with_resource_path(
    mock_get_navitia_api: MagicMock,
    freefloatings_nearby_apis: FreefloatingsNearbyApiClient,
) -> None:
    """
    Test that list_freefloatings_nearby_with_resource_path returns free floatings for a specific resource path.
    """
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/freefloatings_nearby.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    (
        free_floatings,
        pagination,
    ) = freefloatings_nearby_apis.list_freefloatings_nearby_with_resource_path(
        region_id="fr-idf", resource_path="stop_areas/stop_area:IDFM:71591"
    )

    # Then
    called_url = mock_get_navitia_api.call_args[0][0]
    assert "stop_areas/stop_area:IDFM:71591/freefloatings_nearby" in called_url
    assert len(free_floatings) == 2
    assert free_floatings[0].public_id == "scooter_12345"
    assert free_floatings[0].type == "scooter"
    assert free_floatings[1].type == "bike"
    assert pagination.total_result == 2
    assert pagination.items_on_page == 2


@patch.object(FreefloatingsNearbyApiClient, "get_navitia_api")
def test_list_freefloatings_nearby_by_coordinates(
    mock_get_navitia_api: MagicMock,
    freefloatings_nearby_apis: FreefloatingsNearbyApiClient,
) -> None:
    """
    Test that list_freefloatings_nearby_by_coordinates returns free floatings with region coordinates.
    """
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/freefloatings_nearby.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    (
        free_floatings,
        pagination,
    ) = freefloatings_nearby_apis.list_freefloatings_nearby_by_coordinates(
        region_lon=2.3522, region_lat=48.8566, lon=2.3522, lat=48.8566
    )

    # Then
    called_url = mock_get_navitia_api.call_args[0][0]
    assert (
        "coverage/2.3522;48.8566/coords/2.3522;48.8566/freefloatings_nearby"
        in called_url
    )
    assert len(free_floatings) == 2
    assert free_floatings[0].provider_name == "Lime"
    assert pagination.total_result == 2


@patch.object(FreefloatingsNearbyApiClient, "get_navitia_api")
def test_list_freefloatings_nearby_by_coordinates_only(
    mock_get_navitia_api: MagicMock,
    freefloatings_nearby_apis: FreefloatingsNearbyApiClient,
) -> None:
    """
    Test that list_freefloatings_nearby_by_coordinates_only returns free floatings without region id.
    """
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/freefloatings_nearby.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    (
        free_floatings,
        pagination,
    ) = freefloatings_nearby_apis.list_freefloatings_nearby_by_coordinates_only(
        lon=2.3522, lat=48.8566
    )

    # Then
    called_url = mock_get_navitia_api.call_args[0][0]
    assert "coord/2.3522;48.8566/freefloatings_nearby" in called_url
    assert len(free_floatings) == 2
    assert free_floatings[0].type == "scooter"
    assert free_floatings[1].type == "bike"
    assert pagination.total_result == 2
