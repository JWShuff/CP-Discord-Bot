"""Configuration loading from environment."""

import os

from dotenv import load_dotenv

load_dotenv()


class ConfigError(Exception):
    """Raised when required configuration is missing."""


class Config:
    """Application configuration from environment variables."""

    def __init__(self) -> None:
        self.discord_token = self._require("DISCORD_TOKEN")

    def _require(self, key: str) -> str:
        """Get a required environment variable or fail fast."""
        value = os.getenv(key)
        if not value:
            raise ConfigError(
                f"Missing required environment variable: {key}\nCopy .env.example to .env and fill in your values."
            )
        return value


config = Config()
