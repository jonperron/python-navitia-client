from navitia_client.client.base_client import HttpBaseClient


def test_http_base_client() -> None:
    # Given
    auth_token = "foobar"

    # When
    client = HttpBaseClient(auth_token=auth_token)

    # Then
    assert isinstance(client, HttpBaseClient)
