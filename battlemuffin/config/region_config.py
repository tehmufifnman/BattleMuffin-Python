from enum import Enum
from typing import List


class Region(Enum):
    us = 1
    eu = 2
    kr = 3
    tw = 4
    cn = 5


class Locale(Enum):
    en_US = 1
    es_MX = 2
    pt_BR = 3
    en_GB = 4
    es_ES = 5
    fr_FR = 6
    ru_RU = 7
    de_DE = 8
    pt_PT = 9
    it_IT = 10
    ko_KR = 11
    zh_TW = 12
    zh_CN = 13


class RegionConfiguration:

    API_BASE_URL = "api.blizzard.com"
    OAUTH_BASE_URL = "battle.net"

    def __init__(
        self,
        prefix: Region,
        available_locales: List[Locale],
        host: str = None,
        oauth_host: str = None,
    ):
        if host:
            self.host = host
        else:
            self.host = f"https://{prefix.name}.{self.API_BASE_URL}"

        if oauth_host:
            self.oauth_host = oauth_host
        else:
            self.oauth_host = f"https://{prefix.name}.{self.OAUTH_BASE_URL}"

        self.default_locale = available_locales[0]
        self.available_locales = available_locales


region_locale_map = {
    Region.us: RegionConfiguration(
        Region.us, [Locale.en_US, Locale.es_MX, Locale.pt_BR]
    ),
    Region.eu: RegionConfiguration(
        Region.eu,
        [
            Locale.en_GB,
            Locale.es_ES,
            Locale.fr_FR,
            Locale.ru_RU,
            Locale.de_DE,
            Locale.pt_PT,
            Locale.it_IT,
        ],
    ),
    Region.kr: RegionConfiguration(Region.kr, [Locale.ko_KR]),
    Region.tw: RegionConfiguration(Region.tw, [Locale.zh_TW]),
    Region.cn: RegionConfiguration(
        Region.cn,
        [Locale.zh_CN],
        "https://gateway.battlenet.com.cn",
        "https://www.battlenet.com.cn",
    ),
}
