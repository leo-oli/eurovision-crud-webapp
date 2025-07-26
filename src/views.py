from flask import Blueprint, render_template, request, redirect, url_for
from sqlite3 import DatabaseError, OperationalError
from pydantic import ValidationError
from src.models.db_tables import Language, Song
from src.models.languages import Languages
from src.models.countries import Countries
from src.models.events import Events
from src.models.songs import Songs
from src.utils import tables

views_bp = Blueprint("views", __name__)


@views_bp.route("/")
def index():
    """Render the index template with the available tables."""
    return render_template("index.html", active_page="Home", tables=tables)


@views_bp.route("/countries")
def countries():
    """Retrieve all countries from the database and render the countries template."""
    countries = Countries()
    rows = countries.get_all()
    return render_template(
        "countries.html", active_page="Countries", countries=rows, tables=tables
    )


@views_bp.route("/languages")
def languages():
    """Retrieve all languages from the database and render the languages template."""
    languages = Languages()
    rows = languages.get_all()
    return render_template(
        "languages.html", active_page="Languages", languages=rows, tables=tables
    )


@views_bp.route("/songs")
def songs():
    """Retrieve all songs from the database and render the songs template."""
    songs = Songs()
    rows = songs.get_all()
    return render_template("songs.html", active_page="Songs", songs=rows, tables=tables)


@views_bp.route("/events")
def events():
    """Retrieve all events from the database and render the events template."""
    events = Events()
    rows = events.get_all()
    return render_template(
        "events.html", active_page="Events", events=rows, tables=tables
    )


@views_bp.route("/error")
def error():
    """Render the error template with an error message."""
    error_text = request.args.get("error_text")
    return render_template("error.html", error_text=error_text, tables=tables)


@views_bp.route("/language/delete", methods=["POST"])
def delete_language():
    """Handle the deletion of a language from the database."""
    languages = Languages()
    language_id = int(request.form["language_id"])

    try:
        was_removed = languages.remove(language_id)
    except OperationalError:
        rows = languages.get_all()
        return render_template(
            "languages.html",
            active_page="Languages",
            languages=rows,
            tables=tables,
            is_used_error=True,
        )
    except DatabaseError as e:
        return redirect(url_for(".error", error_text=e))

    if not was_removed:
        return redirect(
            url_for(".error", error_text="No data was deleted for some reason")
        )

    return redirect(url_for(".languages"))


@views_bp.route("/songs/insert")
def insert_song_form():
    """Render the song insertion form."""
    all_countries = Countries().get_all()
    all_events = Events().get_all()
    return render_template(
        "song_form.html",
        tables=tables,
        song=None,
        languages=[],
        events=all_events,
        countries=all_countries,
    )


@views_bp.route("/songs/insert", methods=["POST"])
def insert_song_action():
    """Handle the insertion of a new song and its associated languages into the database."""
    inputs = request.form.to_dict()

    # Handle empty place and votes fields
    if inputs["place"] == "":
        inputs["place"] = None
    if inputs["votes"] == "":
        inputs["votes"] = None

    # Extract languages data from the form
    languages_data = []
    for i in range(len(inputs)):
        if f"name_{i}" in inputs:
            language = {
                "name": inputs[f"name_{i}"],
                "speaker_count": int(inputs[f"speaker_count_{i}"]),
                "language_family": inputs[f"language_family_{i}"],
                "country_id": int(inputs[f"country_id_{i}"]),
            }
            languages_data.append(language)
        else:
            continue

    songs = Songs()

    try:
        # Convert the inputs dictionary to a Song object
        song = Song(**inputs)

        # Convert the languages data to a list of Language objects
        languages = [Language(**language_data) for language_data in languages_data]

        # Insert the song and its associated languages
        song_id = songs.insert(song, languages)

    except ValidationError:
        all_countries = Countries().get_all()
        all_events = Events().get_all()
        return render_template(
            "song_form.html",
            tables=tables,
            song=None,
            languages=[],
            events=all_events,
            countries=all_countries,
            validation_error=True,
        )

    if song_id == -1:
        return redirect(
            url_for(".error", error_text="No data was inserted for some reason")
        )

    return redirect(url_for(".songs"))


@views_bp.route("/songs/edit", methods=["POST"])
def edit_song_form():
    """Handle the display of the song editing form."""
    if request.form["button"] == "Submit":
        return edit_song_action()

    all_countries = Countries().get_all()
    all_events = Events().get_all()
    songs = Songs()

    song_id = int(request.form.get("song_id"))
    song = songs.get_by_id(song_id)
    languages = songs.get_languages_by_song_id(song_id)
    return render_template(
        "song_form.html",
        tables=tables,
        song=song,
        languages=languages,
        events=all_events,
        countries=all_countries,
        action="edit",
    )


@views_bp.route("/songs/edit", methods=["POST"])
def edit_song_action():
    """Handle the editing of an existing song and its associated languages in the database."""
    inputs = request.form.to_dict()

    # Handle empty place and votes fields
    if inputs["place"] == "":
        inputs["place"] = None
    if inputs["votes"] == "":
        inputs["votes"] = None

    # Extract languages data from the form
    languages_data = []
    for i in range(len(inputs)):
        if f"name_{i}" in inputs:
            language = {
                "language_id": inputs.get(f"language_id_{i}"),
                "name": inputs[f"name_{i}"],
                "speaker_count": int(inputs[f"speaker_count_{i}"]),
                "language_family": inputs[f"language_family_{i}"],
                "country_id": int(inputs[f"country_id_{i}"]),
            }
            languages_data.append(language)
        else:
            continue

    songs = Songs()

    try:
        # Convert the inputs dictionary to a Song object
        song = Song(**inputs)

        # Convert the languages data to a list of Language objects
        languages = [Language(**language_data) for language_data in languages_data]

        # Update the song and its associated languages
        song_id = songs.update(song, languages)

    except ValidationError:
        all_countries = Countries().get_all()
        all_events = Events().get_all()
        return render_template(
            "song_form.html",
            tables=tables,
            song=None,
            languages=[],
            events=all_events,
            countries=all_countries,
            validation_error=True,
        )

    if song_id == -1:
        return redirect(
            url_for(".error", error_text="No data was updated for some reason")
        )

    return redirect(url_for(".songs"))


@views_bp.route("/songs/delete", methods=["POST"])
def delete_song():
    """Handle the deletion of a song from the database."""
    songs = Songs()
    song_id = int(request.form["song_id"])

    try:
        was_removed = songs.remove(song_id)
    except DatabaseError as e:
        return redirect(url_for(".error", error_text=e))

    if not was_removed:
        return redirect(
            url_for(".error", error_text="No data was deleted for some reason")
        )

    return redirect(url_for(".songs"))


@views_bp.route("/filters")
def filters():
    events = Events()
    songs = Songs()
    genres = songs.get_genres()
    all_events = events.get_all()
    return render_template(
        "filters.html", tables=tables, events=all_events, genres=genres
    )


@views_bp.route("/filters", methods=["POST"])
def filtered_songs():
    inputs = request.form.to_dict()
    inputs["choose_event_flag"] = int(inputs.get("choose_event_flag") is not None)
    return redirect(url_for(".report", **inputs))


@views_bp.route("/report")
def report():
    inputs = request.args
    songs = Songs()
    reports = songs.get_reports(**inputs)
    reports_aggregations = songs.get_report_aggregations(**inputs)
    report_mega_aggregations = songs.get_report_mega_aggregation(**inputs)
    return render_template(
        "report.html",
        tables=tables,
        inputs=inputs,
        reports=reports,
        aggregations=reports_aggregations,
        total=report_mega_aggregations,
    )
