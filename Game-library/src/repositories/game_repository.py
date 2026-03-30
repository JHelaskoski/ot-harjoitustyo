from entities.game import Game

class GameRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def add_game(self, name, console_model_id, release_year, status):
        cursor = self._connection.cursor()
        cursor.execute("""
            insert into games (name, console_model_id, release_year, status) 
            values (?, ?, ?, ?)
        """, (name, console_model_id, release_year, status))
        self._connection.commit()
        
    def get_all_games(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            select * from games
        """)
        rows = cursor.fetchall()
        return [Game(row["name"], row["release_year"], row["status"], row["console_model_id"]) for row in rows]
    