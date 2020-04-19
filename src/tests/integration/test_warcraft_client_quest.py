import os
from clients.warcraft_client import WarcraftClient


def test_get_quests_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quests_index()
    assert response == snapshot


def test_get_quest(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest(2)
    assert response == snapshot


def test_get_quest_categories_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest_categories_index()
    assert response == snapshot


def test_get_quest_category(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest_category(1)
    assert response == snapshot


def test_get_quest_areas_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest_areas_index()
    assert response == snapshot


def test_get_quest_area(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest_area(1)
    assert response == snapshot


def test_get_quest_types_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest_types_index()
    assert response == snapshot


def test_get_quest_type(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_quest_type(1)
    assert response == snapshot
