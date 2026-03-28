from database_connection import get_database_connection


class GenreRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def add_genre(self, name):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into genres (name) values (?)",
            (name,) 
        )
        self._connection.commit()
        
    def get_all_genres(self):
        # Hae kaikki genret listana.
        cursor = self._connection.cursor()
        cursor.execute("select * from genres")
        rows = cursor.fetchall()
        return rows
        
    def get_genre_by_name(self, name):
        # Hakee yhden genren nimen perusteella.
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from genres where name = ?",
            (name,)
        )
        return cursor.fetchone()
    
    def get_genre_by_id(self, genre_id):
        # Hakee yhden genren id:n perusteella.
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from genres where id = ?",
            (genre_id,)
        )
        return cursor.fetchone()
    
    