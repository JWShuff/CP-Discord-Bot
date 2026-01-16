"""Entry point for python -m bot."""

import asyncio

from bot.app import start

if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        # Graceful shutdown already handled in start()
        # Note: asyncio.run() re-raises KeyboardInterrupt on Windows even after handling it
        print("\nReceived interrupt, shutting down...")
        pass
