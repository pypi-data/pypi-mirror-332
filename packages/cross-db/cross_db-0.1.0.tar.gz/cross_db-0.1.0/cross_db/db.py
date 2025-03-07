from typing import Any, Dict, List, Optional, Tuple, Union
from google.cloud.sql.connector import Connector
import pandas as pd
import os


class BaseDB:
    """
    Wrapper class for connecting to a PostgreSQL database using the pg8000 driver.

    Args:
        config (dict): Configuration parameters for the database connection.
            Required keys: host, user, password, database
            Optional keys: app_name
            If config is not provided, environment variables are used.

    Methods:
    --------
    - `select(query, params = None)` : Execute a SQL query and return the results as a pandas DataFrame
    - `execute(query, params = None)` : Execute a single non-SELECT query (INSERT, UPDATE, DELETE)
    - `execute_many(query, params = None)` : Execute a query with multiple parameter sets (bulk operations)
    """

    def __init__(self, config: dict = None):
        if config is None:
            config = {
                "host": os.environ["CLOUDSQL_HOST"],
                "driver": "pg8000",
                "user": os.environ["CLOUDSQL_USER"],
                "password": os.environ["CLOUDSQL_PASSWORD"],
                "database": os.environ["CLOUDSQL_DATABASE"],
                "app_name": None,
            }
            # Validate required environment variables
            missing_vars = [
                k
                for k, v in config.items()
                if k in ["host", "user", "password", "database"] and v is None
            ]
            if missing_vars:
                raise ValueError(
                    f"Missing required environment variables: {', '.join(missing_vars)}"
                )

        self.config = config
        self.connector = Connector()
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()

    def connect(self):
        """Establish a database connection."""
        self.connection = self.connector.connect(
            self.config.get("host"),
            "pg8000",
            user=self.config.get("user"),
            password=self.config.get("password"),
            db=self.config.get("database"),
        )
        self.cursor = self.connection.cursor()

    def close(self):
        """Close the database connection and cursor."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def select(
        self,
        query: str,
        params: Optional[Union[Dict[str, Any], Tuple, List[Any]]] = None,
    ) -> pd.DataFrame:
        """Execute a SQL query and return the results as a pandas DataFrame.

        Args:
            query (str): SQL query to execute

        Returns:
            pandas.DataFrame: Query results as a DataFrame

        Example:
        ```
        # Basic SELECT
        with BaseDB() as db:
            df = db.select("SELECT * FROM violations LIMIT 10")

        # SELECT with parameters
        with BaseDB() as db:
            df = db.select("SELECT * FROM violations WHERE severity > %s", (3,))
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            columns = [desc[0] for desc in self.cursor.description]
            results = self.cursor.fetchall()
            return pd.DataFrame(results, columns=columns)
        except Exception as e:
            print(f"Error executing query: {e}")
            raise e

    def execute(
        self,
        query: str,
        params: Optional[Union[Dict[str, Any], Tuple, List[Any]]] = None,
    ) -> int:
        """Execute a single non-SELECT query (INSERT, UPDATE, DELETE).

        Args:
            query: SQL query to execute
            params: Parameters for the query

        Returns:
            int: Number of affected rows

        Example:
        ```
        # INSERT single row
        with BaseDB() as db:
            db.execute(
                "INSERT INTO violations (id, name, severity) VALUES (%(id)s, %(name)s, %(severity)s)",
                {"id": 1, "name": "Test Violation", "severity": 3}
            )
        """
        try:
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)

            affected_rows = self.cursor.rowcount
            self.connection.commit()
            return affected_rows
        except Exception as e:
            print(f"Error executing query: {e}")
            if self.connection:
                self.connection.rollback()
            raise e

    def execute_many(
        self,
        query: str,
        params_list: List[Dict[str, Any]],
    ) -> int:
        """Execute a query with multiple parameter sets (bulk operations).

        Args:
            query: SQL query to execute
            params_list: List of parameter dictionaries

        Returns:
            int: Number of affected rows

        Example:
        ```
        # Bulk INSERT
        violations = [
            {"id": i, "name": f"Violation {i}", "severity": i % 5}
            for i in range(1, 11)
        ]
        with BaseDB() as db:
            db.execute_many(
                "INSERT INTO violations (id, name, severity) VALUES (%(id)s, %(name)s, %(severity)s)",
                violations
            )
        """
        if not params_list:
            return 0

        try:
            self.cursor.executemany(query, params_list)
            affected_rows = self.cursor.rowcount
            self.connection.commit()
            return affected_rows
        except Exception as e:
            print(f"Error executing query: {e}")
            if self.connection:
                self.connection.rollback()
            raise
