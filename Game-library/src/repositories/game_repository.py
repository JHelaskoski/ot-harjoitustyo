from entities.game import Game

class GameRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_game(self, name, console_model_id, release_year, status, genre_ids):
        cursor = self._connection.cursor()

        cursor.execute("""
            insert into games (name, console_model_id, release_year, status)
            values (?, ?, ?, ?)
        """, (name, console_model_id, release_year, status))

        game_id = cursor.lastrowid

        for genre_id in genre_ids:
            cursor.execute("""
                insert into game_genres (game_id, genre_id)
                values (?, ?)
            """, (game_id, genre_id))

        self._connection.commit()
        return game_id

    def _row_to_game(self, row):
        return Game(
            row["name"],
            row["console_model_id"],
            row["release_year"],
            row["status"],
            row["id"],
            row["story_rating"],
            row["graphics_rating"],
            row["gameplay_rating"],
            row["overall_rating"]
        )

    def get_all_games(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from games")
        rows = cursor.fetchall()
        return [self._row_to_game(row) for row in rows]

    def get_game_by_id(self, game_id):
        cursor = self._connection.cursor()
        cursor.execute("select * from games where id = ?", (game_id,))
        row = cursor.fetchone()
        return self._row_to_game(row) if row else None

    def get_game_by_status(self, status):
        cursor = self._connection.cursor()
        cursor.execute("select * from games where status = ?", (status,))
        rows = cursor.fetchall()
        return [self._row_to_game(row) for row in rows]

    def delete_game(self, game_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM game_genres WHERE game_id = ?", (game_id,))
        cursor.execute("delete from games where id = ?", (game_id,))
        self._connection.commit()

    def get_genres_for_game(self, game_id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT genre_id FROM game_genres WHERE game_id = ?", (game_id,))
        rows = cursor.fetchall()
        return [row["genre_id"] for row in rows]

    def get_games_by_genre(self, genre_id):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT games.*
            FROM games
            JOIN game_genres ON games.id = game_genres.game_id
            WHERE game_genres.genre_id = ?
        """, (genre_id,))
        rows = cursor.fetchall()
        return [self._row_to_game(row) for row in rows]

    def update_status(self, game_id, new_status):
        cursor = self._connection.cursor()
        cursor.execute("""
            update games set status = ? where id = ?
        """, (new_status, game_id))
        self._connection.commit()

    def update_ratings(self, game_id, story, graphics, gameplay, overall):
        cursor = self._connection.cursor()
        cursor.execute("""
            update games
            set story_rating = ?, graphics_rating = ?, gameplay_rating = ?, overall_rating = ?
            where id = ?
        """, (story, graphics, gameplay, overall, game_id))
        self._connection.commit()

    def search_by_name(self, query):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM games WHERE name LIKE ?",
            (f"%{query}%",)
        )
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def get_games_by_console(self, console_id):
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT * FROM games
            WHERE console_model_id IN (
                SELECT id FROM console_models WHERE console_id = ?
            )
        """, (console_id,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def get_top_rated_games(self, limit=3):
        '''lasketaan arvostelu pisteet
        ja näytetään käyttäjälle 3-parasta arvostelemaa peliä'''

        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT
                *,
                (story_rating + graphics_rating + gameplay_rating + overall_rating) AS total_score
            FROM games
            WHERE story_rating IS NOT NULL
            AND graphics_rating IS NOT NULL
            AND gameplay_rating IS NOT NULL
            AND overall_rating IS NOT NULL
            ORDER BY total_score DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()

        games = []
        for row in rows:
            game = self._row_to_game(row)
            game.total_score = row["total_score"]
            games.append(game)

        return games
