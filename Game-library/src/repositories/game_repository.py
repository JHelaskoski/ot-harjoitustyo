from entities.game import Game


class GameRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_game(self, name, console_model_id, release_year, status, genre_ids):
        cursor = self._connection.cursor()

        #Lisätään ensin pelkkä peli games-tauluun
        cursor.execute("""
            insert into games (name, console_model_id, release_year, status)
            values (?, ?, ?, ?)
        """, (name, console_model_id, release_year, status))

        game_id = cursor.lastrowid

        # Sit lisätään genre game-genres tauluun
        for genre_id in genre_ids:
            cursor.execute("""
                insert into game_genres (game_id, genre_id)
                values (?, ?)
            """, (game_id, genre_id))

        self._connection.commit()

    def get_all_games(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            select * from games
        """)
        rows = cursor.fetchall()
        return [
            Game(
                row["name"],
                row["console_model_id"],
                row["release_year"],
                row["status"],
                row["id"]
            )
            for row in rows
        ]

    def get_game_by_id(self, game_id):
        cursor = self._connection.cursor()
        cursor.execute("""
            select * from games where id = ?
        """, (game_id,))
        row = cursor.fetchone()
        if row:
            return Game(
                row["name"],
                row["console_model_id"],
                row["release_year"],
                row["status"],
                row["id"]
            )

        return None

    def get_game_by_status(self, status):
        cursor = self._connection.cursor()
        cursor.execute("""
            select * from games where status = ?
        """, (status,))
        rows = cursor.fetchall()
        return [
            Game(
                row["name"],
                row["console_model_id"],
                row["release_year"],
                row["status"],
                row["id"]
            )
            for row in rows
        ]

    def delete_game(self, game_id):
        cursor = self._connection.cursor()
        cursor.execute("""
            delete from games where id = ?
        """, (game_id,))
        self._connection.commit()

    def get_genres_for_game(self, game_id):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT genre_id FROM game_genres WHERE game_id = ?
        """, (game_id,))
        rows = cursor.fetchall()
        return [row["genre_id"] for row in rows]

    def get_games_by_genre(self, genre_id):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT g.*
            FROM games g
            JOIN game_genres gg ON g.id = gg.game_id
            WHERE gg.genre_id = ?
        """, (genre_id,))
        rows = cursor.fetchall()
        return [
            Game(
                row["name"],
                row["console_model_id"],
                row["release_year"],
                row["status"],
                row["id"]
            )
            for row in rows
        ]

    def update_status(self, game_id, new_status):
        cursor = self._connection.cursor()
        cursor.execute("""
            update games set status = ? where id = ?
        """, (new_status, game_id))
        self._connection.commit()
