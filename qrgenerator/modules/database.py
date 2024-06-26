"""
Module to manage SQLite database operations.
"""

import sqlite3
import logging


class Database:
    """
    Create database, table and insert records.
    """

    def __init__(self, database, table):
        """
        Initialize with database and table names. Initialise Logging.
        """
        self.database = database
        self.table = table
        self.logger = logging.getLogger(self.__class__.__name__)

    def create_database(self):
        """
        Create database and table.
        """
        conn = sqlite3.connect(f'{self.database}.db')
        cur = conn.cursor()

        # Create database table if it does not exist.
        try:
            cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.table} (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT
                                        NOT NULL,
                                        FirstName TEXT,
                                        LastName TEXT,
                                        CreatedDatetime DATETIME DEFAULT
                                        CURRENT_TIMESTAMP NOT NULL
                                    )''')
            conn.commit()
            self.logger.info(f"Table '{self.table}' created successfully.")

        except Exception as e:
            self.logger.error(f"Error: {e}", exc_info=True)
            conn.rollback()

        finally:
            cur.close()
            conn.close()

        return self

    def insert_rows(self, name_list):
        """
        Insert records from list.
        """
        conn = sqlite3.connect(f'{self.database}.db')
        cur = conn.cursor()

        # Insert into table from list
        try:
            cur.executemany(
                f"""INSERT INTO {self.table} (FirstName, LastName)
                VALUES (?, ?)""", name_list)
            conn.commit()

        except Exception as e:
            logging.error(f"Error: {e}")
            conn.rollback()

        finally:
            cur.close()
            conn.close()
