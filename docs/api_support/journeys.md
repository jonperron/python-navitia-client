# Journeys

A client class to interact with the Navitia API for fetching journey data.

Official documentation: <https://doc.navitia.io/#journeys>

Property: `NavitiaClient.journeys`

Methods

```python

    list_journeys(
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Sequence[str] = [],
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0
    ) -> Sequence[Journey]
        Fetches journey data based on various parameters.

    list_journeys_with_region_id(
        self,
        region_id: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Sequence[str] = [],
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0
    ) -> Sequence[Journey]
        Fetches journey data for a specific region based on various parameters.

    list_journeys_with_resource_path(
        self,
        resource_path: str,
        from_: Optional[str] = None,
        to_: Optional[str] = None,
        datetime_: datetime = datetime.now(),
        datetime_represents: str = "departure",
        traveler_type: str = "standard",
        data_freshness: str = "realtime",
        forbidden_uris: Optional[Sequence[str]] = None,
        allowed_id: Optional[Sequence[str]] = None,
        first_section_mode: Optional[Sequence[str]] = None,
        last_section_mode: Optional[Sequence[str]] = None,
        language: str = "en-GB",
        depth: int = 1,
        max_duration_to_pt: int = 30 * 60,
        walking_speed: float = 1.12,
        bike_speed: float = 4.1,
        bss_speed: float = 4.1,
        car_speed: float = 16.8,
        min_nb_journeys: int = 1,
        max_nb_journeys: int = 1,
        count: int = 1,
        max_nb_transfers: int = 10,
        min_nb_transfers: int = 0,
        max_duration: int = 86400,
        wheelchair: bool = False,
        direct_path: str = "indifferent",
        direct_path_mode: Optional[Sequence[str]] = None,
        add_poi_infos: Sequence[str] = [],
        debug: bool = False,
        free_radius_from: int = 0,
        free_radius_to: int = 0,
        timeframe_duration: int = 0
    ) -> Sequence[Journey]
        Fetches journey data for a specific resource path based on various parameters.
```
