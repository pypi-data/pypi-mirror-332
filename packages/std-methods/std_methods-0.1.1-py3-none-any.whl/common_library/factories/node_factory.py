"""
This module implements the NodeFactory.
It creates Function or Element nodes using our updated models,
which now reference related nodes by IDs rather than embedding full models.
"""

from src.common_library.utils.id_generator import generate_id


class NodeFactory:
    # A registry to hold builder functions for different node types.
    _builders = {}

    @classmethod
    def register_builder(cls, node_type: str, builder):
        """
        Registers a builder function for a specific node type.
        """
        cls._builders[node_type.lower()] = builder

    @staticmethod
    def create_node(node_type: str, id: str = None, name: str = None, **kwargs):
        """
        Creates a node payload (as a dict) and optionally converts it into
        a domain-specific model using a builder function.

        Supports node types such as "function" and "element".
        """
        if id is None:
            id = generate_id("N")

        node_type_lower = node_type.lower()

        if node_type_lower == "function":
            payload = {
                "id": id,
                "name": name or "Unnamed Function",
                "description": kwargs.get("description", "No description provided"),
                "inputs": kwargs.get("inputs", []),
                "outputs": kwargs.get("outputs", []),
                "controls": kwargs.get("controls", []),
                "mechanisms": kwargs.get("mechanisms", []),
                "subfunctions": kwargs.get("subfunctions", []),
                "type": "function",
            }
        elif node_type_lower == "element":
            payload = {
                "id": id,
                "name": name or "Unnamed Element",
                "document_ids": kwargs.get("document_ids", []),
                "type": "element",
            }
        else:
            raise ValueError(f"Unsupported node type: {node_type}")

        # Check if a builder was directly provided in kwargs.
        builder = kwargs.get("builder")
        if builder and callable(builder):
            return builder(**payload)

        # Alternatively, check if a builder has been registered for this node type.
        registered_builder = NodeFactory._builders.get(node_type_lower)
        if registered_builder and callable(registered_builder):
            return registered_builder(**payload)

        # Return the payload if no builder is provided.
        return payload
