import os
from clients.warcraft_client import WarcraftClient


def test_get_item_classes_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item_classes_index()
    assert response == snapshot


def test_get_item_class(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item_class(0)
    assert response == snapshot


def test_get_item_sets_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item_sets_index()
    assert response == snapshot


def test_get_item_set(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item_set(1)
    assert response == snapshot


def test_get_item_subclass(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item_subclass(0, 0)
    assert response == snapshot


def test_get_item(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item(19019)
    assert response == snapshot


def test_get_item_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_item_media(19019)
    assert response == snapshot
