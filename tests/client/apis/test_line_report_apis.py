import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.line_report_apis import LineReportsApiClient
from navitia_client.entities.response.disruption import Disruption
from navitia_client.entities.response.line_report import LineReport


@pytest.fixture
def line_reports_apis():
    return LineReportsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(LineReportsApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, line_reports_apis: LineReportsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/line_report.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    disruptions, line_reports = line_reports_apis.list_line_reports(
        region_id="bar", resource_path="foo"
    )

    # Then
    assert len(disruptions) == 1
    assert isinstance(disruptions[0], Disruption)
    assert len(line_reports) == 1
    assert isinstance(line_reports[0], LineReport)
