from datetime import date 
from pydantic import BaseModel, field_validator
from ..utils import check_non_empty_string, check_non_negative_int, check_date

class Country(BaseModel):
    """Represents a country."""

    country_id: int
    name: str
    capital: str
    region: str
    population: int
    area: int
    phone_code: int
    country_code: str
    currency: str


class Event(BaseModel):
    """Represents an event."""

    event_id: int
    name: str | None = None
    start_date: date
    end_date: date
    city: str
    venue: str
    capacity: int
    slogan: str | None = None
    participating_countries_count: int
    country_name: str  # hosted_in

class Language(BaseModel):
    """Represents a language."""

    language_id: int | None = None
    name: str
    speaker_count: int
    language_family: str
    country_id: int | None = None  # spoken_in
    country_name: str | None = None

    @field_validator("name", "language_family")
    @classmethod
    def validate_non_empty_string(cls, value):
        return check_non_empty_string(value)

    @field_validator("speaker_count")
    @classmethod
    def validate_non_negative_int(cls, value):
        return check_non_negative_int(value)


class Performer(BaseModel):
    """Represents a performer."""

    performer_id: int | None = None
    stage_name: str
    is_band: bool
    career_start_year: int
    country_id: int  # is_from
    country_name: str | None = None

    @field_validator("stage_name")
    @classmethod
    def validate_non_empty_string(cls, value):
        return check_non_empty_string(value)

    @field_validator("career_start_year", "country_id")
    @classmethod
    def validate_non_negative_int(cls, value):
        return check_non_negative_int(value)

    @field_validator("career_start_year")
    @classmethod
    def validate_career_start_year(cls, value):
        if value < 1800:
            raise ValueError("Career start year must be after 1956.")
        return value


class Song(BaseModel):
    """Represents a song."""

    song_id: int | None = None
    title: str
    composition_date: date
    duration: int
    genre: str
    place: int | None = None
    votes: int | None = None
    country_id: int  # performed_by
    event_id: int | None = None  # participates_in
    country_name: str | None = None
    event_name: str | None = None

    @field_validator("title", "genre")
    @classmethod
    def validate_non_empty_string(cls, value):
        return check_non_empty_string(value)

    @field_validator("composition_date")
    @classmethod
    def validate_date(cls, value):
        return check_date(value)

    @field_validator("duration", "place", "votes", "country_id", "event_id")
    @classmethod
    def validate_non_negative_int(cls, value):
        return check_non_negative_int(value)

class Report(BaseModel):
    """Represents a table generated as a report."""

    song_title: str
    composition_date: date
    duration: int
    genre: str
    country_name: str
    event_slogan: str | None = None
    language_name: str
    event_name: str | None = None
    speaker_count: int
    language_country_name: str
    percentage_of_speakers: str

class ReportAggregation(BaseModel):
    """Represents a row of aggregated data."""

    song_title: str | None = None
    avg_country_name_length: float | None = None
    count_languages: int = 0
    total_speaker_count: int | None = None
    max_percentage_of_speakers: str | None = None
