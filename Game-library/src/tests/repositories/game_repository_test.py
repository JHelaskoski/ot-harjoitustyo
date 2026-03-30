import unittest
import sqlite3
from repositories.game_repository import GameRepository
from entities.game import Game

class TestGameRepository(unittest.TestCase):
    def setUp(self):
        #Luodaan testitietokanta muistiin
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        
        #Luodaan repositorio, joka käyttää testitietokantaa
        self.repo = GameRepository(self.connection)
        
        #Luodaan taulu testitietokantaan
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
        self.connection.commit()
        
        
    def test_add_game_correctly(self):
        self.repo.add_game("Testgame", 1, 2026, "wishlist")
        
        #Haetaan pelejä
        games = self.repo.get_all_games()
        
        self.assertEqual(len(games), 1)
        game = games[0]
        
        self.assertEqual(game.name, "Testgame")
        self.assertEqual(game.console_model_id, 1)
        self.assertEqual(game.release_year, 2026)
        self.assertEqual(game.status, "wishlist")
        self.assertIsInstance(game, Game)