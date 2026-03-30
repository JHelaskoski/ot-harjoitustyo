from repositories.game_repository import GameRepository

class GameService:
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository
        
    def add_game(self, name: str, console_model_id: int, release_year: int, status: str):
        if not name:
            raise ValueError("Name cannot be empty.")
        
        if console_model_id <= 0:
            raise ValueError("Console model ID must be a positive number.")
        
        if release_year is not None:
            if release_year < 0:
                raise ValueError("Release year must be empty or a non-negative number.")
        
        #Tallennetaan peli tietokantaan
        return self.game_repository.add_game(
            name, console_model_id, release_year, status
        )

    def get_all_games(self):
        return self._game_repository.get_all_games()