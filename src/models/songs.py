from typing import List
from sqlite3 import DatabaseError
from src.models.db_tables import Song, Language, Report, ReportAggregation
from src.models.model import Model
from src.models.languages import Languages


class Songs(Model):
    """Class to represent the songs table in the database."""
    def __init__(self):
        """Initialize the class and create an instance of the Languages class."""
        super().__init__("songs")
        self.languages = Languages()

    def get_all(self) -> List[Song]:
        """Get all songs from the songs table and join it with the countries and events tables."""
        query = """
            SELECT
                s.song_id,
                s.title,
                s.composition_date,
                s.duration,
                s.genre,
                s.place,
                s.votes,
                s.country_id,
                c.name AS country_name,
                s.event_id,
                e.name AS event_name
            FROM songs s
            LEFT JOIN countries c ON s.country_id = c.country_id
            LEFT JOIN events e ON s.event_id = e.event_id
            """

        list_of_rows = self.execute_query(query)
        return [Song(**row) for row in list_of_rows]

    def get_by_id(self, record_id: int) -> Song:
        """Get a single song by its ID and join it with the countries and events tables."""
        query = """
            SELECT
                s.song_id,
                s.title,
                s.composition_date,
                s.duration,
                s.genre,
                s.place,
                s.votes,
                s.country_id,
                c.name AS country_name,
                s.event_id,
                e.name AS event_name
            FROM songs s
            LEFT JOIN countries c ON s.country_id = c.country_id
            LEFT JOIN events e ON s.event_id = e.event_id
            WHERE song_id = ?
            """

        row = self.execute_query(query, (record_id,))[0]
        return Song(**row)

    def get_languages_by_song_id(self, song_id: int) -> List[Language]:
        """Get all languages associated with a song by its ID."""
        query = """
            SELECT
                l.language_id,
                l.name,
                l.speaker_count,
                l.language_family,
                l.country_id,
                c.name AS country_name
            FROM languages l
            JOIN sung_in s ON l.language_id = s.language_id
            JOIN countries c ON l.country_id = c.country_id
            WHERE s.song_id = ?
        """
        rows = self.execute_query(query, (song_id,))
        return [Language(**row) for row in rows]

    def get_genres(self) -> List[str]:
        """Retrieve all genres from the countries table.

        Returns
        -------
        List[str]
            List of genres
        """
        query = "SELECT DISTINCT songs.genre FROM songs"
        rows = self.execute_query(query)
        return [row.get("genre") for row in rows]

    def get_reports(self, **kwargs) -> List[Report]:
        query = """
            SELECT
                s.title as song_title,
                s.composition_date,
                s.duration,
                s.genre,
                cs.name AS country_name,
                e.slogan AS event_slogan,
                UPPER(l.name) AS language_name,
                IIF(e.city IS NOT NULL, CONCAT(STRFTIME('%Y', e.start_date), ' ', e.city), NULL) AS event_name,  -- YEAR(e.start_date))
                l.speaker_count,
                CONCAT(ROUND(l.percentage_of_speakers * 100), '%') AS percentage_of_speakers,
                cl.name AS language_country_name
            FROM songs s
            LEFT JOIN events e ON s.event_id = e.event_id
            JOIN sung_in si ON s.song_id = si.song_id
            JOIN languages l ON si.language_id = l.language_id
            JOIN countries cl ON l.country_id = cl.country_id
            JOIN countries cs ON s.country_id = cs.country_id
            WHERE s.composition_date >= ? AND s.composition_date <= ? AND s.genre = ? AND CASE WHEN ? THEN s.event_id = ? ELSE TRUE END
            ORDER BY s.composition_date
        """
        rows = self.execute_query(query, (kwargs.get("start_date"), kwargs.get("end_date"), kwargs.get("genre"), kwargs.get("choose_event_flag"), kwargs.get("event_id")))
        return [Report(**row) for row in rows]

    def get_report_aggregations(self, **kwargs):
        query = """
            SELECT
                s.title AS song_title,
                ROUND(AVG(LENGTH(c.name)), 2) AS avg_country_name_length,
                COUNT(DISTINCT l.name) AS count_languages,
                SUM(l.speaker_count) AS total_speaker_count,
                CONCAT(ROUND(MAX(l.percentage_of_speakers) * 100), '%') AS max_percentage_of_speakers
            FROM songs s
            LEFT JOIN events e ON s.event_id = e.event_id
            JOIN sung_in si ON s.song_id = si.song_id
            JOIN languages l ON si.language_id = l.language_id
            JOIN countries c ON l.country_id = c.country_id
            WHERE s.composition_date >= ? AND s.composition_date <= ? AND s.genre = ? AND CASE WHEN ? THEN s.event_id = ? ELSE TRUE END
            GROUP BY s.title
        """
        rows = self.execute_query(query, (kwargs.get("start_date"), kwargs.get("end_date"), kwargs.get("genre"), kwargs.get("choose_event_flag"), kwargs.get("event_id")))
        return [ReportAggregation(**row) for row in rows]

    def get_report_mega_aggregation(self, **kwargs):
        query = """
            SELECT
                ROUND(AVG(LENGTH(c.name)), 2) AS avg_country_name_length,
                COUNT(DISTINCT l.name) AS count_languages,
                SUM(l.speaker_count) AS total_speaker_count,
                CONCAT(ROUND(MAX(l.percentage_of_speakers) * 100), '%') AS max_percentage_of_speakers
            FROM songs s
            LEFT JOIN events e ON s.event_id = e.event_id
            JOIN sung_in si ON s.song_id = si.song_id
            JOIN languages l ON si.language_id = l.language_id
            JOIN countries c ON l.country_id = c.country_id
            WHERE s.composition_date >= ? AND s.composition_date <= ? AND s.genre = ? AND CASE WHEN ? THEN s.event_id = ? ELSE TRUE END
        """
        row = self.execute_query(query, (kwargs.get("start_date"), kwargs.get("end_date"), kwargs.get("genre"), kwargs.get("choose_event_flag"), kwargs.get("event_id")))[0]
        return ReportAggregation(**row)

    def insert(self, record: Song, languages: List[Language]) -> int:
        """Insert a new song and its associated languages into the database."""
        query = """
            INSERT INTO songs (
                title,
                composition_date,
                duration,
                genre,
                place,
                votes,
                country_id,
                event_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = tuple(record.dict().values())[1:-2]

        try:
            self.execute_query(query, values)
        except DatabaseError:
            return -1

        song_id = int(self.cursor.lastrowid)

        for language in languages:
            language_id = self.languages.insert(language)
            self.insert_sung_in(song_id, language_id)

        return song_id

    def insert_sung_in(self, song_id: int, language_id: int) -> bool:
        """Insert a new record into the sung_in table to associate a language with a song."""
        query = "INSERT INTO sung_in (song_id, language_id) VALUES (?, ?)"
        try:
            self.execute_query(query, (song_id, language_id))
        except DatabaseError:
            return False
        return True

    def remove(self, record_id: int) -> bool:
        """Delete a song and its associated languages from the database."""
        query = "DELETE FROM songs WHERE song_id = ?"
        self.execute_query(query, (record_id,))
        query = "DELETE FROM sung_in WHERE song_id = ?"
        self.execute_query(query, (record_id,))
        return bool(self.cursor.rowcount)

    def update(self, record: Song, languages: List[Language]) -> bool:
        """Update a song and its associated languages in the database."""

        # Create a map of existing languages for the song
        existing_languages = self.get_languages_by_song_id(record.song_id)
        language_map = {lang.language_id: lang for lang in existing_languages}

        # Update or insert each language
        for lang in languages:
            if lang.language_id is not None and lang.language_id in language_map:
                # Update existing language
                self.languages.update(lang)
            else:
                # Insert new language
                lang.language_id = self.languages.insert(lang)

            # Update the sung_in table to associate the language with the song
            self.execute_query("INSERT OR REPLACE INTO sung_in (song_id, language_id) VALUES (?, ?)", (record.song_id, lang.language_id))

        # Delete any languages that were removed from the song
        for lang_id in language_map.keys():
            if lang_id not in [lang.language_id for lang in languages]:
                self.execute_query("DELETE FROM sung_in WHERE song_id = ? AND language_id = ?", (record.song_id, lang_id))

        # Update the song itself
        query = """
            UPDATE songs SET
                title = ?,
                composition_date = ?,
                duration = ?,
                genre = ?,
                place = ?,
                votes = ?,
                country_id = ?,
                event_id = ?
            WHERE song_id = ?
            """

        record_id = record.song_id
        values = tuple(record.dict().values())[1:-2]
        self.execute_query(query, (*values, record_id))

        return bool(self.cursor.rowcount)
