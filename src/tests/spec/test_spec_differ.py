import requests


def test_api_spec_diff(snapshot):
    response = requests.get(
        "https://develop.battle.net/api/pages/content/documentation/world-of-warcraft/game-data-apis.json"
    ).json()
    assert response == snapshot
