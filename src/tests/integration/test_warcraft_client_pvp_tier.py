import os
from clients.warcraft_client import WarcraftClient


def test_get_pvp_tiers_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_tiers_index()
    assert response == snapshot


def test_get_pvp_tier(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_tier(1)
    assert response == snapshot


def test_get_pvp_tier_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_tier_media(1)
    assert response == snapshot
