"""Application entry points for the project."""

DEFAULT_RECIPIENT = "Imagination Sandbox"


def get_message(recipient: str = DEFAULT_RECIPIENT) -> str:
    """Return the project greeting, optionally addressed to someone else."""
    return f"Hello from {recipient}!"
