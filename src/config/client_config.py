from config.region_config import Region, Locale, region_locale_map


class ClientConfiguration:
    def __init__(self, client_id: str, client_secret: str, region: Region, locale: Locale):
        if region not in region_locale_map.keys():
            raise ValueError("Configuration not found for specified region")

        region_config = region_locale_map[region]
        if locale not in region_config.available_locales:
            raise ValueError("Locale not valid for specified region")

        self.host = region_config.host
        self.oauth_host = region_config.oauth_host
        self.locale = region_config.default_locale if not locale else locale
        self.client_id = client_id
        self.client_secret = client_secret
