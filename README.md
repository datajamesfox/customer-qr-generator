## QR Code Generator for SQLite

This Python project generates unique combinations of names and stores them in an SQLite database to be used to generate QRcodes via API.

### Installation
------------
Install dependencies from requirements.txt:

    pip install -r requirements.txt

### Usage
-----
Run main.py from the top level project folder.

SQLite - database is set as database.db as default. Table is set as race_entrants as default.

    .open database.db
    SELECT * FROM race_entrants;

Run tests.py for unit testing.

### Continuous Integration
-----
CI implemented with GitHub Actions to run unit tests and lint checks.