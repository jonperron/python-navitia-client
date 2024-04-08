from dataclasses import dataclass
from typing import Any, Optional, Sequence


from .base_entity import BaseEntity
from .coord import Coord
from .administrative_region import AdministrativeRegion


@dataclass
class StopArea(BaseEntity):
    label: str
    coord: Coord
    administrative_regions: Optional[Sequence[AdministrativeRegion]]
    stop_points: Optional[Sequence["StopPoint"]]

    @staticmethod
    def from_json(payload: dict[str, Any]) -> "StopArea":
        administrative_regions = (
            [
                AdministrativeRegion.from_json(region)
                for region in payload["administrative_regions"]
            ]
            if "administrative_regions" in payload
            else None
        )

        stop_points = (
            [StopPoint.from_json(stop_point) for stop_point in payload["stop_points"]]
            if "stop_points" in payload
            else None
        )

        return StopArea(
            id=payload["id"],
            name=payload["name"],
            label=payload["label"],
            coord=Coord.from_json(payload["coord"]),
            administrative_regions=administrative_regions,
            stop_points=stop_points,
        )


@dataclass
class StopPoint(BaseEntity):
    label: str
    coord: Coord
    administrative_regions: Optional[Sequence[AdministrativeRegion]]
    equipments: Sequence[str]
    stop_area: Optional[StopArea]

    @staticmethod
    def from_json(
        payload: dict[str, Any],
    ) -> "StopPoint":
        administrative_regions = (
            [
                AdministrativeRegion.from_json(region)
                for region in payload["administrative_regions"]
            ]
            if "administrative_regions" in payload
            else None
        )

        stop_area = (
            StopArea.from_json(payload["stop_area"]) if "stop_area" in payload else None
        )

        return StopPoint(
            id=payload["id"],
            name=payload["name"],
            label=payload["label"],
            coord=Coord.from_json(payload["coord"]),
            administrative_regions=administrative_regions,
            equipments=payload["equipments"],
            stop_area=stop_area,
        )
