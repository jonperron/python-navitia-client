import pytest
from requests import Response  # type: ignore
from navitia_client.client.apis.api_base_client import ApiBaseClient
from navitia_client.client.exceptions import (
    NavitiaAccessTokenMissingError,
    NavitiaForbiddenAccessError,
    NavitiaUnableToParseError,
    NavitiaUnknownObjectError,
)


def test_http_base_client() -> None:
    # Given
    auth_token = "foobar"

    # When
    client = ApiBaseClient(
        auth_token=auth_token, base_navitia_url="https://api.navitia.io/v1/"
    )

    # Then
    assert isinstance(client, ApiBaseClient)


@pytest.fixture
def api_base_client():
    return ApiBaseClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


def test_check_response_for_exception(api_base_client: ApiBaseClient) -> None:
    # Given
    response = Response()
    response._content = (
        b'{"error": {"id": "unknown_object", "message": "Unable to find place: 0;0"}}'
    )
    # When/Then
    with pytest.raises(NavitiaUnknownObjectError):
        api_base_client._check_response_for_exception(response)

    # Given
    response = Response()
    response._content = (
        b'{"error": {"id": "unable_to_parse", "message": "Unable to parse : {0;0}"}}'
    )
    # When/Then
    with pytest.raises(NavitiaUnableToParseError):
        api_base_client._check_response_for_exception(response)

    # Given
    response = Response()
    response._content = b'{"message": "no token"}'
    # When/Then
    with pytest.raises(NavitiaAccessTokenMissingError):
        api_base_client._check_response_for_exception(response)

    # Given
    response = Response()
    response._content = (
        b'{"message": "It is either read-protected or not readable by the server."}'
    )
    # When/Then
    with pytest.raises(NavitiaForbiddenAccessError):
        api_base_client._check_response_for_exception(response)


def test_generate_filter_query(api_base_client: ApiBaseClient) -> None:
    # Given
    filters = {
        "start_page": 0,
        "count": 25,
        "depth": 1,
    }

    expected_filters_string = "?start_page=0&count=25&depth=1"

    # When
    generated_filters_string = api_base_client._generate_filter_query(filters)

    # Then
    assert expected_filters_string == generated_filters_string


def test_generate_filter_query_no_filters(api_base_client: ApiBaseClient) -> None:
    # Given
    filters = {}  # type: ignore

    expected_filters_string = ""

    # When
    generated_filters_string = api_base_client._generate_filter_query(filters)

    # Then
    assert expected_filters_string == generated_filters_string


def test_generate_filter_query_arg_is_list(api_base_client: ApiBaseClient) -> None:
    # Given
    filters = {
        "start_page": 0,
        "count": 25,
        "depth": 1,
        "type[]": ["stop_point", "stop_area"],
    }

    expected_filters_string = (
        "?start_page=0&count=25&depth=1&type[]=stop_point&type[]=stop_area"
    )

    # When
    generated_filters_string = api_base_client._generate_filter_query(filters)

    # Then
    assert expected_filters_string == generated_filters_string


def test_generate_filter_query_arg_list_is_empty(
    api_base_client: ApiBaseClient,
) -> None:
    # Given
    filters = {"start_page": 0, "count": 25, "depth": 1, "type[]": []}

    expected_filters_string = "?start_page=0&count=25&depth=1"

    # When
    generated_filters_string = api_base_client._generate_filter_query(filters)

    # Then
    assert expected_filters_string == generated_filters_string
