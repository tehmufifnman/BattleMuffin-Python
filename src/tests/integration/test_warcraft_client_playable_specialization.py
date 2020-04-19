import json
import os

from clients.warcraft_client import WarcraftClient


def test_get_playable_specializations_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_specializations_index()
    assert response == snapshot


def test_get_playable_specialization(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_specialization(262)
    text = json.dumps(response)
    text = text.replace("\\r\\n", "\\n")
    obj = json.loads(text)
    assert obj == snapshot


def test_get_playable_specialization_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_specialization_media(262)
    assert response == snapshot
