import os
from clients.warcraft_client import WarcraftClient


def test_get_regions_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_regions_index()
    assert response == snapshot


def test_get_region(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_region(1)
    assert response == snapshot
