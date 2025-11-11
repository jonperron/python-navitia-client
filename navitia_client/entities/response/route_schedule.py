from dataclasses import dataclass
from typing import Any
from navitia_client.entities.response.display_information import DisplayInformation
from navitia_client.entities.response.schedule_table import ScheduleTable


@dataclass
class RouteSchedule:
    display_informations: DisplayInformation
    table: ScheduleTable

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "RouteSchedule":
        return cls(
            display_informations=DisplayInformation.from_payload(
                payload["display_informations"]
            ),
            table=ScheduleTable.from_payload(payload["table"]),
        )
