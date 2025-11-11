# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-11-11

### ⚠️ BREAKING CHANGES

This is a major version release with significant API changes. All API client methods now require Request objects instead of individual parameters, which provides better type safety and more maintainable code.

**Migration Guide:**

Before (v1.x):
```python
# Old way with individual parameters
journeys = client.journeys.list_journeys(
    from_="stop_area:RAT:SA:GDLYO",
    to_="stop_area:RAT:SA:CHDEG",
    datetime_=datetime(2024, 6, 1, 8, 0),
    count=5
)
```

After (v2.0):
```python
from navitia_client.entities.request.journey import JourneyRequest

# New way with Request objects
request = JourneyRequest(
    from_="stop_area:RAT:SA:GDLYO",
    to_="stop_area:RAT:SA:CHDEG",
    datetime_=datetime(2024, 6, 1, 8, 0),
    count=5
)
journeys = client.journeys.list_journeys(request=request)
```

### Added

- **Request Objects for All APIs**: Introduced dedicated request classes for all API endpoints:
  - `JourneyRequest` for journey queries
  - `PlacesNearbyRequest` for places nearby queries
  - `ArrivalRequest` for arrival queries
  - `DepartureRequest` for departure queries
  - `EquipmentReportRequest` for equipment report queries
  - `FreefloatingsNearbyRequest` for freefloatings nearby queries
  - `IsochoneRequest` for isochrone queries
  - `LineReportRequest` for line report queries
  - `TrafficReportRequest` for traffic report queries
  - `RouteScheduleRequest` for route schedule queries
  - `StopScheduleRequest` for stop schedule queries
  - `TerminusScheduleRequest` for terminus schedule queries
  - Request classes for all PT (Public Transportation) APIs

### Changed

- **API Method Signatures**: All API client methods now accept Request objects instead of multiple individual parameters
  - Public Transportation APIs (lines, routes, stops, networks, etc.)
  - Journey APIs
  - Places and geocoding APIs
  - Schedule APIs (route schedules, stop schedules, terminus schedules)
  - Report APIs (line reports, traffic reports, equipment reports)
  - Arrival and departure APIs
  - Isochrone APIs
  - Freefloatings nearby APIs

- **Entity Organization**: Moved all entity classes to `response` namespace for better organization
  - Entities are now under `navitia_client.entities.response.*`
  - Request entities are under `navitia_client.entities.request.*`
  - This provides clearer separation between request and response models

- **Documentation**: Updated documentation for all PT API clients to reflect the new Request object pattern

### Fixed

- Fixed workflow configuration for automatic releases ([#91](https://github.com/jonperron/python-navitia-client/pull/91))
- Ensured consistent use of request objects across all API clients ([#97](https://github.com/jonperron/python-navitia-client/pull/97))

### Pull Requests

- fix(workflow): fix workflow to autorelease by @jonperron in [#91](https://github.com/jonperron/python-navitia-client/pull/91)
- chore(refacto): move all entities to response entities by @jonperron in [#93](https://github.com/jonperron/python-navitia-client/pull/93)
- feat(api): replace dict by request objects for non-pt APIs by @jonperron in [#94](https://github.com/jonperron/python-navitia-client/pull/94)
- feat(api): replace dict by request objects for pt APIs by @jonperron in [#95](https://github.com/jonperron/python-navitia-client/pull/95)
- chore(doc): update doc for all pt api clients by @jonperron in [#96](https://github.com/jonperron/python-navitia-client/pull/96)
- fix(api): use request objects in all api clients by @jonperron in [#97](https://github.com/jonperron/python-navitia-client/pull/97)

### Benefits of This Release

1. **Type Safety**: Request objects provide better IDE autocomplete and type checking
2. **Maintainability**: Easier to add new parameters without changing method signatures
3. **Documentation**: Request objects are self-documenting with clear parameter descriptions
4. **Validation**: Centralized parameter validation in request classes
5. **Testing**: Simplified testing with reusable request objects

### Upgrading

To upgrade from v1.x to v2.0:

1. Update your imports to include the required Request classes:
   ```python
   from navitia_client.entities.request.journey import JourneyRequest
   from navitia_client.entities.request.places_nearby import PlacesNearbyRequest
   # etc.
   ```

2. Replace method calls with individual parameters with Request objects:
   ```python
   # Create a request object
   request = JourneyRequest(from_="...", to_="...", count=5)

   # Pass it to the API method
   result = client.journeys.list_journeys(request=request)
   ```

3. Update imports for response entities if you were importing them directly:
   ```python
   # Old
   from navitia_client.entities.journey import Journey

   # New
   from navitia_client.entities.response.journey import Journey
   # Or simply
   from navitia_client.entities.response import Journey
   ```

For detailed API documentation, see the [docs/api_support](docs/api_support/) directory.

---

## [1.3.0] and earlier

See [GitHub Releases](https://github.com/jonperron/python-navitia-client/releases) for previous versions.
