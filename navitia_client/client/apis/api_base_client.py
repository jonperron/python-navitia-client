from typing import Any
from requests import Response, Session  # type: ignore

from navitia_client.client.exceptions import (
    NavitiaAccessTokenMissingError,
    NavitiaForbiddenAccessError,
    NavitiaNotFoundError,
    NavitiaUnknownObjectError,
    NavitiaUnableToParseError,
)


class ApiBaseClient:
    """Common base client for API calls."""

    def __init__(self, auth_token: str, base_navitia_url: str) -> None:
        self.base_navitia_url = base_navitia_url
        self.session = Session()
        self.session.headers.update({"Authorization": auth_token})

    @staticmethod
    def _check_response_for_exception(response: Response) -> Response:
        json_payload = response.json()
        if "error" in json_payload:
            error_message = json_payload["error"]["message"]
            match json_payload["error"]["id"]:
                case "unable_to_parse":
                    raise NavitiaUnableToParseError(error_message)
                case "unknown_object":
                    raise NavitiaUnknownObjectError(error_message)
                case "no_solution":
                    raise NavitiaNotFoundError(error_message)

        if "message" in json_payload:
            error_message = json_payload["message"]
            if "no token" in error_message:
                raise NavitiaAccessTokenMissingError(error_message)
            if " either read-protected or not readable" in error_message:
                raise NavitiaForbiddenAccessError(error_message)

        return response

    @staticmethod
    def _generate_filter_query(filters: dict[str, Any]) -> str:
        """Generate query string regarding provided filters"""
        filter_query = ""
        for key, value in filters.items():
            if isinstance(value, list):
                filter_query += "".join(
                    f"&{key}={individual_value}" for individual_value in value
                )
            else:
                filter_query += f"&{key}={value}"
        return "?" + filter_query[1:] if len(filter_query) > 0 else ""

    def get_navitia_api(self, endpoint: str) -> Response:
        return self._check_response_for_exception(self.session.get(endpoint))
