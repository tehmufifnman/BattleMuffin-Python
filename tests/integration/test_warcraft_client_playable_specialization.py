from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_playable_specializations_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_specializations_index()
    assert response == snapshot


def test_get_playable_specialization(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_specialization(262)
    assert response == snapshot


def test_get_playable_specialization_media(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_playable_specialization_media(262)
    assert response == snapshot
