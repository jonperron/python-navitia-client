import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.equipment_report_apis import EquipmentReportsApiClient
from navitia_client.entities.request.equipment_report import EquipmentReportRequest


@pytest.fixture
def equipment_report_apis():
    return EquipmentReportsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(EquipmentReportsApiClient, "get_navitia_api")
def test_list_equipment_reports(
    mock_get_navitia_api: MagicMock, equipment_report_apis: EquipmentReportsApiClient
) -> None:
    """
    Test that list_equipment_reports returns equipment reports and pagination.
    """
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/equipment_reports.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    equipment_reports, pagination = equipment_report_apis.list_equipment_reports(
        region_id="fr-idf", request=EquipmentReportRequest()
    )

    # Then
    assert len(equipment_reports) == 2
    assert equipment_reports[0].line is not None
    assert len(equipment_reports[0].stop_area_equipments) > 0
    assert pagination.total_result == 2
    assert pagination.items_on_page == 2


@patch.object(EquipmentReportsApiClient, "get_navitia_api")
def test_list_equipment_reports_with_resource_path(
    mock_get_navitia_api: MagicMock, equipment_report_apis: EquipmentReportsApiClient
) -> None:
    """
    Test that list_equipment_reports_with_resource_path returns equipment reports for a specific resource path.
    """
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/equipment_reports.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    equipment_reports, pagination = (
        equipment_report_apis.list_equipment_reports_with_resource_path(
            region_id="fr-idf",
            resource_path="lines/line:IDFM:C01742",
            request=EquipmentReportRequest(),
        )
    )

    # Then
    called_url = mock_get_navitia_api.call_args[0][0]
    assert "lines/line:IDFM:C01742/equipment_reports" in called_url
    assert len(equipment_reports) == 2
    assert equipment_reports[0].line is not None
    assert len(equipment_reports[0].stop_area_equipments) > 0
    assert pagination.total_result == 2
    assert pagination.items_on_page == 2
