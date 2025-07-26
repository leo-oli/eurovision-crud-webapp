from typing import List
from sqlite3 import DatabaseError, OperationalError
from src.models.db_tables import Language
from src.models.model import Model


class Languages(Model):
    """Class for interacting with the `languages` table in the database."""

    def __init__(self):
        """Initialize the `Languages` class by calling the superclass constructor with the table name."""
        super().__init__("languages")

    def get_all(self) -> List[Language]:
        """Retrieve all records from the `languages` table and return them as a list of `Language` objects."""
        query = """
        SELECT
                l.language_id,
                l.name,
                l.speaker_count,
                l.language_family,
                c.name AS country_name
            FROM languages l
            LEFT JOIN countries c ON l.country_id = c.country_id
        """
        list_of_rows = self.execute_query(query)
        return [Language(**row) for row in list_of_rows]

    def get_by_id(self, record_id: int) -> Language:
        """Retrieve a single record from the `languages` table based on its ID and return it as a `Language` object."""
        query = "SELECT * FROM languages WHERE language_id = ?"
        row = self.execute_query(query, (record_id,))[0]
        return Language(**row)

    def insert(self, record: Language) -> int:
        """Insert a new record into the `languages` table based on the provided `Language` object.

        Returns
        -------
        int
            The ID of the newly inserted record.
        """
        query = "INSERT INTO languages (name, speaker_count, language_family, country_id) VALUES (?, ?, ?, ?)"
        values = tuple(record.dict().values())[1:-1]

        try:
            self.execute_query(query, values)
        except DatabaseError:
            return -1
        return self.cursor.lastrowid

    def is_used(self, record_id: int) -> bool:
        """Check if a language is used in the `sung_in` table.

        Returns
        -------
        bool
            A boolean value indicating whether the language is used (True) or not (False).
        """
        query_count = "SELECT COUNT (*) FROM sung_in WHERE language_id = ?"
        count = self.execute_query(query_count, (record_id,))[0]
        return count.get("COUNT (*)", 0)

    def remove(self, record_id: int) -> bool:
        """Delete a record from the `languages` table based on its ID.

        Raises
        ------
        sqlite3.OperationalError
            If the language is used in the `sung_in` table.

        Returns
        -------
            A boolean value indicating whether the deletion was successful (True) or not (False).
        """
        if self.is_used(record_id):
            raise OperationalError("This record is used somewhere else")
        query = "DELETE FROM languages WHERE language_id = ?"
        self.execute_query(query, (record_id,))
        return bool(self.cursor.rowcount)

    def update(self, record: Language) -> bool:
        """Update a record in the `languages` table based on the provided `Language` object.

        Returns
        -------
        bool
            A boolean value indicating whether the update was successful (True) or not (False).
        """
        query = """
        UPDATE languages SET
            name = ?,
            speaker_count = ?,
            language_family = ?,
            country_id = ?
            WHERE language_id = ?
        """

        record_id = record.language_id
        values = tuple(record.dict().values())[1:-1]
        self.execute_query(query, (*values, record_id))

        return bool(self.cursor.rowcount)
