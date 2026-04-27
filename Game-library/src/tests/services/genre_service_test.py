import unittest
from services.genre_service import GenreService

#luodaan ensin feikki genre repo
class FakeGenreRepository:
    def __init__(self):
        self.genres = [
            {"id": 1, "name": "Action"},
            {"id": 2, "name": "Adventure"},
            {"id": 3, "name": "RPG"}
        ]

    def get_all_genres(self):
        return list(self.genres)

    def get_genre_by_id(self, genre_id):
        for genre in self.genres:
            if genre["id"] == genre_id:
                return genre
        return None

    def get_genre_by_name(self, name):
        for genre in self.genres:
            if genre["name"].lower() == name.lower():
                return genre
        return None

#Sitten luodaan testit, joka käyttää feikki repoa

class TestGenreService(unittest.TestCase):
    def setUp(self):
        self.repo = FakeGenreRepository()
        self.service = GenreService(self.repo)

    def test_get_all_genres(self):
        genres = self.service.get_all_genres()
        self.assertEqual(len(genres), 3)

    def test_get_genre_by_id(self):
        genre = self.service.get_genre_by_id(1)
        self.assertEqual(genre["name"], "Action")

    def test_get_genre_by_name(self):
        genre = self.service.get_genre_by_name("RPG")
        self.assertEqual(genre["id"], 3)
