import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.physical_mode import PhysicalMode
from navitia_client.client.apis.public_transportation_apis import (
    PhysicalModeApiClient,
)


@pytest.fixture
def physical_modes_apis():
    return PhysicalModeApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(PhysicalModeApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, physical_modes_apis: PhysicalModeApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "physical_modes": [
            {
                "co2_emission_rate": {"unit": "gEC/Km", "value": 0.0},
                "id": "physical_mode:Bike",
                "name": "Bike",
            },
            {
                "co2_emission_rate": {"unit": "gEC/Km", "value": 0.0},
                "id": "physical_mode:BikeSharingService",
                "name": "BikeSharingService",
            },
            {
                "co2_emission_rate": {"unit": "gEC/Km", "value": 132.0},
                "id": "physical_mode:Bus",
                "name": "Bus",
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
    physical_modes, _ = physical_modes_apis.list_entity_collection_from_region("tuz")

    # Then
    assert len(physical_modes) == 3
    assert isinstance(physical_modes[1], PhysicalMode)


@patch.object(PhysicalModeApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, physical_modes_apis: PhysicalModeApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "physical_modes": [
            {
                "co2_emission_rate": {"unit": "gEC/Km", "value": 0.0},
                "id": "physical_mode:Bike",
                "name": "Bike",
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
    physical_modes, _ = physical_modes_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(physical_modes) == 1
    assert isinstance(physical_modes[0], PhysicalMode)
