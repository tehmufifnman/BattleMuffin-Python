import requests
from authlib.integrations.requests_client import OAuth2Session
from uplink import Consumer, Query, get, params, returns

from config.client_config import ClientConfiguration
from config.region_config import Locale, Region


class WarcraftClient(Consumer):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: Region = Region.us,
        locale: Locale = Locale.en_US,
        **kwargs,
    ):
        self.client_config = ClientConfiguration(
            client_id, client_secret, region, locale
        )
        client = self.get_client(**kwargs)
        super().__init__(base_url=self.client_config.host, client=client)
        self._inject(Query("locale").with_value(self.client_config.locale.name))

    def get_client(self, **kwargs):
        if "client" in kwargs.keys():
            return kwargs.get("client")
        else:
            oath_response = requests.get(
                f"{self.client_config.oauth_host}/oauth/.well-known/openid-configuration"
            ).json()
            token_endpoint = oath_response["token_endpoint"]
            client = OAuth2Session(
                self.client_config.client_id,
                self.client_config.client_secret,
                scope="openid",
                token_endpoint=token_endpoint,
                grant_type="client_credentials",
            )
            client.fetch_token()
            return client

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/achievement-category/index")
    def get_achievement_category_index(self):
        """Returns an index of achievement categories."""
