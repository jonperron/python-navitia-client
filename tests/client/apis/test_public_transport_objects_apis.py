import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.public_transport_objects_apis import (
    PublicTransportObjectsApiClient,
)
from navitia_client.entities.pt_object import PtObject


@pytest.fixture
def pt_objects_apis():
    return PublicTransportObjectsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(PublicTransportObjectsApiClient, "get_navitia_api")
def test_list_objects(
    mock_get_navitia_api: MagicMock, pt_objects_apis: PublicTransportObjectsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open(
        "tests/test_data/public_transport_objects.json", encoding="utf-8"
    ) as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    pt_objects = pt_objects_apis.list_public_transport_objects(
        region_id="bar", query="REMY"
    )

    # Then
    assert len(pt_objects) == 1
    assert isinstance(pt_objects[0], PtObject)
