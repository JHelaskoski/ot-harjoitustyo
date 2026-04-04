from repositories.console_repository import ConsoleRepository

class ConsoleService:
    def __init__(self, console_repo):
        self._repo = console_repo

    def get_all_consoles(self):
        return self._repo.get_all_consoles()

    def get_console_by_id(self, console_id):
        return self._repo.get_console_by_id(console_id)

    def get_console_by_name(self, name):
        return self._repo.get_console_by_name(name)
