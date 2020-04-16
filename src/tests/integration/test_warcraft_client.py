import os
from clients.warcraft_client import WarcraftClient


def test_get_achievement_category_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_achievement_category_index()
    snapshot.assert_match(response)
