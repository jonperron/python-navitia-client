import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.company import Company
from navitia_client.client.apis.public_transportation_apis import CompanyApiClient


@pytest.fixture
def company_apis():
    return CompanyApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(CompanyApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, company_apis: CompanyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "companies": [
            {
                "codes": [{"type": "source", "value": "12"}],
                "id": "company:foo:0012",
                "name": "Foo gmbh",
            }
        ]
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    companies = company_apis.list_entity_collection_from_region("tuz")

    # Then
    assert len(companies) == 1
    assert isinstance(companies[0], Company)


@patch.object(CompanyApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, company_apis: CompanyApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "companies": [
            {
                "codes": [{"type": "source", "value": "12"}],
                "id": "company:foo:0012",
                "name": "Foo gmbh",
            }
        ]
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    networks = company_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(networks) == 1
    assert isinstance(networks[0], Company)
