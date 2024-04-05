from navitia_client.client.apis.api_base_client import ApiBaseClient


def test_http_base_client() -> None:
    # Given
    auth_token = "foobar"

    # When
    client = ApiBaseClient(
        auth_token=auth_token, base_navitia_url="https://api.navitia.io/v1/"
    )

    # Then
    assert isinstance(client, ApiBaseClient)
