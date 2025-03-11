from src.common_library.factories.relationship_factory import RelationshipFactory


# A dummy relationship model for testing the builder functionality.
class DummyRelationship:
    def __init__(self, **payload):
        self.payload = payload


def dummy_relationship_builder(**payload):
    return DummyRelationship(**payload)


def test_create_relationship_default():
    """
    Test that RelationshipFactory returns a dictionary with the proper keys when no builder is provided.
    """
    payload = RelationshipFactory.create_relationship(
        "CONNECTS", "source-1", "target-1"
    )
    assert isinstance(payload, dict)
    assert payload["type"] == "CONNECTS"
    assert payload["source_id"] == "source-1"
    assert payload["target_id"] == "target-1"
    assert "id" in payload


def test_create_relationship_with_builder():
    """
    Test that providing a builder function returns an instance of the expected relationship model.
    """
    relationship = RelationshipFactory.create_relationship(
        "CONNECTS", "source-1", "target-1", builder=dummy_relationship_builder
    )
    assert isinstance(relationship, DummyRelationship)
    assert relationship.payload["type"] == "CONNECTS"
