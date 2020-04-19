import os
from clients.warcraft_client import WarcraftClient


def test_get_achievement_categories_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_achievement_categories_index()
    assert response == snapshot


def test_get_achievement_category(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_achievement_category(81)
    assert response == snapshot


def test_get_achievements_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_achievements_index()
    assert response == snapshot


def test_get_achievement(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_achievement(6)
    assert response == snapshot


def test_get_achievement_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_achievement_media(6)
    assert response == snapshot
