import os
from clients.warcraft_client import WarcraftClient


def test_get_playable_classes_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_classes_index()
    assert response == snapshot


def test_get_playable_class(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_class(7)
    assert response == snapshot


def test_get_playable_class_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_class_media(7)
    assert response == snapshot


def test_get_pvp_talent_slots(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_pvp_talent_slots(7)
    assert response == snapshot
