import unittest
import sqlite3
from repositories.genre_repository import GenreRepository

class TestGenreRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repo = GenreRepository(self.connection)

        # Luodaan taulu testitietokantaan
        cursor = self.connection.cursor()
        cursor.execute("""
            create table genres (
                id integer primary key,
                name text
            )
        """)
        self.connection.commit()

    def test_add_genre_correctly(self):
        self.repo.add_genre("Action")

        genres = self.repo.get_all_genres()

        self.assertEqual(len(genres), 1)
        genre = genres[0]

        self.assertEqual(genre["name"], "Action")

    def test_get_genre_by_name(self):
        self.repo.add_genre("Adventure")

        genre = self.repo.get_genre_by_name("Adventure")
        self.assertIsNotNone(genre)
        self.assertEqual(genre["name"], "Adventure")

    def test_get_genre_by_id(self):
        self.repo.add_genre("RPG")

        genre = self.repo.get_genre_by_id(1)
        self.assertIsNotNone(genre)
        self.assertEqual(genre["name"], "RPG")
