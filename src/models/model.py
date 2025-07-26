from typing import Any, Tuple, Dict, List
import sqlite3
from ..utils import DB_PATH


class Model:
    """Base class for all models"""

    def __init__(self, table_name: str):
        """Initialize the database connection and table name"""
        self.db_path = DB_PATH
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __enter__(self):
        """Enter the context manager and return the cursor object"""
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Commit any changes made to the database and close the connection"""
        self.connection.commit()

    def execute_query(self, query: str, parameters: Tuple = ()) -> List[Dict[str, Any]]:
        """Execute an SQL query and fetch the results

        Parameters
        ----------
        query : str
            The SQL query to execute
        parameters : Tuple, optional
            The parameters to pass to the query, by default ()

        Returns
        -------
        List[Dict[str, Any]]
            A list of dictionaries containing the query results

        Raises
        ------
        sqlite3.DatabaseError
        """
        try:
            with self:
                self.cursor.execute(query, parameters)
                result = self.cursor.fetchall()
        except sqlite3.Error as e:
            raise sqlite3.DatabaseError(f"Some error during query execution occurred: {e}")

        return [dict(row) for row in result]

    def get_columns(self) -> Tuple[str, ...]:
        """Get table columns

        Returns
        -------
        Tuple[str, ...]
            Tuple of table column names
        """
        query = f"PRAGMA table_info({self.table_name})"
        with self:
            cursor2 = self.cursor.execute(query)
        columns = tuple(row[1] for row in cursor2)
        return columns

    def get_all(self) -> List[Dict[str, Any]]:
        """Read all records from the table

        Returns
        -------
        List[Dict[str, Any]]
            A list of dictionaries containing all records in the table
        """
        query = f"SELECT * FROM {self.table_name}"
        return self.execute_query(query)

    def get_by_id(self, record_id: int) -> Dict[str, Any]:
        """Read a single record by its ID

        Parameters
        ----------
        record_id : int
            ID of the record

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the record with the specified ID
        """
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        return self.execute_query(query, (record_id,))[0]