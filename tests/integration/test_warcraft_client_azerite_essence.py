import os

from battlemuffin.clients.warcraft_client import WarcraftClient
from battlemuffin.config.region_config import Locale, Region


def test_get_azerite_essences_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_azerite_essences_index()
    assert response == snapshot


def test_get_azerite_essence(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_azerite_essence(2)
    assert response == snapshot


def test_get_azerite_essence_media(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_azerite_essence_media(2)
    assert response == snapshot
