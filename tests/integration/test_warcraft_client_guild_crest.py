import os
from clients.warcraft_client import WarcraftClient


def test_get_guild_crest_components_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_guild_crest_components_index()
    assert response == snapshot


def test_get_guild_crest_border_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_guild_crest_border_media(0)
    assert response == snapshot


def test_get_guild_crest_emblem_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_guild_crest_emblem_media(0)
    assert response == snapshot
