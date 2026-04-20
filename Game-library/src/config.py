import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_FILENAME = "game_library.db"
DATABASE_FILE_PATH = os.path.join(BASE_DIR, "..", "data", DATABASE_FILENAME)
