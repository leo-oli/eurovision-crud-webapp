from typing import List
from src.models.db_tables import Event
from src.models.model import Model


class Events(Model):
    """
    Class to handle all the events-related database operations.

    Attributes
    ----------
    table_name : str
        Name of the table in the database.

    Methods
    -------
    get_all()
        Get all events from the database.
    get_by_id(record_id: int)
        Get event details by ID from the database.
    """
    def __init__(self):
        """
        Initialize the Events class with the name of the table in the database.
        """
        super().__init__("events")

    def get_all(self) -> List[Event]:
        """
        Get all events from the database.

        Returns
        -------
        List[Event]
            List of Event objects.
        """
        query = """
            SELECT
                e.event_id,
                e.name,
                e.start_date,
                e.end_date,
                e.city,
                e.venue,
                e.capacity,
                e.slogan,
                e.participating_countries_count,
                c.name AS country_name
            FROM events e
            LEFT JOIN countries c ON e.country_id = c.country_id
        """
        list_of_rows = self.execute_query(query)
        return [Event(**row) for row in list_of_rows]

    def get_by_id(self, record_id: int) -> Event:
        """
        Get event details by ID from the database.

        Parameters
        ----------
        record_id : int
            ID of the event to get.

        Returns
        -------
        Event
            Event object.
        """
        query = """
            SELECT
                e.event_id,
                e.name,
                e.start_date,
                e.end_date,
                e.city,
                e.venue,
                e.capacity,
                e.slogan,
                e.participating_countries_count,
                c.name AS country_name
            FROM events e
            LEFT JOIN countries c ON e.country_id = c.country_id
            WHERE e.event_id = ?
        """
        row = self.execute_query(query, (record_id,))[0]
        return Event(**row)
