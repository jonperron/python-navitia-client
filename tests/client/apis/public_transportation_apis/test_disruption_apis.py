import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.disruption import Disruption
from navitia_client.client.apis.public_transportation_apis import DisruptionApiClient


@pytest.fixture
def disruption_apis():
    return DisruptionApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(DisruptionApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, disruption_apis: DisruptionApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/disruption.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    disruptions, _ = disruption_apis.list_entity_collection_from_region("tuz")

    # Then
    assert len(disruptions) == 3
    assert isinstance(disruptions[0], Disruption)


@patch.object(DisruptionApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, disruption_apis: DisruptionApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/disruption.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    disruptions, _ = disruption_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(disruptions) == 3
    assert isinstance(disruptions[0], Disruption)
