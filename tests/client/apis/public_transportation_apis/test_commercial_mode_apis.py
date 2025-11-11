import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.physical_mode import CommercialMode
from navitia_client.entities.request.public_transportations import CommercialModeRequest
from navitia_client.client.apis.public_transportation_apis import (
    CommercialModeApiClient,
)


@pytest.fixture
def commercial_modes_apis():
    return CommercialModeApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(CommercialModeApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, commercial_modes_apis: CommercialModeApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/commercial_mode.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    commercial_modes, _ = commercial_modes_apis.list_entity_collection_from_region(
        "tuz", CommercialModeRequest()
    )

    # Then
    assert len(commercial_modes) == 2
    assert isinstance(commercial_modes[1], CommercialMode)


@patch.object(CommercialModeApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, commercial_modes_apis: CommercialModeApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/commercial_mode.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    commercial_modes, _ = commercial_modes_apis.get_entity_by_id(
        "tuz", "1", CommercialModeRequest()
    )

    # Then
    assert len(commercial_modes) == 2
    assert isinstance(commercial_modes[0], CommercialMode)
