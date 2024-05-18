from dataclasses import dataclass
from typing import Any
from navitia_client.entities.display_information import DisplayInformation
from navitia_client.entities.schedule_table import ScheduleTable


@dataclass
class RouteSchedule:
    display_informations: DisplayInformation
    table: ScheduleTable

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "RouteSchedule":
        return cls(
            display_informations=DisplayInformation.from_json(
                payload["display_informations"]
            ),
            table=ScheduleTable.from_json(payload["table"]),
        )
