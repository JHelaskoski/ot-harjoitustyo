from repositories.genre_repository import GenreRepository

class GenreService:
    def __init__(self, genre_repository: GenreRepository):
        self._genre_repository = genre_repository

    def fetch_all_genres(self):
        return self._genre_repository.get_all_genres()

    def get_genre_by_name(self, name):
        return self._genre_repository.get_genre_by_name(name)

    def get_genre_by_id(self, genre_id):
        return self._genre_repository.get_genre_by_id(genre_id)
