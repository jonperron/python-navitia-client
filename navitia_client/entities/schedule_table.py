from dataclasses import dataclass
from typing import Any, Sequence

from navitia_client.entities.display_information import DisplayInformation
from navitia_client.entities.link import Link
from navitia_client.entities.pt_datetime import PTDatetime
from navitia_client.entities.stop_area import StopPoint


@dataclass
class ScheduleTableHeader:
    additional_informations: Sequence[str]
    display_informations: DisplayInformation
    links: Sequence[Link]

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "ScheduleTableHeader":
        return cls(
            additional_informations=[
                additional_information
                for additional_information in payload["additional_informations"]
            ],
            display_informations=DisplayInformation.from_json(
                payload["display_informations"]
            ),
            links=[Link.from_json(link) for link in payload["links"]],
        )


@dataclass
class ScheduleTableRow:
    date_times: Sequence[PTDatetime]
    stop_point: StopPoint

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "ScheduleTableRow":
        return cls(
            date_times=[
                PTDatetime.from_json(date_time) for date_time in payload["date_times"]
            ],
            stop_point=StopPoint.from_json(payload["stop_point"]),
        )


@dataclass
class ScheduleTable:
    headers: Sequence[ScheduleTableHeader]
    rows: Sequence[ScheduleTableRow]

    @classmethod
    def from_json(cls, payload: dict[str, Any]) -> "ScheduleTable":
        return cls(
            headers=[
                ScheduleTableHeader.from_json(table_header)
                for table_header in payload["headers"]
            ],
            rows=[ScheduleTableRow.from_json(row) for row in payload["rows"]],
        )
