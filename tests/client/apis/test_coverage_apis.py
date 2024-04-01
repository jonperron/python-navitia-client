from unittest.mock import MagicMock
import pytest

from navitia_client.client.apis.coverage_apis import CoverageApis
from navitia_client.entities import Region


@pytest.patch("navitia_client.client.apis.coverage_apis.CoverageApis")
def test_list_covered_areas(coverage_apis_mock: MagicMock) -> None:
    # Given
    coverage_apis_mock._get_navitia_api.return_value = {
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
            }
        ]
    }
    regions = coverage_apis.list_covered_areas()
    assert len(regions) == 1
    assert isinstance(regions[0], Region)


def test_get_region_by_id(mock_session, coverage_apis):
    mock_response = {
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
            }
        ]
    }
    mock_session.get.return_value.json.return_value = mock_response
    regions = coverage_apis.get_region_by_id("foobar")
    assert len(regions) == 1
    assert isinstance(regions[0], Region)


def test_get_region_by_coordinates(mock_session, coverage_apis):
    mock_response = {
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
            }
        ]
    }
    mock_session.get.return_value.json.return_value = mock_response
    regions = coverage_apis.get_region_by_coordinates(12.5, 13.2)
    assert len(regions) == 1
    assert isinstance(regions[0], Region)
