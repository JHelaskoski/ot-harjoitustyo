import sqlite3
def get_database_connection():
    connection = sqlite3.connect('game_library.db')
    connection.row_factory = sqlite3.Row
    return connection
