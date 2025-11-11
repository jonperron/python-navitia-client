from datetime import datetime
import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.coverage_apis import CoverageApiClient
from navitia_client.entities.response.administrative_region import Region
from navitia_client.entities.response import Pagination


@pytest.fixture
def coverage_apis():
    return CoverageApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(CoverageApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, coverage_apis: CoverageApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/coverage.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    regions, pagination = coverage_apis.list_covered_areas()

    # Then
    assert len(regions) == 1
    assert isinstance(regions[0], Region)
    assert regions[0].id == "region1"
    assert regions[0].name == "Region 1"
    assert regions[0].dataset_created_at == datetime(2022, 1, 1, 0, 0)
    assert regions[0].end_production_date == datetime(2022, 12, 31, 0, 0)
    assert regions[0].last_load_at == datetime(2022, 1, 1, 0, 0)
    assert regions[0].shape == "shape_data"
    assert regions[0].start_production_date == datetime(2022, 1, 1, 0, 0)
    assert regions[0].status == "active"
    assert isinstance(pagination, Pagination)


@patch.object(CoverageApiClient, "get_navitia_api")
def test_get_region_by_id(
    mock_get_navitia_api: MagicMock, coverage_apis: CoverageApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "regions": [
            {
                "id": "region1",
                "name": "Region 1",
                "dataset_created_at": "2022-01-01T00:00:00",
                "end_production_date": "20221231",
                "last_load_at": "2022-01-01T00:00:00",
                "shape": "shape_data",
                "start_production_date": "20220101",
                "status": "active",
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
    regions, pagination = coverage_apis.get_coverage_by_region_id("12")

    # Then
    assert len(regions) == 1
    assert isinstance(regions[0], Region)
    assert isinstance(pagination, Pagination)


@patch.object(CoverageApiClient, "get_navitia_api")
def test_get_region_by_coordinates(
    mock_get_navitia_api: MagicMock, coverage_apis: CoverageApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "regions": [
            {
                "id": "region1",
                "name": "Region 1",
                "dataset_created_at": "2022-01-01T00:00:00",
                "end_production_date": "20221231",
                "last_load_at": "2022-01-01T00:00:00",
                "shape": "shape_data",
                "start_production_date": "20220101",
                "status": "active",
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
    regions, pagination = (
        coverage_apis.get_coverage_by_region_coordinates_and_coordinates(12.5, 13.2)
    )

    # Then
    assert len(regions) == 1
    assert isinstance(regions[0], Region)
    assert isinstance(pagination, Pagination)
