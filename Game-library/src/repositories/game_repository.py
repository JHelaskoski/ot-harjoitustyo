from database_connection import get_database_connection

class GameRepository:
    def __init__(self):
        self._connection = get_database_connection()
        
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
        return cursor.fetchall()
    