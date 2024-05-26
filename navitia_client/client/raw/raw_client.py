from typing import Any
from requests import Response, Session  # type: ignore


class RawClient:
    """
    Client to perform raw calls on the APIs.

    This class is intended for debug purposes.

    Attributes:
        base_navitia_url (str): The base URL for the Navitia API.
        session (requests.Session): The session used to make HTTP requests with the provided authorization token.
    """

    def __init__(self, auth_token: str, base_navitia_url: str) -> None:
        """
        Initialize the RawClient with an authorization token and base URL.

        Args:
            auth_token (str): The authorization token for API access.
            base_navitia_url (str): The base URL for the Navitia API.
        """
        self.base_navitia_url = base_navitia_url
        self.session = Session()
        self.session.headers.update({"Authorization": auth_token})

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """
        Generate a query string from a dictionary of filters.

        Args:
            filters (dict[str, Any]): A dictionary of filter parameters.

        Returns:
            str: The generated query string.
        """
        filter_query = "&".join([f"{key}={value}" for key, value in filters.items()])
        return "?" + filter_query if filter_query else ""

    def call_api(self, endpoint: str, filters: dict[str, Any]) -> Response:
        """
        Perform a GET request to the specified API endpoint with the given filters.

        Args:
            endpoint (str): The API endpoint to call.
            filters (dict[str, Any]): A dictionary of filters to include in the API call.

        Returns:
            requests.Response: The response from the API call.
        """
        request_url = (
            f"{self.base_navitia_url}/{endpoint}/"
            + self._generate_filter_query(filters)
        )
        response = self.session.get(request_url)
        return response
