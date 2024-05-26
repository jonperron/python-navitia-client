# navitia-client

This repository provides a unofficial Python wrapper to use [navitia.io APIs](https://doc.navitia.io).

##  Pre-requisites

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
| Isochrones                                | ✅           | Beta endpoint according to API response      |
| Route Schedules                           | ✅           |                                              |
| Stop Schedules                            | ✅           |                                              |
| Terminus Schedules                        | ✅           |                                              |
| Departures                                | ✅           |                                              |
| Arrivals                                  | ✅           |                                              |
| Line reports                              | ✅           | Beta endpoint according to API response      |
| Traffic reports                           | ✅           | Beta endpoint according to API response      |
| Equipment reports                         | ❌           | Beta service, not available to all providers |

## Usage

To use this library, you need an authentication token provided by Navitia.io.

### Create client instance

Once created, you will create an instance of the NavitiaClient class with the following:

```python
from navitia_client.client import NavitiaClient
client = NavitiaClient(auth=<YOUR_TOKEN_HERE>)
```

A base URL for Navitia IO is hardcoded and provided to NavitiaClient by default. It can be updated using the base_navitia_url parameter.

###  Access APIs data

URLs are mapped as property in the class `NavitiaClient`. You can find the mapping [here](docs/api_support/).

For example, if you want to have the list of datasets in a given region, use:

```python
datasets, pagination = client.datasets.list_datasets(region_id=<REGION_ID>)
```

### Pagination

A couple of APIs are paginated, in particular the public transporations APIs.. In such case, you can navigate in the response using the parameters `start_page` and `count`.

An object `Pagination` will be provided by the impacted methods to help you navigating.

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
