from repositories.game_repository import GameRepository
from repositories.console_model_repository import ConsoleModelRepository
from repositories.genre_repository import GenreRepository
from database_connection import get_database_connection

class GameService:
    """Tarjoaa sovelluslogiikan pelien lisäämiseen, hakemiseen ja poistamiseen.

    Tätä luokkaa käyttää käyttöliittymä. Service varmistaa käyttäjän syötteet
    ja välittää kutsut GameRepositorylle, ConsoleModelRepositorylle ja
    GenreRepositorylle.
    """

    Valid_statuses = ["wishlist", "playing", "completed"]

    def __init__(self, game_repo: GameRepository,
                console_model_repo: ConsoleModelRepository,
                genre_repo: GenreRepository):
        """Luokan konstruktori, joka tallentaa käytettävät repositoriot.

        Args:
            game_repo: Olio, joka hoitaa pelien tietokantakyselyt.
            console_model_repo: Olio, joka hakee konsolimallit.
            genre_repo: Olio, joka hakee genret.
        """

        self._game_repo = game_repo
        self._console_model_repo = console_model_repo
        self._genre_repo = genre_repo

    def add_game(self, name, console_model_id, release_year, status, genre_ids):
        """Lisää uuden pelin.

        Args:
            name: Pelin nimi.
            console_model_id: Valitun konsolimallin ID.
            release_year: Pelin julkaisuvuosi.
            status: Pelin tila (wishlist, playing, completed).
            genre_ids: Lista valittujen genrejen ID-arvoja.

        Returns:
            Uuden pelin tietokanta-ID.

        Raises:
            ValueError: Jos jokin syöte on virheellinen.
        """

        if not name:
            raise ValueError("Name cannot be empty.")

        if console_model_id <= 0:
            raise ValueError("Console model ID must be a positive number.")

        if release_year is not None:
            year_str = str(release_year)

            if len(year_str) != 4:
                raise ValueError("Release year must be a 4-digit year.")

            if release_year < 1900 or release_year > 2100:
                raise ValueError("Release year must be between 1900 and 2100.")

        for genre_id in genre_ids:
            if not self._genre_repo.get_genre_by_id(genre_id):
                raise ValueError(f"Genre ID {genre_id} is not valid.")

        if status not in self.Valid_statuses:
            raise ValueError("Invalid status.")

        return self._game_repo.add_game(
            name=name,
            console_model_id=console_model_id,
            release_year=release_year,
            status=status,
            genre_ids=genre_ids
        )

    def get_all_games(self):
        """Hakee kaikki pelit.

        Tätä kutsuu käyttöliittymän kirjastonäkymät.

        Returns:
            Lista Game-olioita.
        """

        return self._game_repo.get_all_games()

    def get_game_by_id(self, game_id: int):
        return self._game_repo.get_game_by_id(game_id)

    def get_game_by_status(self, status: str):
        if status not in self.Valid_statuses:
            raise ValueError("Invalid status.")
        return self._game_repo.get_game_by_status(status)

    def change_status(self, game_id: int, new_status: str):
        if new_status not in self.Valid_statuses:
            raise ValueError("Invalid status.")

        game = self._game_repo.get_game_by_id(game_id)
        if not game:
            raise ValueError("Game not found.")

        return self._game_repo.update_status(game_id, new_status)

    def delete_game(self, game_id: int):
        """Poistaa pelin.

        Args:
            game_id: Poistettavan pelin tunniste.

        Raises:
            ValueError: Jos peliä ei löydy.
        """

        game = self._game_repo.get_game_by_id(game_id)
        if not game:
            raise ValueError("Game not found.")

        return self._game_repo.delete_game(game_id)

    def get_genres_for_game(self, game_id: int):
        return self._game_repo.get_genres_for_game(game_id)

    def get_games_by_genre(self, genre_id):
        if not self._genre_repo.get_genre_by_id(genre_id):
            raise ValueError(" Invalid genre ID.")
        return self._game_repo.get_games_by_genre(genre_id)

    def add_ratings(self, game_id: int, story: int, graphics: int, gameplay: int, overall: int):
        """Lisää pelin arvostelut.

        Tätä kutsuu käyttöliittymä, kun käyttäjä tallentaa pelin arviot.

        Args:
            game_id: Pelin tunniste.
            story: Tarinan arvosana (0–10).
            graphics: Grafiikan arvosana (0–10).
            gameplay: Pelattavuuden arvosana (0–10).
            overall: Kokonaisarvosana (0–10).

        Raises:
            ValueError: Jos peliä ei löydy tai arvosanat ovat virheellisiä.
        """

        game = self._game_repo.get_game_by_id(game_id)
        if not game:
            raise ValueError("Game not found.")

        for value in [story, graphics, gameplay, overall]:
            if not isinstance(value, int) or value < 0 or value > 10:
                raise ValueError("Ratings must be integers between 0 and 10.")

        return self._game_repo.update_ratings(
            game_id=game_id,
            story=story,
            graphics=graphics,
            gameplay=gameplay,
            overall=overall
        )

    def search_games(self, query=None, genre_id=None, console_id=None):
        """Hakee pelejä nimen, genren tai konsolin perusteella.

        Args:
            query: Hakusana.
            genre_id: Genren tunniste.
            console_id: Konsolin tunniste.

        Returns:
            Lista pelejä sanakirjoina.
        """

        # haku nimen perusteella
        if query:
            return self._game_repo.search_by_name(query)

        # haku genren perusteella
        if genre_id:
            return self._game_repo.get_games_by_genre(genre_id)

        # haku konsolin perusteella
        if console_id:
            return self._game_repo.get_games_by_console(console_id)

        return []

    def get_top_rated_games(self):
        return self._game_repo.get_top_rated_games()

_connection = get_database_connection()
_game_repo = GameRepository(_connection)
_console_model_repo = ConsoleModelRepository(_connection)
_genre_repo = GenreRepository(_connection)

game_service = GameService(_game_repo, _console_model_repo, _genre_repo)
