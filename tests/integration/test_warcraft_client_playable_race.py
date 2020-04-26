import os

from battlemuffin.clients.warcraft_client import WarcraftClient
from battlemuffin.config.region_config import Locale, Region


def test_get_playable_races_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_playable_races_index()
    assert response == snapshot


def test_get_playable_race(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_playable_race(2)
    assert response == snapshot
