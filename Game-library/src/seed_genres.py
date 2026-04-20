from repositories.genre_repository import GenreRepository
from database_connection import get_database_connection

def seed_genres():
    repo = GenreRepository(get_database_connection())

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

if __name__ == "__main__":
    seed_genres()
