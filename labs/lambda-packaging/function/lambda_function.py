"""Offline greeting handler retained from a Lambda packaging lesson."""

def lambda_handler(event, context):
    """Return World for the supported Hello input; reject malformed events."""
    if not isinstance(event, dict) or event.get("input") != "Hello":
        raise ValueError("event.input must be Hello")
    return "World"
