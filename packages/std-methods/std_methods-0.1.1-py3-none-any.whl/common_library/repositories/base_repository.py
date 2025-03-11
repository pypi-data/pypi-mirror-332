import os
import logging
from typing import Optional, Dict, Any, List
from neo4j import GraphDatabase, Driver


class BaseRepository:
    """
    BaseRepository encapsulates common operations for interacting with a Neo4j database.

    Attributes:
        driver (Driver): The Neo4j driver instance.
        logger (Logger): Logger instance for this class.

    Methods:
        close(): Closes the Neo4j driver connection.
        execute_query(query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            Executes a Cypher query and returns the result as a list of records.
    """

    def __init__(
        self,
        uri: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
    ):
        """
        Initialize the BaseRepository with connection details for Neo4j.

        Parameters:
            uri (str, optional): The URI of the Neo4j instance.
                Defaults to the environment variable NEO4J_URI or "bolt://neo4j:7687".
            user (str, optional): The username for Neo4j.
                Defaults to the environment variable NEO4J_USER or "neo4j".
            password (str, optional): The password for Neo4j.
                Defaults to the environment variable NEO4J_PASSWORD or "secret".
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://neo4j:7687")
        self.user = user or os.getenv("NEO4J_USER", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD", "secret")

        self.logger.info(
            f"Initializing connection to Neo4j at {self.uri} with user {self.user}"
        )

        try:
            self.driver: Driver = GraphDatabase.driver(
                self.uri, auth=(self.user, self.password)
            )
            # Test the connection with a simple query.
            with self.driver.session() as session:
                session.run("RETURN 1")
            self.logger.info("Connected to Neo4j successfully.")
        except Exception as exc:
            self.logger.error(f"Failed to connect to Neo4j: {exc}", exc_info=True)
            raise

    def close(self) -> None:
        """
        Closes the Neo4j driver connection.
        Should be called when the repository is no longer needed.
        """
        if hasattr(self, "driver") and self.driver:
            self.driver.close()
            self.logger.info("Neo4j driver connection closed.")

    def execute_query(
        self, query: str, parameters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Executes a Cypher query using a managed session.

        Parameters:
            query (str): The Cypher query to execute.
            parameters (Dict[str, Any], optional): The parameters for the query.

        Returns:
            List[Dict[str, Any]]: The result of the query as a list of records.

        Raises:
            Exception: Re-raises any exception that occurs during query execution after logging.
        """
        self.logger.debug(f"Executing query: {query} with parameters: {parameters}")
        try:
            with self.driver.session() as session:
                result = session.run(query, parameters or {})
                data = result.data()
                if not data:
                    self.logger.warning(f"Query returned no results: {query}")
                return data
        except Exception as exc:
            self.logger.error(
                f"Error executing query: {query} with parameters: {parameters}. Exception: {exc}",
                exc_info=True,
            )
            raise
