import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_spell(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_spell(196607)
    assert response == snapshot


def test_get_spell_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_spell_media(196607)
    assert response == snapshot
