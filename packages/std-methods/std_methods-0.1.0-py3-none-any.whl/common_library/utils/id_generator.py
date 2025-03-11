# app/utils/id_generator.py
import uuid


def generate_id(prefix: str) -> str:
    """
    Generates a unique identifier with the specified prefix.

    Parameters:
        prefix (str): The prefix to use (e.g., "N", "E", "Doc", "Dgm", "Proj").

    Returns:
        str: A unique ID in the format '{prefix}-{uuid4}'.
    """
    return f"{prefix}-{uuid.uuid4()}"
