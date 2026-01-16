"""Tests for configuration loading."""

import pytest

from bot.config import Config, ConfigError


@pytest.fixture
def mock_discord_token(monkeypatch):
    """Fixture to set the DISCORD_TOKEN env var."""
    test_token = "test_discord_token"
    monkeypatch.setenv("DISCORD_TOKEN", test_token)

    return test_token


class TestConfig:
    """Test Config class."""

    def test_config_loads_discord_token(self, mock_discord_token):
        """Test that Config loads DISCORD_TOKEN from environment."""
        config = Config()

        assert config.discord_token == mock_discord_token

    def test_config_raises_error_when_token_missing(self, monkeypatch):
        """Test that Config raises ConfigError when DISCORD_TOKEN is missing."""
        monkeypatch.delenv("GRACE_PERIOD_DAYS", raising=False)

        with pytest.raises(ConfigError, match="Missing required environment variable: GRACE_PERIOD_DAYS"):
            Config()

    def test_config_raises_error_when_token_empty(self, monkeypatch):
        """Test that Config raises ConfigError when DISCORD_TOKEN is empty string."""
        monkeypatch.setenv("MOD_CHANNEL_ID", "")

        with pytest.raises(ConfigError, match="Missing required environment variable: MOD_CHANNEL_ID"):
            Config()

    def test_config_raises_error_when_regex_invalid(self, mock_discord_token, monkeypatch):
        """Test that Config raises ConfigError when NAME_POLICY_REGEX does not parse to valid regex."""
        monkeypatch.setenv("NAME_POLICY_REGEX", "[unclosed matcher")
        with pytest.raises(ConfigError, match="Invalid NAME_POLICY_REGEX"):
            Config()
