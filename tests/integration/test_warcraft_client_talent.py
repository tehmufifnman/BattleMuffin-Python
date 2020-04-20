import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_talents_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_talents_index()
    assert response == snapshot


def test_get_talent(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_talent(23106)
    assert response == snapshot


def test_get_pvp_talents_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_talents_index()
    assert response == snapshot


def test_get_pvp_talent(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_talent(3)
    assert response == snapshot
