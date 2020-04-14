import requests
from authlib.integrations.requests_client import OAuth2Session
from uplink import Consumer, Query, get, params, returns

from config.client_config import ClientConfiguration
from config.region_config import Locale, Region


class WarcraftClient(Consumer):
    def __init__(self, client_id: str, client_secret: str, region: Region = Region.us, locale: Locale = Locale.en_US):
        self.client_config = ClientConfiguration(client_id, client_secret, region, locale)

        oath_response = requests.get(f"{self.client_config.oauth_host}/oauth/.well-known/openid-configuration").json()
        token_endpoint = oath_response['token_endpoint']
        session = OAuth2Session(client_id, client_secret, scope="openid", token_endpoint=token_endpoint, grant_type="client_credentials")
        session.fetch_token()
        super().__init__(base_url=self.client_config.host, client=session)
        self._inject(Query("locale").with_value(self.client_config.locale.name))

    @returns.json
    @params({"namespace": "static-us"})
    @get("/data/wow/achievement-category/index")
    def get_achievement_category_index(self):
        """Returns an index of achievement categories."""
