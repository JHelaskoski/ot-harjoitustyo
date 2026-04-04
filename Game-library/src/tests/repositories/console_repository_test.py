import unittest
import sqlite3
from repositories.console_repository import ConsoleRepository

class TestConsoleRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repo = ConsoleRepository(self.connection)

        cursor = self.connection.cursor()
        cursor.execute("""
            create table consoles (
                id integer primary key,
                name text
            )
        """)
        self.connection.commit()

    def test_add_console_correctly(self):
        self.repo.add_console("Testconsole")

        consoles = self.repo.get_all_consoles()

        self.assertEqual(len(consoles), 1)
        console = consoles[0]

        self.assertEqual(console["name"], "Testconsole")

    def test_get_all_consoles(self):
        self.repo.add_console("Testconsole1")
        self.repo.add_console("Testconsole2")

        consoles = self.repo.get_all_consoles()

        self.assertEqual(len(consoles), 2)
        self.assertEqual(consoles[0]["name"], "Testconsole1")
        self.assertEqual(consoles[1]["name"], "Testconsole2")
