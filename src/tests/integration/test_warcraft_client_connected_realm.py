import os
from clients.warcraft_client import WarcraftClient


def test_get_connected_realms_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_connected_realms_index()
    assert response == snapshot


def test_get_connected_realm(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_connected_realm(11)
    assert response == snapshot
