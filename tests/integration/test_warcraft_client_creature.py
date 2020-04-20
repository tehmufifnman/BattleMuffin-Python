import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_creature_families_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_families_index()
    assert response == snapshot


def test_get_creature_family(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_family(1)
    assert response == snapshot


def test_get_creature_types_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_types_index()
    assert response == snapshot


def test_get_creature_type(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_type(1)
    assert response == snapshot


def test_get_creature(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature(42722)
    assert response == snapshot


def test_get_creature_display_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_display_media(30221)
    assert response == snapshot


def test_get_creature_family_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_family_media(1)
    assert response == snapshot
