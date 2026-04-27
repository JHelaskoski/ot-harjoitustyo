from entities.game import Game

class GameRepository:
    """Tallentaa ja hakee pelejä tietokannasta.

    Tätä luokkaa käyttävät GameService ja käyttöliittymä, kun pelejä lisätään,
    haetaan, suodatetaan tai poistetaan.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka tallentaa tietokantayhteyden.

        Args:
            connection: SQLite-yhteys, jota käytetään kyselyihin.
        """

        self._connection = connection

    def add_game(self, name, console_model_id, release_year, status, genre_ids):
        """Lisää uuden pelin ja sen tiedot tietokantaan

        Args:
            name: Pelin nimi.
            console_model_id: Konsolimallin tunniste.
            release_year: Pelin julkaisuvuosi.
            status: Pelin tila (wishlist, playing, completed).
            genre_ids: Lista valittujen genrejen ID-arvoja.

        Returns:
            Uuden pelin tietokanta-ID.
        """

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
        """Muuntaa tietokantarivin Game-olioksi.

        Tätä käytetään sisäisesti, kun pelejä haetaan listana tai yksittäisenä.

        Args:
            row: Tietokantarivi, jossa pelin tiedot.
        """

        return Game(
            name=row["name"],
            console_model_id=row["console_model_id"],
            release_year=row["release_year"],
            status=row["status"],
            game_id=row["id"],
            story_rating=row["story_rating"],
            graphics_rating=row["graphics_rating"],
            gameplay_rating=row["gameplay_rating"],
            overall_rating=row["overall_rating"]
        )

    def get_all_games(self):
        """Palauttaa kaikki käyttäjän lisäämät pelit. Käytetään kirjastonäkymässä"""

        cursor = self._connection.cursor()
        cursor.execute("select * from games")
        rows = cursor.fetchall()
        return [self._row_to_game(row) for row in rows]

    def get_game_by_id(self, game_id):
        """Hakee yhden pelin ID:n perusteella. Käytetään palvelukerroksessa pelin tarkasteluun.

        Args:
            game_id: Haettavan pelin tunniste.

        Returns:
            Game-olio tai None, jos peliä ei löydy.
        """

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
        """Hakee kaikki pelit, joilla on tietty genre.

        Tätä käyttää hakunäkymä, kun käyttäjä suodattaa pelejä genren perusteella.

        Args:
            genre_id: Genren tunniste.
        """

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
