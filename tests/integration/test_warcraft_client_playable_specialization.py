import json
import os

from battlemuffin.clients.warcraft_client import WarcraftClient
from battlemuffin.config.region_config import Locale, Region


def test_get_playable_specializations_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_playable_specializations_index()
    assert response == snapshot


def test_get_playable_specialization(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_playable_specialization(262)
    text = json.dumps(response)
    text = text.replace("\\r\\n", "\\n")
    obj = json.loads(text)
    assert obj == snapshot


def test_get_playable_specialization_media(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_playable_specialization_media(262)
    assert response == snapshot
