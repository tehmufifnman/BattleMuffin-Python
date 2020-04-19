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


def test_get_azerite_essences_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_azerite_essences_index()
    assert response == snapshot


def test_get_azerite_essence(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_azerite_essence(2)
    assert response == snapshot


def test_get_azerite_essence_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_azerite_essence_media(2)
    assert response == snapshot


def test_get_connected_realms_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_connected_realms_index()
    assert response == snapshot


def test_get_connected_realm(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_connected_realm(11)
    assert response == snapshot


def test_get_creature_families_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_families_index()
    assert response == snapshot


def test_get_creature_family(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_family(1)
    assert response == snapshot


def test_get_creature_types_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_types_index()
    assert response == snapshot


def test_get_creature_type(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_type(1)
    assert response == snapshot


def test_get_creature(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature(42722)
    assert response == snapshot


def test_get_creature_display_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_display_media(30221)
    assert response == snapshot


def test_get_creature_family_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_creature_family_media(1)
    assert response == snapshot


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
