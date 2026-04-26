# Ohjelmistotekniikka, harjoitustyö - GameLibrary
---
Sovellus tarjoaa käyttäjille mahdollisuuden hallita omaa pelikirjastoaan.
Käyttäjä voi lisätä pelejä, selata niitä eri statuksen mukaan (toivelista, pelaan tällä hetkellä, pelatut), hakea pelejä, arvostella pelatut pelit sekä poistaa pelejä tai vaihtaa pelin statusta.

## Huomio Python-versiosta
---
Sovelluksen toiminta on testattu Python-versiolla 3.12.
Uudemmilla versioilla voi aiheuttaa virheen. Tarv. lataa sopiva Python-versio.

## Dokumentaatio
---
* [Käyttöohje](Game-library/dokumentaatio/kayttoohje.md)
* [Arkkitehtuuri](Game-library/dokumentaatio/arkkitehtuuri.md)
* [Changelog](Game-library/dokumentaatio/changelog.md)
* [Testaus](Game-library/dokumentaatio/testaus.md)
* [Työaikakirjanpito](Game-library/dokumentaatio/tyoaikakirjanpito.md)
* [Vaatimusmäärittely](Game-library/dokumentaatio/vaatimusmaarittely.md)

## Asennus
---

1. Asenna riippuvuudet komennolla:
```poetry install```

2. Alusta tietokanta komennolla:
```poetry run invoke build```

3. Käynnistä sovellus:
```poetry run invoke start```

## Komentorivitoiminnot
---

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:
```poetry run invoke start```

### Testaus

Testit suoritetaan komennolla:
```poetry run invoke test```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
```poetry run invoke coverage-report```

Raportti generoituu htmlcov‑hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```poetry run invoke lint```
