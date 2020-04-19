import json
import os

from clients.warcraft_client import WarcraftClient


def test_get_journal_expansions_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_expansions_index()
    assert response == snapshot


def test_get_journal_expansion(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_expansion(68)
    assert response == snapshot


def test_get_journal_encounters_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_encounters_index()
    assert response == snapshot


def test_get_journal_encounter(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_encounter(89)
    response = client.get_playable_specialization(262)
    text = json.dumps(response)
    text = text.replace("\\r\\n", "\\n")
    obj = json.loads(text)
    assert response == snapshot


def test_get_journal_instances_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_instances_index()
    assert response == snapshot


def test_get_journal_instance(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_instance(63)
    assert response == snapshot


def test_get_journal_instance_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_journal_instance_media(63)
    assert response == snapshot
