from dataclasses import dataclass


from navitia_client.entities.request.base_entity_request import BasePTEntityRequest


@dataclass
class VehicleJourneyRequest(BasePTEntityRequest):
    """
    Request class for VehicleJourney entity queries.

    Inherits all parameters from BasePTEntityRequest:
    - count: Maximum number of results (default is 10)
    - start_page: Page number to start from (default is 0)
    - depth: Search depth (default is 1)
    - odt: ODT type filter (default is "all")
    - distance: Maximum search distance (default is 200)
    - headsign: Optional line headsign
    - since: Optional datetime filter (for vehicle_journeys and disruptions)
    - until: Optional datetime filter (for vehicle_journeys and disruptions)
    - disable_geojson: Whether to disable GeoJSON in response (default is False)
    - disable_disruption: Whether to disable disruption info (default is False)
    """

    pass
