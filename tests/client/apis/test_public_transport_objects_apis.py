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
    mock_response.json.return_value = {
        "pt_objects": [
            {
                "embedded_type": "stop_area",
                "id": "stop_area:SNCF:87758896",
                "name": "Saint-Rémy-lès-Chevreuse (Saint-Rémy-lès-Chevreuse)",
                "quality": 70,
                "stop_area": {
                    "administrative_regions": [
                        {
                            "coord": {"lat": "48.7054888", "lon": "2.071109"},
                            "id": "admin:fr:78575",
                            "insee": "78575",
                            "label": "Saint-Rémy-lès-Chevreuse " "(78470)",
                            "level": 8,
                            "name": "Saint-Rémy-lès-Chevreuse",
                            "zip_code": "78470",
                        }
                    ],
                    "codes": [
                        {"type": "source", "value": "87758896"},
                        {"type": "uic", "value": "87758896"},
                    ],
                    "coord": {"lat": "48.702722", "lon": "2.070924"},
                    "id": "stop_area:SNCF:87758896",
                    "label": "Saint-Rémy-lès-Chevreuse " "(Saint-Rémy-lès-Chevreuse)",
                    "links": [],
                    "name": "Saint-Rémy-lès-Chevreuse",
                    "timezone": "Europe/Paris",
                },
            }
        ],
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    pt_objects = pt_objects_apis.list_public_transport_objects(
        region_id="bar", query="REMY"
    )

    # Then
    assert len(pt_objects) == 1
    assert isinstance(pt_objects[0], PtObject)
