class Game:
    """Peli-olio, joka sisältää pelin perustiedot ja mahdolliset arvostelut.

    Attributes:
        game_id: Pelin tietokanta-ID. None, jos peliä ei ole vielä tallennettu.
        name: Pelin nimi.
        console_model_id: Konsolimallin tunniste, johon peli kuuluu.
        release_year: Pelin julkaisuvuosi. Voi olla None, jos ei tiedossa.
        status: Pelin tila (wishlist, playing, completed).

        story_rating: Tarinan arvosana (0–10) tai None, jos ei asetettu.
        graphics_rating: Grafiikan arvosana (0–10) tai None.
        gameplay_rating: Pelattavuuden arvosana (0–10) tai None.
        overall_rating: Kokonaisarvosana (0–10) tai None.
    """

    def __init__(self, name, console_model_id, release_year, status,
                 game_id=None, story_rating=None, graphics_rating=None,
                 gameplay_rating=None, overall_rating=None):
        """Luokan konstruktori, joka luo uuden peli-olion.

        Args:
            name: Pelin nimi.
            console_model_id: Konsolimallin tunniste.
            release_year: Pelin julkaisuvuosi tai None.
            status: Pelin tila (wishlist, playing, completed).
            game_id: Pelin tietokanta-ID. Oletuksena None.
            story_rating: Tarinan arvosana tai None.
            graphics_rating: Grafiikan arvosana tai None.
            gameplay_rating: Pelattavuuden arvosana tai None.
            overall_rating: Kokonaisarvosana tai None.
        """

        self.game_id = game_id
        self.name = name
        self.console_model_id = console_model_id
        self.release_year = release_year
        self.status = status

        self.story_rating = story_rating
        self.graphics_rating = graphics_rating
        self.gameplay_rating = gameplay_rating
        self.overall_rating = overall_rating
