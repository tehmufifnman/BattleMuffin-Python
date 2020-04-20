import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_pets_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pets_index()
    assert response == snapshot


def test_get_pet(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pet(39)
    assert response == snapshot
