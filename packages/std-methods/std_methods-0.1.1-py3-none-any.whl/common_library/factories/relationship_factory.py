"""
This module implements the RelationshipFactory.
Since we no longer have a dedicated Edge model, this factory returns a standardized
relationship payload (as a dictionary) that can be used by the repository layer.
"""

from src.common_library.utils.id_generator import generate_id


class RelationshipFactory:
    # A registry to hold builder functions for relationship types if needed.
    _builders = {}

    @classmethod
    def register_builder(cls, rel_type: str, builder):
        """
        Registers a builder function for a specific relationship type.
        """
        cls._builders[rel_type] = builder

    @staticmethod
    def create_relationship(
        rel_type: str, source_id: str, target_id: str, id: str = None, **kwargs
    ):
        """
        Creates a relationship payload (as a dict) and optionally converts it into
        a domain-specific model using a builder function.
        """
        if id is None:
            id = generate_id("Rel")

        payload = {
            "id": id,
            "type": rel_type,
            "source_id": source_id,
            "target_id": target_id,
        }
        # Merge additional keyword attributes.
        payload.update(kwargs)

        # Check if a builder was directly provided in kwargs.
        builder = kwargs.get("builder")
        if builder and callable(builder):
            return builder(**payload)

        # Alternatively, check if a builder has been registered for this relationship type.
        registered_builder = RelationshipFactory._builders.get(rel_type)
        if registered_builder and callable(registered_builder):
            return registered_builder(**payload)

        # Return the payload if no builder is provided.
        return payload
