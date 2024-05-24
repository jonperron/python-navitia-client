import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.isochrone_apis import IsochronesApiClient
from navitia_client.entities.isochrones import Isochrone


@pytest.fixture
def isochrones_apis():
    return IsochronesApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(IsochronesApiClient, "get_navitia_api")
def test_list_covered_areas_with_region_id(
    mock_get_navitia_api: MagicMock, isochrones_apis: IsochronesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/isochrones.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    isocrhones = isochrones_apis.list_isochrones_with_region_id(
        region_id="bar", from_="foo"
    )

    # Then
    assert len(isocrhones) == 1
    assert isinstance(isocrhones[0], Isochrone)


@patch.object(IsochronesApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, isochrones_apis: IsochronesApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/isochrones.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    isocrhones = isochrones_apis.list_isochrones(from_="foo")

    # Then
    assert len(isocrhones) == 1
    assert isinstance(isocrhones[0], Isochrone)
