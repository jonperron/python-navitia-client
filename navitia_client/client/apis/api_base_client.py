from requests import Response, Session  # type: ignore


class ApiBaseClient:
    def __init__(self, auth_token: str, base_navitia_url: str) -> None:
        self.base_navitia_url = base_navitia_url
        self.session = Session()
        self.session.headers.update({"Authorization": auth_token})

    def get_navitia_api(self, endpoint: str) -> Response:
        return self.session.get(endpoint)
