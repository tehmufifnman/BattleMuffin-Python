import os
from clients.warcraft_client import WarcraftClient


def test_get_mythic_raid_leaderboard(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_raid_leaderboard("uldir", "alliance")
    assert response == snapshot
