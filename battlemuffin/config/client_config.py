from battlemuffin.config.region_config import Region, Locale


class ClientConfiguration:

    API_BASE_URL = "api.blizzard.com"
    OAUTH_BASE_URL = "battle.net"
    API_BASE_URL_CN = "https://gateway.battlenet.com.cn"
    OAUTH_BASE_URL_CN = "https://www.battlenet.com.cn"

    def __init__(
        self, client_id: str, client_secret: str, region: Region, locale: Locale = None
    ):
        if not region or type(region) is not Region:
            raise ValueError("Invalid value supplied for Region.")

        if locale and type(locale) is not Locale:
            raise ValueError("Invalid value supplied for Locale.")

        self.host = (
            f"https://{region.name}.{self.API_BASE_URL}"
            if region != Region.cn
            else self.API_BASE_URL_CN
        )
        self.oauth_host = (
            f"https://{region.name}.{self.OAUTH_BASE_URL}"
            if region != Region.cn
            else self.OAUTH_BASE_URL_CN
        )
        self.locale = locale
        self.region = region
        self.client_id = client_id
        self.client_secret = client_secret
