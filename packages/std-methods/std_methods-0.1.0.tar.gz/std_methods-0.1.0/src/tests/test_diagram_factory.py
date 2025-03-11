from src.common_library.factories.diagram_factory import DiagramFactory


# A dummy diagram model for testing the builder functionality.
class DummyDiagram:
    def __init__(self, **payload):
        self.payload = payload


def dummy_diagram_builder(**payload):
    return DummyDiagram(**payload)


def test_create_diagram_default():
    """
    Test that the diagram factory returns a plain dictionary payload when no builder is provided.
    """
    payload = DiagramFactory.create_diagram("IDEF0", name="Test Diagram")
    assert isinstance(payload, dict)
    assert payload["name"] == "Test Diagram"
    assert payload["type"] == "IDEF0"
    assert "id" in payload


def test_create_diagram_with_builder():
    """
    Test that the diagram factory uses an inline builder function to return a model instance.
    """
    diagram = DiagramFactory.create_diagram(
        "IDEF0", name="Builder Diagram", builder=dummy_diagram_builder
    )
    assert isinstance(diagram, DummyDiagram)
    assert diagram.payload["name"] == "Builder Diagram"
