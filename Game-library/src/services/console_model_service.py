from repositories.console_model_repository import ConsoleModelRepository

class ConsoleModelService:
    def __init__(self, console_model_repository: ConsoleModelRepository):
        self._repo = console_model_repository

    def fetch_all_models(self):
        return self._repo.get_all_models()

    def get_model_by_id(self, model_id):
        return self._repo.get_model_by_id(model_id)

    def get_model_by_name(self, name):
        return self._repo.get_model_by_name(name)
