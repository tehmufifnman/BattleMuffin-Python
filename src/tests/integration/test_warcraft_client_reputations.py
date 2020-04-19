import os
from clients.warcraft_client import WarcraftClient


def test_get_reputation_factions_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_reputation_factions_index()
    assert response == snapshot


def test_get_reputation_faction(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_reputation_faction(21)
    assert response == snapshot


def test_get_reputation_tiers_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_reputation_tiers_index()
    assert response == snapshot


def test_get_reputation_tiers(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_reputation_tiers(2)
    assert response == snapshot