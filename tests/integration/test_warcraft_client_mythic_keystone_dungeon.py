import os

from battlemuffin.clients.warcraft_client import WarcraftClient
from battlemuffin.config.region_config import Locale, Region


def test_get_mythic_keystone_dungeons_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_mythic_keystone_dungeons_index()
    assert response == snapshot


def test_get_mythic_keystone_dungeon(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_mythic_keystone_dungeon(353)
    assert response == snapshot


def test_get_mythic_keystone_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_mythic_keystone_index()
    assert response == snapshot


def test_get_mythic_keystone_period(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_mythic_keystone_period(641)
    assert response == snapshot


def test_get_mythic_keystone_seasons_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_mythic_keystone_seasons_index()
    assert response == snapshot


def test_get_mythic_keystone_season(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_mythic_keystone_season(1)
    assert response == snapshot
