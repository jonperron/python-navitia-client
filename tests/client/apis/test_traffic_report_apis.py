import json
from unittest.mock import MagicMock, patch

import pytest

from navitia_client.client.apis.traffic_report_apis import TrafficReportsApiClient
from navitia_client.entities.response.disruption import Disruption
from navitia_client.entities.response.traffic_report import TrafficReport


@pytest.fixture
def traffic_reports_apis():
    return TrafficReportsApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(TrafficReportsApiClient, "get_navitia_api")
def test_list_covered_areas(
    mock_get_navitia_api: MagicMock, traffic_reports_apis: TrafficReportsApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    with open("tests/test_data/traffic_reports.json", encoding="utf-8") as file:
        mock_response.json.return_value = json.load(file)

    mock_get_navitia_api.return_value = mock_response

    # When
    disruptions, traffic_report, _ = traffic_reports_apis.list_traffic_reports(
        region_id="bar", resource_path="foo"
    )

    # Then
    assert len(disruptions) == 1
    assert isinstance(disruptions[0], Disruption)
    assert len(traffic_report) == 1
    assert isinstance(traffic_report[0], TrafficReport)
