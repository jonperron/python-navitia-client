import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.physical_mode import PhysicalMode
from navitia_client.entities.request.public_transportations import PhysicalModeRequest
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
    with open("tests/test_data/physical_mode.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    physical_modes, _ = physical_modes_apis.list_entity_collection_from_region(
        "tuz", PhysicalModeRequest()
    )

    # Then
    assert len(physical_modes) == 3
    assert isinstance(physical_modes[1], PhysicalMode)


@patch.object(PhysicalModeApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, physical_modes_apis: PhysicalModeApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/physical_mode.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    physical_modes, _ = physical_modes_apis.get_entity_by_id(
        "tuz", "1", PhysicalModeRequest()
    )

    # Then
    assert len(physical_modes) == 3
    assert isinstance(physical_modes[0], PhysicalMode)
