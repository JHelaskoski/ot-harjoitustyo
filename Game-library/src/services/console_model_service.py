from repositories.console_model_repository import ConsoleModelRepository

class ConsoleModelService:
    def __init__(self, console_model_repository: ConsoleModelRepository):
        self._console_model_repository = console_model_repository

    def add_console_model(self, console_id, name):
        self._console_model_repository.add_console_model(console_id, name)

    def get_console_models_by_console_id(self, console_id):
        return self._console_model_repository.get_console_models_by_console_id(console_id)

    def get_all_console_models(self):
        return self._console_model_repository.get_all_console_models()
