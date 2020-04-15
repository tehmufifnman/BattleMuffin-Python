import pytest

from clients.warcraft_client import WarcraftClient
from config.client_config import ClientConfiguration, Locale, Region

BASE_URL = "api.blizzard.com"


def test_client_config_bad_region():
    with pytest.raises(ValueError):
        ClientConfiguration("client_id", "client_secret", 999, Locale.en_US)


def test_client_config_bad_locale():
    with pytest.raises(ValueError):
        ClientConfiguration("client_id", "client_secret", Region.us, 999)


def test_warcraft_client_init(mocker):
    mocker.patch('requests.Response')
    mocker.patch('uplink.Consumer.session')
    mocker.patch('authlib.integrations.requests_client.OAuth2Session.fetch_token')
    WarcraftClient("client_id", "client_secret")


def test_warcraft_client_get_achievement_category_index(mock_client, mock_response):
    # Arrange
    expected_json = {"key": "value"}
    mock_response.with_json(expected_json)
    mock_client.with_response(mock_response)
    client = WarcraftClient("client_id", "client_secret", base_url=BASE_URL, client=mock_client)

    # Act
    actual_json = client.get_achievement_category_index()

    # Asset
    assert expected_json == actual_json
