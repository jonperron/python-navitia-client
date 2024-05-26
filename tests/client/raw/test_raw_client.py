import pytest
from unittest.mock import MagicMock, patch


from navitia_client.client.raw.raw_client import RawClient


@pytest.fixture
def raw_client():
    auth_token = "test_token"
    base_navitia_url = "http://api.navitia.io"
    return RawClient(auth_token, base_navitia_url)


def test_generate_filter_query_empty(raw_client):
    # Given
    filters = {}

    # When
    result = raw_client._generate_filter_query(filters)

    # Then
    assert result == ""


def test_generate_filter_query_with_filters(raw_client):
    # Given
    filters = {"key1": "value1", "key2": "value2"}

    # When
    result = raw_client._generate_filter_query(filters)

    # Then
    assert result == "?key1=value1&key2=value2"


@patch.object(RawClient, "call_api")
def test_call_api(mock_raw_client_call_api, raw_client):
    # Given
    endpoint = "coverage"
    filters = {"key1": "value1", "key2": "value2"}

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"dummy": "data"}

    mock_raw_client_call_api.return_value = mock_response

    # When
    response = raw_client.call_api(endpoint, filters)

    # Then
    assert response.status_code == 200
    assert response.json() == {"dummy": "data"}
