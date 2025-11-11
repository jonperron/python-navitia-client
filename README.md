# navitia-client

[![Pre-release Build Status](https://img.shields.io/github/actions/workflow/status/jonperron/python-navitia-client/pre-release.yaml?branch=main)](https://github.com/jonperron/python-navitia-client/actions)
[![Release Build Status](https://img.shields.io/github/actions/workflow/status/jonperron/python-navitia-client/release.yaml?branch=main)](https://github.com/jonperron/python-navitia-client/actions)
[![Python Version](https://img.shields.io/pypi/pyversions/python-navitia-client.svg)](https://pypi.org/project/python-navitia-client/)

This repository provides a unofficial Python wrapper to use [navitia.io APIs](https://doc.navitia.io).

> **⚠️ Version 2.0.0 Breaking Changes**
>
> Version 2.0.0 introduces breaking changes with the adoption of Request objects for all API methods.
> If you're upgrading from v1.x, please see the [CHANGELOG](CHANGELOG.md) for the migration guide.

##  Pre-requisites

To use this library, you will need an access token from [navitia.io](https://navitia.io/tarifs/).

##  Installation

The package is available on PiPy

```bash
pip install python-navitia-client
```

##  API support

The library supports the following [APIs](https://doc.navitia.io/#api-catalog):

| API                                       | Supported ? | Comment                                      |
| ----------------------------------------- | ----------- | -------------------------------------------- |
| Coverage                                  | ✅           |                                              |
| Datasets                                  | ✅           |                                              |
| Contributors                              | ✅           |                                              |
| Inverted geocoding                        | ✅           |                                              |
| Public transportation Objects exploration | ✅           |                                              |
| Autocomplete on Public Transport objects  | ✅           |                                              |
| Autocomplete on geographical objects      | ✅           |                                              |
| Places nearby                             | ✅           |                                              |
| Journeys                                  | ✅           |                                              |
| Isochrones                                | ✅           |                                              |
| Route Schedules                           | ✅           |                                              |
| Stop Schedules                            | ✅           |                                              |
| Terminus Schedules                        | ✅           |                                              |
| Departures                                | ✅           |                                              |
| Arrivals                                  | ✅           |                                              |
| Line reports                              | ✅           |                                              |
| Traffic reports                           | ✅           |                                              |
| Equipment reports                         | ✅           | Not available to all providers               |
| Freefloating nearby                       | ✅           | Not available to all providers               |

## Usage

To use this library, you need an authentication token provided by Navitia.io.

### Create client instance

Create an instance of the NavitiaClient class with your authentication token:

```python
from navitia_client.client import NavitiaClient

client = NavitiaClient(auth="YOUR_TOKEN_HERE")
```

A base URL for Navitia IO is hardcoded and provided to NavitiaClient by default. It can be updated using the `base_navitia_url` parameter.

###  Access APIs data

URLs are mapped as properties in the `NavitiaClient` class. You can find the mapping [here](docs/api_support/).

#### Simple APIs (Coverage, Datasets, Contributors)

For simple APIs like coverage, datasets, and contributors, you can call methods directly:

```python
# Get coverage information
regions = client.coverage.list_coverage_regions()

# Get datasets for a region
datasets, pagination = client.datasets.list_datasets(region_id="fr-idf")
```

#### APIs with Request Objects (Journeys, Places, Schedules, etc.)

Most APIs now use Request objects for better type safety and maintainability:

```python
from navitia_client.entities.request.journey import JourneyRequest
from datetime import datetime

# Create a journey request
request = JourneyRequest(
    from_="stop_area:RAT:SA:GDLYO",
    to_="stop_area:RAT:SA:CHDEG",
    datetime_=datetime(2024, 6, 1, 8, 0),
    count=5
)

# Get journeys
journeys = client.journeys.list_journeys(request=request)
```

Other examples:

```python
from navitia_client.entities.request.places_nearby import PlacesNearbyRequest

# Places nearby with custom parameters
request = PlacesNearbyRequest(
    distance=1000,
    type=["stop_area", "stop_point"],
    count=20
)
places, pagination = client.places_nearby.list_objects_by_region_id_and_path(
    region_id="fr-idf",
    resource_path="lines/line:RAT:M1",
    request=request
)
```

### Pagination

Several APIs are paginated, particularly the public transportation APIs. You can navigate through results using the `start_page` and `count` parameters in Request objects:

```python
from navitia_client.entities.request.journey import JourneyRequest

# Request with pagination
request = JourneyRequest(
    from_="stop_area:RAT:SA:GDLYO",
    to_="stop_area:RAT:SA:CHDEG",
    start_page=0,  # First page
    count=10       # 10 results per page
)

journeys = client.journeys.list_journeys(request=request)
```

A `Pagination` object is provided by paginated methods to help you navigate through results.

### Tips

Few tips on how to use the Navitia APIs are available [here](docs/few_tips.md).

##  Dependencies

* Python >= 3.10
* requests>=2.31

Additional dependencies are described in the [pyproject.toml file](pyproject.toml).

##  Contributing

You are free to contribute to the repo. Please read [Contributing.md](docs/CONTRIBUTING.md).

##  Additional questions

* Are you affiliated with Navitia ?
No. This is an unofficial wrapper for the Navitia.io APIs.

* Is this client asynchronous ?
No, and it is not planned to. If you want to add async support, feel free to contribute.

* Is this client production ready ?
Yes and no. For my own purpose, it is, but I cannot guarantee that everything will behave well. If you spot a bug, please open an issue in the repo.
