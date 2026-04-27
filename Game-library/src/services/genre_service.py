from repositories.genre_repository import GenreRepository
from database_connection import get_database_connection

class GenreService:
    """Tarjoaa sovelluslogiikan genrejen hakemiseen.
    """

    def __init__(self, genre_repository: GenreRepository):
        """Luokan konstruktori, joka tallentaa käytettävän repositorion.

        Args:
            genre_repository: Olio, joka hoitaa genreihin liittyvät
                tietokantakyselyt.
        """

        self._genre_repository = genre_repository

    def get_all_genres(self):
        """Hakee kaikki genret.

        Tätä kutsuu käyttöliittymä, kun pelin lisäyksessä näytetään
        käyttäjälle valittavissa olevat genret.

        Returns:
            Lista tietokantarivejä kaikista genreistä.
        """

        return self._genre_repository.get_all_genres()

    def get_genre_by_name(self, name):
        return self._genre_repository.get_genre_by_name(name)

    def get_genre_by_id(self, genre_id):
        return self._genre_repository.get_genre_by_id(genre_id)

_default_genre_repository = GenreRepository(get_database_connection())
genre_service = GenreService(_default_genre_repository)
