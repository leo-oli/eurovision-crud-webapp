from typing import List
from src.models.db_tables import Country
from src.models.model import Model


class Countries(Model):
    """A class representing the countries table in the database."""

    def __init__(self):
        """Initialize the Countries class by calling the parent constructor with the table name."""
        super().__init__("countries")

    def get_all(self) -> List[Country]:
        """Retrieve all records from the countries table and return them as a list of Country objects.

        Returns
        -------
        List[Country]
            A list of Country objects.
        """
        query = "SELECT * FROM countries"
        list_of_rows = self.execute_query(query)
        return [Country(**row) for row in list_of_rows]

    def get_by_id(self, record_id: int) -> Country:
        """Retrieve a single record from the countries table based on its ID and return it as a Country object.

        Parameters
        ----------
        record_id : int
            The ID of the record to retrieve.

        Returns
        -------
        Country
            A Country object.
        """
        query = "SELECT * FROM countries WHERE country_id = ?"
        row = self.execute_query(query, (record_id,))[0]
        return Country(**row)
