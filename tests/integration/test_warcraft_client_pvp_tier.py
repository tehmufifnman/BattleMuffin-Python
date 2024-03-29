import os

from battlemuffin.clients.warcraft_client import WarcraftClient
from battlemuffin.config.region_config import Locale, Region


def test_get_pvp_tiers_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_pvp_tiers_index()
    assert response == snapshot


def test_get_pvp_tier(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_pvp_tier(1)
    assert response == snapshot


def test_get_pvp_tier_media(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_pvp_tier_media(1)
    assert response == snapshot
