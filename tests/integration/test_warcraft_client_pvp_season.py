import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_pvp_seasons_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_seasons_index()
    assert response == snapshot


def test_get_pvp_season(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_season(27)
    assert response == snapshot


def test_get_pvp_leaderboards_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_leaderboards_index(27)
    assert response == snapshot


def test_get_pvp_leaderboard(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_leaderboard(27, "3v3")
    assert response == snapshot


def test_get_pvp_rewards_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_rewards_index(27)
    assert response == snapshot
