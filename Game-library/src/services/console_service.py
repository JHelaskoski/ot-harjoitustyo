from repositories.console_repository import ConsoleRepository
from database_connection import get_database_connection

class ConsoleService:
    """Tarjoaa sovelluslogiikan konsoliperheiden hakemiseen.
       Service välittää kutsut ConsoleRepositorylle.
    """

    def __init__(self, console_repo):
        """Luokan konstruktori, joka tallentaa käytettävän repositorion.

        Args:
            console_repo: Olio, joka hoitaa konsolien tietokantakyselyt.
        """

        self._repo = console_repo

    def get_all_consoles(self):
        """Hakee kaikki konsoliperheet.

        Tätä kutsuu käyttöliittymä, kun pelin lisäyksessä näytetään
        käyttäjälle valittavissa olevat konsolit.

        Returns:
            Lista tietokantarivejä, joissa konsolien id ja nimi.
        """

        return self._repo.get_all_consoles()

    def get_console_by_id(self, console_id):
        return self._repo.get_console_by_id(console_id)

    def get_console_by_name(self, name):
        return self._repo.get_console_by_name(name)

console_repository = ConsoleRepository(get_database_connection())
console_service = ConsoleService(console_repository)
