import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_titles_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_titles_index()
    assert response == snapshot


def test_get_title(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_title(1)
    assert response == snapshot
