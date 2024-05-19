from dataclasses import dataclass
from typing import Any, Sequence

from navitia_client.entities.line_and_route import Line
from navitia_client.entities.pt_object import PtObject


@dataclass
class LineReport:
    line: Line
    pt_objets: Sequence[PtObject]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "LineReport":
        return cls(
            line=Line.from_payload(payload["line"]),
            pt_objets=[PtObject.from_payload(data) for data in payload["pt_objects"]],
        )
