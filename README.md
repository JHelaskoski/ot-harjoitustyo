# Ohjelmistotekniikka, harjoitustyö - GameLibrary
---
Sovellus tarjoaa käyttäjille mahdollisuuden lisätä uusia pelejä omaan pelikirjastoonsa sekä tallentaa ne tietokantaan.

## Dokumentaatio
---
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
```poetryrun invoke start```

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
```poetry run invokecoverage-report```

Raportti generoituu htmlcov‑hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```poetry run invoke lint```
