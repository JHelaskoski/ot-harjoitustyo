import unittest
import sqlite3
from repositories.game_repository import GameRepository
from entities.game import Game


class TestGameRepository(unittest.TestCase):
    def setUp(self):
        # Luodaan testitietokanta muistiin
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row

        # Luodaan repositorio, joka käyttää testitietokantaa
        self.repo = GameRepository(self.connection)

        # Luodaan taulu testitietokantaan
        cursor = self.connection.cursor()
        cursor.execute("""
            create table games (
                id integer primary key,
                name text,
                console_model_id integer,
                release_year integer,
                status text
            )
        """)

        cursor.execute("""
            create table genres (
                id integer primary key,
                name text
            );
        """)

        cursor.execute("""
            create table game_genres (
                game_id integer,
                genre_id integer
            );
        """)
        self.connection.commit()

    def test_add_game_correctly(self):
        self.repo.add_game("Testgame", 1, 2026, "wishlist", [1, 2])

        # Haetaan pelejä
        games = self.repo.get_all_games()

        self.assertEqual(len(games), 1)
        game = games[0]

        self.assertEqual(game.name, "Testgame")
        self.assertEqual(game.console_model_id, 1)
        self.assertEqual(game.release_year, 2026)
        self.assertEqual(game.status, "wishlist")
        self.assertIsInstance(game, Game)

    def test_get_game_by_id(self):
        self.repo.add_game("Testgame", 1, 2026, "wishlist", [1, 2])
        game = self.repo.get_game_by_id(1)

        self.assertEqual(game.name, "Testgame")
        self.assertEqual(game.console_model_id, 1)
        self.assertEqual(game.release_year, 2026)
        self.assertEqual(game.status, "wishlist")
        self.assertIsInstance(game, Game)

    def test_get_game_by_id_returns_none_when_not_found(self):
        game = self.repo.get_game_by_id(999)
        self.assertIsNone(game)

    def test_get_game_by_status(self):
        self.repo.add_game("Testgame1", 1, 2026, "wishlist", [1, 2])
        self.repo.add_game("Testgame2", 2, 2025, "playing", [1, 2])

        wishlist_games = self.repo.get_game_by_status("wishlist")
        playing_games = self.repo.get_game_by_status("playing")

        self.assertEqual(len(wishlist_games), 1)
        self.assertEqual(len(playing_games), 1)
        self.assertEqual(wishlist_games[0].name, "Testgame1")
        self.assertEqual(playing_games[0].name, "Testgame2")

    def test_delete_game(self):
        self.repo.add_game("Testgame", 1, 2026, "wishlist", [1, 2])
        self.repo.delete_game(1)

        games = self.repo.get_all_games()
        self.assertEqual(len(games), 0)

    def test_get_genres_for_game(self):
        self.repo.add_game("Testgame", 1, 2026, "wishlist", [1, 2])

        genres = self.repo.get_genres_for_game(1)
        self.assertEqual(genres, [1, 2])

    def test_get_games_by_genre(self):
        self.repo.add_game("Testgame1", 1, 2026, "wishlist", [1, 2])
        self.repo.add_game("Testgame2", 2, 2025, "playing", [2, 3])

        games_genre_2 = self.repo.get_games_by_genre(2)
        games_genre_3 = self.repo.get_games_by_genre(3)

        self.assertEqual(len(games_genre_2), 2)
        self.assertEqual(len(games_genre_3), 1)
        self.assertEqual(games_genre_2[0].name, "Testgame1")
        self.assertEqual(games_genre_2[1].name, "Testgame2")
        self.assertEqual(games_genre_3[0].name, "Testgame2")

    def test_upddate_status(self):
        self.repo.add_game("Testgame", 1, 2026, "wishlist", [1, 2])
        self.repo.update_status(1, "playing")

        game = self.repo.get_game_by_id(1)
        self.assertEqual(game.status, "playing")
