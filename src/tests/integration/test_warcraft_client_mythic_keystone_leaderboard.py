import os
from clients.warcraft_client import WarcraftClient


def test_get_mythic_keystone_leaderboards_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_leaderboards_index(11)
    assert response == snapshot


def test_get_mythic_keystone_leaderboard(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_leaderboard(11, 197, 641)
    assert response == snapshot
