# Eurovision Song Contest Database Explorer

A web application built with Flask and SQLite to explore the Eurovision Song Contest database.

This project was developed as part of a university database course.

## Table of Contents

- [Eurovision Song Contest Database Explorer](#eurovision-song-contest-database-explorer)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Using Docker](#using-docker)
    - [Using Poetry](#using-poetry)
    - [Using Python Directly](#using-python-directly)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
  - [Contact](#contact)

## Description

This project allows users to browse tables containing information about countries, languages, people, event sponsors, etc., related to the Eurovision Song Contest.
The database and web app were designed and implemented by me as a CRUD (MVC) application using Flask for its simplicity and SQLite for lightweight database management.

## Features

- MVC architecture with CRUD
- SQL usage with a SQLite backend
- Flask web framework
- Docker support

## Installation

To set up this project locally, you will need Docker installed on your machine.

1. Clone the repository to your local machine:

```bash
git clone https://github.com/leo-oli/eurovision-crud-webapp
```

2. Change into the project directory:

```bash
cd eurovision-crud-webapp
```

## Usage

Follow these instructions to run the application:

### Using Docker

1. Build the Docker container:

```bash
docker build -t eurovision-crud-webapp:1.0 .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 eurovision-crud-webapp:1.0
```

3. Open your web browser and navigate to <http://localhost:5000> to explore the Eurovision Song Contest database.

### Using Poetry

Ensure Poetry is installed on your system. Then, follow these steps:

1. Install dependencies using Poetry:

```bash
poetry install
```

2. Run the application

```bash
poetry run python -m src.app
```

3. Open your web browser and navigate to <http://localhost:5000> to explore the Eurovision Song Contest database.

### Using Python Directly

Alternatively, if you prefer using Python directly:

1. Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python -m src.app
```

## Project Structure

- `db/`
  - `dump.sql`: SQL dump file for the Eurovision Song Contest database
- `src/`
  - `app.py`: Flask app file
  - `utils.py`: Some python utilities
  - `templates/`: Jinja2 templates for the web app
  - `models/`
    - `model.py`: MVC model base class
    - `db_tables.py`: Utility dataclasses
    - Other MVC models

## Contributing

Contributions are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with a descriptive message.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Favicon provided under CC-BY 4.0 from [favicon.io](https://favicon.io/emoji-favicons/studio-microphone)

## Contact

For any questions or feedback, please contact Leonid Oliinyk at [leo.oli.github.clubhouse326@simplelogin.com](mailto:leo.oli.github.clubhouse326@simplelogin.com)
