"""
Script to run QRcode generator functionality.
"""

from modules import Database, NamePermutations, Qrcode
from multiprocessing import Pool
import sqlite3
import time
import logging


def save_qrcodes(database_name, table_name):
    # Connect to db
    conn = sqlite3.connect(f'{database_name}.db')
    cur = conn.cursor()

    # Return table ids
    try:
        cur.execute(f'SELECT id FROM {table_name}')
        for row in cur.fetchall():
            id = row[0]

            # Call API and save QR codes
            qr = Qrcode(id)
            qr.get_qr()

            # 1 query per second due to Free API usage quota limits.
            # https://documentation.image-charts.com/limits-and-quotas/
            time.sleep(1)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        cur.close()
        conn.close()


def main():
    # Set Logging Config
    logging.basicConfig(
        level=logging.INFO,
        filename="filename.log",
        format="%(asctime)s - %(name)s - %(funcName)s - %(message)s")

    # List of names
    names = ['riley', 'james', 'ryan', 'joshi', 'andrew']

    # Generate permutations
    name_permutations = NamePermutations(names, 1000)
    name_list = name_permutations.permutation_multiple()

    # Set db and table names
    database_name = 'database'
    table_name = 'race_entrants'

    # Create database if it doesn't already exist
    db = Database(database_name, table_name)
    db = db.create_database()

    # Split name_list for parallel processing
    half_list = len(name_list) // 2
    batch_1 = name_list[:half_list]
    batch_2 = name_list[half_list:]

    # Insert records using multiprocessing pools
    with Pool(processes=2) as pool:
        pool.map(db.insert_rows, [batch_1, batch_2])

        # Get and save QRcodes from table ID
        save_qrcodes(database_name, table_name)


if __name__ == "__main__":
    main()
