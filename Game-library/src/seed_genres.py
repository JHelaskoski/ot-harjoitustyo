from repositories.genre_repository import GenreRepository

repo = GenreRepository()

genres = [
    "Action",
    "Adventure",
    "RPG",
    "Strategy",
    "Simulation",
    "Sports",
    "Puzzle",
    "Horror",
    "Racing",
    "Fighting",
    "Co-op",
    "Open World",
    "Cozy"
]

# Lisätään genret tietokantaan.
for name in genres:
    repo.add_genre(name)