import json
import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.response.company import Company
from navitia_client.entities.request.public_transportations import CompanyRequest
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
    with open("tests/test_data/company.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    companies, _ = company_apis.list_entity_collection_from_region(
        "tuz", CompanyRequest()
    )

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
    companies, _ = company_apis.get_entity_by_id("tuz", "1", CompanyRequest())

    # Then
    assert len(companies) == 1
    assert isinstance(companies[0], Company)
