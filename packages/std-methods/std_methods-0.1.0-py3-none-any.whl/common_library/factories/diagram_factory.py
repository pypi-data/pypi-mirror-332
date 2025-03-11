"""
This module implements the DiagramFactory.
It encapsulates the logic needed to create different types of Diagram objects,
including the new inline placements as a list of dictionaries.
"""

from src.common_library.utils.id_generator import generate_id


class DiagramFactory:
    # A registry to hold builder functions for different diagram types.
    _builders = {}

    @classmethod
    def register_builder(cls, diagram_type: str, builder):
        """
        Registers a builder function for a specific diagram type.
        The diagram_type is stored in uppercase for consistency.
        """
        cls._builders[diagram_type.upper()] = builder

    @staticmethod
    def create_diagram(
        diagram_type: str,
        id: str = None,
        name: str = None,
        description: str = None,
        project_id: str = None,
        **kwargs,
    ):
        """
        Creates a diagram payload (as a dict) and optionally converts it into
        a domain-specific model using a builder function.

        If a builder is passed via kwargs (or registered for this diagram type),
        it will be used to convert the payload.
        """
        if id is None:
            id = generate_id("Dgm")

        # Construct a generic payload with default values.
        payload = {
            "id": id,
            "name": name or "Unnamed Diagram",
            "description": description or "No description provided",
            "project_id": project_id or "Unassigned Project",
            "placements": kwargs.get("placements", []),
            "extra_info": kwargs.get("extra_info", ""),
            "type": diagram_type.upper(),
        }

        # Check if a builder was directly provided in kwargs.
        builder = kwargs.get("builder")
        if builder and callable(builder):
            return builder(**payload)

        # Alternatively, check if a builder has been registered for this diagram type.
        registered_builder = DiagramFactory._builders.get(diagram_type.upper())
        if registered_builder and callable(registered_builder):
            return registered_builder(**payload)

        # Return the generic payload if no builder is provided.
        return payload
