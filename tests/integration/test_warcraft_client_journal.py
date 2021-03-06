import json
import os

from battlemuffin.clients.warcraft_client import WarcraftClient
from battlemuffin.config.region_config import Locale, Region


def test_get_journal_expansions_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_expansions_index()
    assert response == snapshot


def test_get_journal_expansion(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_expansion(68)
    assert response == snapshot


def test_get_journal_encounters_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_encounters_index()
    assert response == snapshot


def test_get_journal_encounter(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_encounter(89)
    text = json.dumps(response)
    text = text.replace("\\r\\n", "\\n")
    obj = json.loads(text)
    assert obj == snapshot


def test_get_journal_instances_index(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_instances_index()
    assert response == snapshot


def test_get_journal_instance(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_instance(63)
    assert response == snapshot


def test_get_journal_instance_media(snapshot):
    client = WarcraftClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), Region.us, Locale.en_US
    )
    response = client.get_journal_instance_media(63)
    assert response == snapshot
