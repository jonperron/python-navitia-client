from requests import Session  # type: ignore

BASE_NAVITIA_URL: str = "https://api.navitia.io/v1/"


class HttpBaseClient:
    def __init__(
        self, auth_token: str, base_navitia_url: str = BASE_NAVITIA_URL
    ) -> None:
        self.base_navitia_url = base_navitia_url
        self.session = Session().headers.update({"Authorization": auth_token})
