from src.common_library.factories.node_factory import NodeFactory


# A dummy node model for testing the builder functionality.
class DummyNode:
    def __init__(self, **payload):
        self.payload = payload


def dummy_node_builder(**payload):
    return DummyNode(**payload)


def test_create_function_node_default():
    """
    Test that the NodeFactory returns a correct dictionary for a 'function' node without a builder.
    """
    payload = NodeFactory.create_node("function", name="Test Function")
    assert isinstance(payload, dict)
    assert payload["name"] == "Test Function"
    assert payload["type"] == "function"
    assert "id" in payload


def test_create_function_node_with_builder():
    """
    Test that providing a builder returns an instance of the expected model for a 'function' node.
    """
    node = NodeFactory.create_node(
        "function", name="Function Builder", builder=dummy_node_builder
    )
    assert isinstance(node, DummyNode)
    assert node.payload["name"] == "Function Builder"


def test_create_element_node_default():
    """
    Test that the NodeFactory returns a correct dictionary for an 'element' node without a builder.
    """
    payload = NodeFactory.create_node("element", name="Test Element")
    assert isinstance(payload, dict)
    assert payload["name"] == "Test Element"
    assert payload["type"] == "element"
    assert "id" in payload


def test_create_element_node_with_builder():
    """
    Test that providing a builder returns an instance of the expected model for an 'element' node.
    """
    node = NodeFactory.create_node(
        "element", name="Element Builder", builder=dummy_node_builder
    )
    assert isinstance(node, DummyNode)
    assert node.payload["name"] == "Element Builder"
