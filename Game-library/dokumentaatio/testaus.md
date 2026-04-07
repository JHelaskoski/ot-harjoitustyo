# Testausdokumentti
---
Sovellusta on testattu sekä automatisoiduin unittest‑pohjaisia yksikkö- ja integraatiotesteillä että käyttöliittymän kautta tehdyillä manuaalisilla kokeiluilla.

## Yksikkö- ja integraatiotestaus
---
### Sovelluslogiikka

Sovelluslogiikan toiminnallisuutta testataan erillisillä testiluokilla, joissa jokaiselle palveluluokalle (GameService, ConsoleService, ConsoleModelService, GenreService) on oma testitiedostonsa. Testeissä palveluluokille annetaan käyttöön “fake”‑repositoryt, jotka tallentavat tiedot muistiin tietokannan sijaan. Näin voidaan varmistaa, että palveluluokkien logiikka toimii oikein ilman riippuvuutta tietokantakerrokseen. Testit kattavat mm. pelien lisäämisen, hakemisen, tilan muuttamisen ja poistamisen.

### Repositorio-luokat

Repositorio‑luokkia (GameRepository, ConsoleRepository, ConsoleModelRepository, GenreRepository) testataan erillisillä testitiedostoilla käyttäen erillistä testitietokantaa. Testeissä tietokanta alustetaan aina muistiin, ja taulut luodaan ennen jokaista testiä. Testit varmistavat, että tietojen tallennus, haku, poistaminen ja liitostaulujen käsittely toimivat oikein. Jokaiselle repositoriolle on oma testiluokkansa, jossa testataan sen keskeiset toiminnot.

(Jatkuu, kun ohjelmisto vielä täydentyy)
