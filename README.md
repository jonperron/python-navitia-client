# navitia-client

This repository provides A Python client to use [navitia.io APIs](https://doc.navitia.io).

##  Pre-requisites

To use this library, you will need an access token from [navitia.io](https://navitia.io/tarifs/).

##  Installation

The package is not yet available on pip.

For development purpose, you can install it using

```bash
pip install -e .
```

## Usage

```python
from navitia_client.client import NavitiaClient
client = NavitiaClient(auth=<YOUR_TOKEN_HERE>)
```

A base URL for Navitia IO is hardcoded and provided to NavitiaClient by default. It can be updated using the base_navitia_url parameter.

##  API support

The library supports the following [APIs](https://doc.navitia.io/#api-catalog):

| API                                       | Supported ? |
| ----------------------------------------- | ----------- |
| Coverage                                  | ✅           |
| Datasets                                  | ✅           |
| Contributors                              | ✅           |
| Inverted geocoding                        | ✅           |
| Public transportation Objects exploration | ✅           |
| Autocomplete on Public Transport objects  | ✅           |
| Autocomplete on geographical objects      | ✅           |
| Places nearby                             | ✅           |
| Journeys                                  | ❌           |
| Isochrones                                | ❌           |
| Route Schedules                           | ❌           |
| Stop Schedules                            | ❌           |
| Terminus Schedules                        | ❌           |
| Departures                                | ❌           |
| Arrivals                                  | ❌           |
| Line reports                              | ❌           |
| Traffic reports                           | ❌           |
| Equipment_Reports                         | ❌           |

##  Dependencies

* Python >= 3.10
* requests>=2.31

Additional dependencies are described in the [pyproject.toml file](pyproject.toml).

##  Contributing

You are free to contribute to the repo. Please read [Contributing.md](CONTRIBUTING.md).

##  Additional questions

* IS this client asynchronous ?
No, and it is not planned to. If you want to add async support, feel free to contribute.
