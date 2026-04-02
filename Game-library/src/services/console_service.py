from repositories.console_repository import ConsoleRepository

class ConsoleService:

    def __init__(self, console_repository: ConsoleRepository):
        self._console_repository = console_repository

    def add_console(self, name):
        self._console_repository.add_console(name)

    def get_all_consoles(self):
        return self._console_repository.get_all_consoles()
