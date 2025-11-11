import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.contributors_apis import ContributorsApiClient
from navitia_client.entities.response.contributor import Contributor
from navitia_client.entities.response import Pagination


@pytest.fixture
def contributors_apis():
    return ContributorsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(ContributorsApiClient, "get_navitia_api")
def test_list_contributors(
    mock_get_navitia_api: MagicMock, contributors_apis: ContributorsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/contributors.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    contributors, pagination = contributors_apis.list_contributors(region_id="bar")

    # Then
    assert len(contributors) == 1
    assert isinstance(contributors[0], Contributor)
    assert contributors[0].name == "foo Production"
    assert contributors[0].id == "foo:foo-piv"
    assert contributors[0].license == "Private"
    assert contributors[0].website == ""
    assert isinstance(pagination, Pagination)


@patch.object(ContributorsApiClient, "get_navitia_api")
def test_get_region_by_id(
    mock_get_navitia_api: MagicMock, contributors_apis: ContributorsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/contributors.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)
    mock_get_navitia_api.return_value = mock_response

    # When
    contributors, _ = contributors_apis.get_contributor_on_dataset(
        region_id="bar", dataset_id="foo:xxx"
    )

    # Then
    assert len(contributors) == 1
    assert isinstance(contributors[0], Contributor)
    assert contributors[0].name == "foo Production"
    assert contributors[0].id == "foo:foo-piv"
    assert contributors[0].license == "Private"
    assert contributors[0].website == ""
