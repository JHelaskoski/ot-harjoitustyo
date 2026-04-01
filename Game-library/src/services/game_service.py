from repositories.game_repository import GameRepository
from repositories.console_model_repository import ConsoleModelRepository


class GameService:
    Valid_statuses = ["wishlist", "playing", "completed"]

    def __init__(self, game_repo: GameRepository, console_model_repo: ConsoleModelRepository):
        self._game_repo = game_repo
        self._console_model_repo = console_model_repo

    def add_game(self, name: str, console_model_id: int, release_year: int):
        if not name:
            raise ValueError("Name cannot be empty.")

        if console_model_id <= 0:
            raise ValueError("Console model ID must be a positive number.")

        if release_year is not None and release_year < 0:
            raise ValueError("Release year must be empty or a positive number.")

        return self._game_repo.add_game(name, console_model_id, release_year)


    def get_all_games(self):
        return self._game_repo.get_all_games()

    def get_game_by_id(self, game_id: int):
        return self._game_repo.get_by_id(game_id)

    def get_games_by_status(self, status: str):
        if status not in self.Valid_statuses:
            raise ValueError("Invalid status.")
        return self._game_repo.get_by_status(status)

    def change_status(self, game_id: int, new_status: str):
        if new_status not in self.Valid_statuses:
            raise ValueError("Invalid status.")

        game = self._game_repo.get_by_id(game_id)
        if not game:
            raise ValueError("Game not found.")

        return self._game_repo.update_status(game_id, new_status)
