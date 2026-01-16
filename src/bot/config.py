"""Configuration loading from environment."""

import os
import re

from dotenv import load_dotenv

load_dotenv()


class ConfigError(Exception):
    """Raised when required configuration is missing."""


class Config:
    """Application configuration from environment variables."""

    def __init__(self) -> None:
        self.discord_token = self._require("DISCORD_TOKEN")
        self.grace_period_days = int(self._require("GRACE_PERIOD_DAYS"))
        self.mod_channel_id = self._require("MOD_CHANNEL_ID")
        # Parse and compile the regex at startup
        self.name_policy_regex = self._compile_regex(self._require("NAME_POLICY_REGEX"))

    def _require(self, key: str) -> str:
        """Get a required environment variable or fail fast."""
        value = os.getenv(key)
        if not value:
            raise ConfigError(
                f"Missing required environment variable: {key}\nCopy .env.example to .env and fill in your values."
            )
        return value

    def _compile_regex(self, pattern: str) -> re.Pattern[str]:
        """Compile a regex pattern string or fail fast"""
        try:
            return re.compile(pattern)
        except re.error as e:
            raise ConfigError(f"Invalid NAME_POLICY_REGEX: {e.msg}\nPattern: {pattern}\nPosition: {e.pos}")


config = Config()
