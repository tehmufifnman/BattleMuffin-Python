import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_mount_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mount_index()
    assert response == snapshot


def test_get_mount(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mount(6)
    assert response == snapshot
