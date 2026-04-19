from repositories.console_model_repository import ConsoleModelRepository
from database_connection import get_database_connection

class ConsoleModelService:
    def __init__(self, console_model_repository: ConsoleModelRepository):
        self._repo = console_model_repository

    def fetch_all_models(self):
        return self._repo.get_all_console_models()

    def get_model_by_id(self, model_id):
        return self._repo.get_console_model_by_id(model_id)

    def get_model_by_name(self, name):
        return self._repo.get_console_model_by_name(name)

    def get_models_by_console(self, console_id):
        return self._repo.get_console_models_by_console_id(console_id)

console_model_service = ConsoleModelService(
    ConsoleModelRepository(get_database_connection())
    )
