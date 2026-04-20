from initialize_database import initialize_database
from seed_genres import seed_genres
from seed_consoles import seed_consoles
from seed_console_model import seed_console_models

def build():
    initialize_database()
    seed_genres()
    seed_consoles()
    seed_console_models()

if __name__ == "__main__":
    build()
