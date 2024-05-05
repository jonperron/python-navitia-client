from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.datasets_apis import DatasetsApiClient
from navitia_client.entities.dataset import Dataset


@pytest.fixture
def datasets_apis():
    return DatasetsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(DatasetsApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, datasets_apis: DatasetsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "datasets": [
            {
                "contributor": {
                    "id": "foo:foo-piv",
                    "license": "Private",
                    "name": "foo Production",
                    "website": "",
                },
                "description": "",
                "end_validation_date": "20240428T020000",
                "id": "foo:xxx",
                "realtime_level": "base_schedule",
                "start_validation_date": "20240405T020000",
                "system": "",
            }
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
    datasets, _ = datasets_apis.list_datasets(region_id="bar")

    # Then
    assert len(datasets) == 1
    assert isinstance(datasets[0], Dataset)
    assert datasets[0].description == ""
    assert datasets[0].start_validation_date == datetime(2024, 4, 5, 2, 0, 0)
    assert datasets[0].end_validation_date == datetime(2024, 4, 28, 2, 0, 0)
    assert datasets[0].id == "foo:xxx"
    assert datasets[0].realtime_level == "base_schedule"
    assert datasets[0].system == ""
    contributor = datasets[0].contributor
    assert contributor.name == "foo Production"
    assert contributor.id == "foo:foo-piv"
    assert contributor.license == "Private"
    assert contributor.website == ""


@patch.object(DatasetsApiClient, "get_navitia_api")
def test_get_region_by_id(
    mock_get_navitia_api: MagicMock, datasets_apis: DatasetsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "datasets": [
            {
                "contributor": {
                    "id": "foo:foo-piv",
                    "license": "Private",
                    "name": "foo Production",
                    "website": "",
                },
                "description": "",
                "end_validation_date": "20240428T020000",
                "id": "foo:xxx",
                "realtime_level": "base_schedule",
                "start_validation_date": "20240405T020000",
                "system": "",
            }
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
    datasets, _ = datasets_apis.get_dataset_by_id(
        region_id="bar", dataset_id="foo:foo-piv"
    )

    # Then
    assert len(datasets) == 1
    assert isinstance(datasets[0], Dataset)


@patch.object(DatasetsApiClient, "get_navitia_api")
def test_get_region_by_id_missing_contributor(
    mock_get_navitia_api: MagicMock, datasets_apis: DatasetsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "datasets": [
            {
                "description": "",
                "end_validation_date": "20240428T020000",
                "id": "foo:xxx",
                "realtime_level": "base_schedule",
                "start_validation_date": "20240405T020000",
                "system": "",
            }
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
    datasets, _ = datasets_apis.get_dataset_by_id(
        region_id="bar", dataset_id="foo:foo-piv"
    )

    # Then
    assert len(datasets) == 0
