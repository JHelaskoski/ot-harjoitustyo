from repositories.game_repository import GameRepository
from repositories.console_model_repository import ConsoleModelRepository
from repositories.genre_repository import GenreRepository
from database_connection import get_database_connection

class GameService:
    Valid_statuses = ["wishlist", "playing", "completed"]

    def __init__(self, game_repo: GameRepository, console_model_repo: ConsoleModelRepository,genre_repo: GenreRepository):
        self._game_repo = game_repo
        self._console_model_repo = console_model_repo
        self._genre_repo = genre_repo

    def add_game(self, name: str, console_model_id: int, release_year: int, genre_ids: list):
        if not name:
            raise ValueError("Name cannot be empty.")

        if console_model_id <= 0:
            raise ValueError("Console model ID must be a positive number.")

        if release_year is not None and release_year < 0:
            raise ValueError("Release year must be empty or a positive number.")

        for genre_id in genre_ids:
            if not self._genre_repo.get_genre_by_id(genre_id):
                raise ValueError(f"Genre ID {genre_id} is not valid.")

        return self._game_repo.add_game(
            name,
            console_model_id,
            release_year,
            "wishlist",
            genre_ids)

    def get_all_games(self):
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
        game = self._game_repo.get_game_by_id(game_id)
        if not game:
            raise ValueError("Game not found.")

        for value in [story, graphics, gameplay, overall]:
            if not isinstance(value, int) or value < 0 or value > 10:
                raise ValueError("Ratings must be integers between 0 and 10.")

        return self._game_repo.update_ratings(
            game_id, story, graphics, gameplay, overall
    )

_connection = get_database_connection()
_game_repo = GameRepository(_connection)
_console_model_repo = ConsoleModelRepository(_connection)
_genre_repo = GenreRepository(_connection)

game_service = GameService(_game_repo, _console_model_repo, _genre_repo)
