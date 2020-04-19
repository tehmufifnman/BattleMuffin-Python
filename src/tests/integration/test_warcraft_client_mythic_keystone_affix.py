import os
from clients.warcraft_client import WarcraftClient


def test_get_mythic_keystone_affixes_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_affixes_index()
    assert response == snapshot


def test_get_mythic_keystone_affix(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_affix(1)
    assert response == snapshot


def test_get_mythic_keystone_affix_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_mythic_keystone_affix_media(1)
    assert response == snapshot
