import unittest
import sqlite3
from repositories.console_model_repository import ConsoleModelRepository

class TestConsoleModelRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repo = ConsoleModelRepository(self.connection)

        cursor = self.connection.cursor()
        cursor.execute("""
                    create table console_models (
                        id integer primary key,
                        console_id integer,
                        name text
                    );
                    """)
        self.connection.commit()

    def test_add_console_model_correctly(self):
        self.repo.add_console_model(1, "Testmodel")

        cursor = self.connection.cursor()
        cursor.execute("select * from console_models")
        models = cursor.fetchall()

        self.assertEqual(len(models), 1)
        model = models[0]

        self.assertEqual(model["console_id"], 1)
        self.assertEqual(model["name"], "Testmodel")

    def test_get_console_models_by_console_id(self):
        self.repo.add_console_model(1, "Testmodel1")
        self.repo.add_console_model(2, "Testmodel2")

        models = self.repo.get_console_models_by_console_id(1)

        self.assertEqual(len(models), 1)
        self.assertEqual(models[0]["name"], "Testmodel1")

    def test_get_all_console_models(self):
        self.repo.add_console_model(1, "Testmodel1")
        self.repo.add_console_model(2, "Testmodel2")

        models = self.repo.get_all_console_models()

        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["name"], "Testmodel1")
        self.assertEqual(models[1]["name"], "Testmodel2")
