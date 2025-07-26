import os
from pathlib import Path
from dataclasses import dataclass
from typing import Tuple, List
from datetime import date


@dataclass
class Table:
    name: str
    desc: str
    link: str


PROJECT_ROOT_DIR = Path(__file__).parents[1]  # utils.py is stored in website/src/, so two directories up
DB_PATH = os.path.join(PROJECT_ROOT_DIR, "db", "eurovisiondb.sqlite")
FIRST_EUROVISION_DATE = date(1956, 5, 24)

tables = [
    Table("Countries", "Countries participating in Eurovision Song Contest", "/countries"),
    Table("Languages", "Languages spoken in Eurovision Song Contest", "/languages"),
    Table("Songs", "Songs sung in Eurovision Song Contest", "/songs"),
    Table("Events", "Events themselves", "/events"),
    Table("Report", "Data filtering", "/filters"),
]


def clean_column(column: str) -> str:
    """Clean a column name

    Parameters
    ----------
    column : str
        Input column name

    Returns
    -------
    str
        Cleaned column name
    """
    return column.title().replace("_Id", "_ID").replace("_", " ")


def clean_columns(columns: Tuple[str]) -> List[str]:
    """Clean a list of column names

    Parameters
    ----------
    columns : List[str]
        List of column names

    Returns
    -------
    List[str]
        Cleaned list of column names
    """
    return [clean_column(column) for column in columns]


def check_non_empty_string(value: str) -> str:
    """Validate a string

    Parameters
    ----------
    value : str

    Returns
    -------
    str
        value

    Raises
    ------
    ValueError
        If the string is empty
    """
    if not value or not value.strip():
        raise ValueError("This field cannot be empty or contain only whitespace.")
    return value


def check_non_negative_int(value: int, zero: int = 0) -> int:
    """Validate an int

    Parameters
    ----------
    value : int

    Returns
    -------
    int
        value

    Raises
    ------
    ValueError
        If the number is negative
    """
    if value is None:
        return value
    if value < zero:
        raise ValueError("This field must be a non-negative integer.")
    return value


def check_date(value: date) -> date:
    """Validate a date

    Parameters
    ----------
    value : date

    Returns
    -------
    date
        value

    Raises
    ------
    ValueError
        If the date is before first Eurovision (1956-5-24)
    """
    if value < FIRST_EUROVISION_DATE:
        raise ValueError("Date must be after 1956-5-24.")
    return value
