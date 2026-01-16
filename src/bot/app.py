"""Discord client setup and lifecycle management."""

import asyncio
import signal
import sys

import discord
import discord.ext.commands as commands

from bot.config import config

# Minimal intents - only guilds, no privileged intents
intents = discord.Intents(guilds=True)

# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready() -> None:
    """Called when the bot has connected and is ready."""
    print(f"READY: {client.user}")


async def shutdown() -> None:
    """Gracefully close the Discord client."""
    await client.close()


def _handle_signal(sig: signal.Signals) -> None:
    """Schedule shutdown when receiving termination signals."""
    print(f"\nReceived {sig.name}, shutting down...")
    asyncio.create_task(shutdown())


async def start() -> None:
    """Start the Discord client with signal handling."""
    # Set up signal handlers for graceful shutdown
    loop = asyncio.get_running_loop()

    if sys.platform != "win32":
        # Unix-like systems
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, lambda s=sig: _handle_signal(s))
    else:
        # Windows doesn't support add_signal_handler
        # SIGINT (Ctrl+C) is handled by default KeyboardInterrupt
        pass

    try:
        await client.start(config.discord_token)
    except KeyboardInterrupt:
        print("\nReceived interrupt, shutting down...")
    finally:
        if not client.is_closed():
            await client.close()
