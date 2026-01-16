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
        monkeypatch.delenv("DISCORD_TOKEN", raising=False)

        with pytest.raises(ConfigError, match="Missing required environment variable: DISCORD_TOKEN"):
            Config()

    def test_config_raises_error_when_token_empty(self, monkeypatch):
        """Test that Config raises ConfigError when DISCORD_TOKEN is empty string."""
        monkeypatch.setenv("DISCORD_TOKEN", "")

        with pytest.raises(ConfigError, match="Missing required environment variable: DISCORD_TOKEN"):
            Config()

    def test_require_method_returns_value(self, mock_discord_token, monkeypatch):
        """Test that _require method returns env var value."""
        test_value = "some_value"
        monkeypatch.setenv("TEST_VAR", test_value)

        config = Config()
        result = config._require("TEST_VAR")

        assert result == test_value

    def test_require_method_raises_on_missing(self, mock_discord_token):
        """Test that _require raises ConfigError for missing var."""
        config = Config()

        with pytest.raises(ConfigError, match="Missing required environment variable: NONEXISTENT"):
            config._require("NONEXISTENT")
