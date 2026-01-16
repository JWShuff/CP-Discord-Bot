from typing import NamedTuple


class PolicyResult(NamedTuple):
    compliant: bool
    matched_name: str  # provided
    sanitized_name: str  # safe to post/log

    def sanitize_for_logging(name: str, max_length: int = 100) -> str:
        """Remove control chars, truncate to 100 characters, and escape for posting/logging"""
        # Strip control chars (C0, C1, other sketchy unicode)
        cleaned = "".join(char for char in name if char.isprintable() or char == " ")
        # Truncate
        if len(cleaned) > max_length:
            cleaned = cleaned[:max_length] + "..."
        return cleaned
