import pytest
from src.common_library.repositories.base_repository import BaseRepository
from neo4j import GraphDatabase


# Dummy session and driver classes to simulate Neo4j behavior.
class DummySession:
    def __init__(self):
        self.closed = False

    def __enter__(self):
        # Return self so it can be used as a context manager.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure the session is closed when exiting the context.
        self.close()

    def run(self, query, parameters=None):
        # Simulate a successful query execution.
        class DummyResult:
            def data(self):
                return [{"dummy": "value"}]

        return DummyResult()

    def close(self):
        self.closed = True


class DummyDriver:
    def __init__(self):
        self.session_called = False

    def session(self):
        self.session_called = True
        return DummySession()

    def close(self):
        pass


def dummy_driver(uri, auth):
    return DummyDriver()


# Patch GraphDatabase.driver to return our dummy driver.
@pytest.fixture(autouse=True)
def patch_graph_database_driver(monkeypatch):
    monkeypatch.setattr(GraphDatabase, "driver", dummy_driver)


def test_base_repository_initialization():
    """
    Test that BaseRepository initializes correctly and verifies connectivity.
    """
    repo = BaseRepository(uri="bolt://dummy", user="dummy", password="dummy")
    assert hasattr(repo, "driver")
    # Verify that our dummy driver's session was called during connection testing.
    assert repo.driver.session_called is True


def test_execute_query():
    """
    Test that execute_query returns data as expected.
    """
    repo = BaseRepository(uri="bolt://dummy", user="dummy", password="dummy")
    result = repo.execute_query("RETURN dummy")
    assert isinstance(result, list)
    assert result[0]["dummy"] == "value"


def test_close_repository():
    """
    Test that the close method properly closes the driver.
    """
    repo = BaseRepository(uri="bolt://dummy", user="dummy", password="dummy")
    closed = False

    def dummy_close():
        nonlocal closed
        closed = True

    repo.driver.close = dummy_close
    repo.close()
    assert closed is True
