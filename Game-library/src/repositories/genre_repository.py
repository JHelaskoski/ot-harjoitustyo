class GenreRepository:
    """Hakee genret tietokannasta.
    Tätä luokkaa käyttävät GameService ja käyttöliittymä, kun pelin lisäyksessä
    tai suodatuksessa tarvitaan lista genreistä.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka tallentaa tietokantayhteyden.

            Args:
                connection: SQLite-yhteys, jota käytetään kyselyihin.
        """

        self._connection = connection

    def add_genre(self, name):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into genres (name) values (?)",
            (name,)
        )
        self._connection.commit()

    def get_all_genres(self):
        """Palauttaa kaikki genret.


        Tätä kutsuu UI:n pelin lisäysnäkymä, joka näyttää käyttäjälle
        valittavissa olevat genret listana

        Returns:
            Lista genre-rivejä tietokannasta.
        """

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
        """Hakee genren ID:n perusteella.

        Tätä kutsuu GameRepository, kun peliä lisätessä liitetään oikeat
        genre_id:t pelin ja genrien väliseen liitostauluun.

        Args:
            genre_id: Genren tunniste.

        Returns:
            Yksi genrerivi tai None, jos ei löydy.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from genres where id = ?",
            (genre_id,)
        )
        return cursor.fetchone()
