import unittest
from services.game_service import GameService

class FakeGameRepository:
    def __init__(self):
        self.games = []
        self.next_id = 1

    def add_game(self, name, console_model_id, release_year, status, genre_ids):
        game = {
            "id": self.next_id,
            "name": name,
            "console_model_id": console_model_id,
            "release_year": release_year,
            "status": status,
            "genre_ids": genre_ids
        }
        self.games.append(game)
        self.next_id += 1
        return game

    def get_all_games(self):
        return list(self.games)

    def get_game_by_id(self, game_id):
        for game in self.games:
            if game["id"] == game_id:
                return game
        return None

    def get_game_by_status(self, status):
        return [game for game in self.games if game["status"] == status]

    def update_status(self, game_id, new_status):
        for game in self.games:
            if game["id"] == game_id:
                game["status"] = new_status
                return game
        return None

    def get_genres_for_game(self, game_id: int):
        game = self.get_game_by_id(game_id)
        if game:
            return game["genre_ids"]
        return []

    def get_games_by_genre(self, genre_id):
        return [game for game in self.games if genre_id in game["genre_ids"]]

    def delete_game(self, game_id):
        for game in self.games:
            if game["id"] == game_id:
                self.games.remove(game)
                return True
        return False

class FakeConsoleModelRepository:
    def __init__(self):
        self.models = {1: {"id": 1}, 2: {"id": 2}}

    def get_by_id(self, model_id):
        return self.models.get(model_id)


class FakeGenreRepository:
    def __init__(self):
        self.genres = {1: "Action", 2: "RPG"}

    def get_genre_by_id(self, genre_id):
        return self.genres.get(genre_id)


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_repo = FakeGameRepository()
        self.console_model_repo = FakeConsoleModelRepository()
        self.genre_repo = FakeGenreRepository()
        self.service = GameService(self.game_repo, self.console_model_repo, self.genre_repo)

    def test_add_game_correctly(self):
        game = self.service.add_game("Testi", 1, 2026, [1, 2])

        self.assertEqual(game["name"], "Testi")
        self.assertEqual(game["console_model_id"], 1)
        self.assertEqual(game["release_year"], 2026)
        self.assertEqual(game["status"], "wishlist")
        self.assertEqual(game["genre_ids"], [1, 2])

    def test_add_game_empty_name_raises(self):
        with self.assertRaises(ValueError):
            self.service.add_game("", 1, 2026, [1, 2])

    def test_add_game_negative_console_model_id(self):
        with self.assertRaises(ValueError):
            self.service.add_game("Testi", -1, 2026, [1, 2])

    def test_add_game_negative_release_year(self):
        with self.assertRaises(ValueError):
            self.service.add_game("Testi", 1, -2026, [1, 2])

    def test_add_game_invalid_genre_id(self):
        with self.assertRaises(ValueError):
            self.service.add_game("Testi", 1, 2026, [999])

    def test_get_all_games(self):
        self.service.add_game("Testi1", 1, 2026, [1, 2])
        self.service.add_game("Testi2", 2, 2025, [1, 2])

        games = self.service.get_all_games()
        self.assertEqual(len(games), 2)

    def test_get_game_by_id(self):
        game = self.service.add_game("Testi", 1, 2026, [1, 2])
        asked_game = self.service.get_game_by_id(game["id"])
        self.assertEqual(asked_game["name"], "Testi")

    def test_get_game_by_status(self):
        self.service.add_game("Testi1", 1, 2026, [1, 2])
        self.service.add_game("Testi2", 2, 2025, [1, 2])
        self.service.change_status(1, "playing")

        playing_games = self.service.get_game_by_status("playing")
        wishlist_games = self.service.get_game_by_status("wishlist")

        self.assertEqual(len(playing_games), 1)
        self.assertEqual(len(wishlist_games), 1)

    def test_get_game_by_status_invalid_status(self):
        with self.assertRaises(ValueError):
            self.service.get_game_by_status("invalid_status")

    def test_change_status_game_not_found(self):
        with self.assertRaises(ValueError):
            self.service.change_status(999, "playing")

    def test_change_status_invalid_status(self):
        game = self.service.add_game("Testi", 1, 2026, [1, 2])
        with self.assertRaises(ValueError):
            self.service.change_status(game["id"], "invalid_status")

    def test_delete_game(self):
        game = self.service.add_game("Testi", 1, 2026, [1, 2])
        self.service.delete_game(game["id"])
        self.assertIsNone(self.service.get_game_by_id(game["id"]))

    def test_delete_game_not_found(self):
        with self.assertRaises(ValueError):
            self.service.delete_game(999)

    def test_get_genres_for_game(self):
        game = self.service.add_game("Testi", 1, 2026, [1, 2])
        genres = self.service.get_genres_for_game(game["id"])
        self.assertEqual(genres, [1, 2])

    def test_get_games_by_genre(self):
        self.service.add_game("Testi1", 1, 2026, [1])
        self.service.add_game("Testi2", 2, 2025, [2])
        games = self.service.get_games_by_genre(1)
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0]["name"], "Testi1")

    def test_get_games_by_genre_invalid_genre_id(self):
        with self.assertRaises(ValueError):
            self.service.get_games_by_genre(999)
