import os
from clients.warcraft_client import WarcraftClient


def test_get_professions_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_professions_index()
    assert response == snapshot


def test_get_profession(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_profession(164)
    assert response == snapshot


def test_get_profession_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_profession_media(164)
    assert response == snapshot


def test_get_profession_skill_tier(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_profession_skill_tier(164, 2477)
    assert response == snapshot


def test_get_recipe(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_recipe(1631)
    assert response == snapshot


def test_get_recipe_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_recipe_media(1631)
    assert response == snapshot
