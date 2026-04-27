from repositories.console_model_repository import ConsoleModelRepository
from database_connection import get_database_connection

class ConsoleModelService:
    """Tarjoaa sovelluslogiikan konsolimallien hakemiseen.

    Tätä luokkaa käyttää käyttöliittymä, kun pelin lisäyksessä tai
    suodatuksessa tarvitaan tietyn konsolin mallit. Service välittää
    kutsut ConsoleModelRepositorylle.
    """

    def __init__(self, console_model_repository: ConsoleModelRepository):
        """Luokan konstruktori, joka tallentaa käytettävän repositorion.

        Args:
            console_model_repository: Olio, joka hoitaa konsolimallien
                tietokantakyselyt.
        """

        self._repo = console_model_repository

    def fetch_all_models(self):
        return self._repo.get_all_console_models()

    def get_model_by_id(self, model_id):
        """Hakee konsolimallin ID:n perusteella.

        Tätä käyttää käyttöliittymä, kun pelin lisäyksessä tarkistetaan
        tai näytetään valittu konsolimalli.

        Args:
            model_id: Konsolimallin tunniste.

        Returns:
            Konsolimallin tiedot sisältävä rivi tai None.
        """

        return self._repo.get_console_model_by_id(model_id)

    def get_model_by_name(self, name):
        return self._repo.get_console_model_by_name(name)

    def get_models_by_console(self, console_id):
        """Hakee kaikki konsolimallit tietylle konsolille.

        Tätä kutsuu käyttöliittymä, kun pelin lisäyksessä käyttäjä valitsee
        ensin konsolin ja sen jälkeen halutaan näyttää kyseisen konsolin mallit.

        Args:
            console_id: Konsolin tunniste.

        Returns:
            Lista tietokantarivejä konsolin malleista.
        """

        return self._repo.get_console_models_by_console_id(console_id)

console_model_service = ConsoleModelService(
    ConsoleModelRepository(get_database_connection())
    )
