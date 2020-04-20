import os
from clients.warcraft_client import WarcraftClient


def test_get_mythic_keystone_dungeons_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_dungeons_index()
    assert response == snapshot


def test_get_mythic_keystone_dungeon(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_dungeon(353)
    assert response == snapshot


def test_get_mythic_keystone_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_index()
    assert response == snapshot


def test_get_mythic_keystone_periods_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_periods_index()
    assert response == snapshot


def test_get_mythic_keystone_period(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_period(641)
    assert response == snapshot


def test_get_mythic_keystone_seasons_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_seasons_index()
    assert response == snapshot


def test_get_mythic_keystone_season(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_season(1)
    assert response == snapshot
