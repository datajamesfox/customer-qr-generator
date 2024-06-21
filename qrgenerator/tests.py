from modules import Database
from modules import NamePermutations
import unittest
import os
import sqlite3


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = 'test_db'
        self.table = 'test_table'
        self.db = Database(self.database, self.table)
        self.db.create_database()

    def tearDown(self):
        os.remove(f'{self.database}.db')

    def test_create_database(self):
        conn = sqlite3.connect(f'{self.database}.db')
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table}'")
        table_exists = cur.fetchone()
        self.assertIsNotNone(table_exists)
        cur.close()
        conn.close()


class TestNamePermutations(unittest.TestCase):
    def test_generate_permutations(self):
        names = ['John', 'Jane', 'Bob']
        name_permutations = NamePermutations(names, 1)
        permutations = name_permutations.generate_permutations()
        expected_permutation_length = 6
        self.assertEqual(len(permutations), expected_permutation_length)


if __name__ == '__main__':
    unittest.main()
