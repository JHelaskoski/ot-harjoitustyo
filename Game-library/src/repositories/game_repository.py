from database_connection import get_database_connection

class GameRepository:
    def __init__(self):
        self._connection = get_database_connection()