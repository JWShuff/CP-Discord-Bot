"""Tests for Discord client setup."""

from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture
def mock_discord_config(monkeypatch):
    """Fixture to mock the Discord config for all app tests.

    This runs before each test that requests it, setting up a fake
    config so we don't need a real DISCORD_TOKEN.
    """
    mock_config = MagicMock()
    mock_config.discord_token = "test_token"
    monkeypatch.setattr("bot.app.config", mock_config)
    return mock_config


class TestApp:
    """Test app module."""

    def test_client_has_minimal_intents(self, mock_discord_config):
        """Test that client is created with minimal intents."""
        from bot.app import client, intents

        assert intents.guilds is True
        assert client.intents.guilds is True
        # Ensure we're not requesting privileged intents
        assert client.intents.members is False
        assert client.intents.presences is False
        assert client.intents.message_content is False

    @pytest.mark.asyncio
    async def test_shutdown_closes_client(self, mock_discord_config):
        """Test that shutdown function closes the client."""
        from bot.app import client, shutdown

        # Mock the close method
        client.close = AsyncMock()

        await shutdown()

        client.close.assert_called_once()

    def test_on_ready_event_is_registered(self, mock_discord_config):
        """Test that on_ready event handler is registered."""
        from bot import app

        # Check that on_ready function exists and is decorated
        assert hasattr(app, "on_ready")
        assert callable(app.on_ready)
