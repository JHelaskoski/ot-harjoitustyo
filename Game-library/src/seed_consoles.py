from repositories.console_repository import ConsoleRepository
from database_connection import get_database_connection


def seed_consoles():
    repo = ConsoleRepository(get_database_connection())

    # konsoliperheet/yläotsikot
    consoles = ["PlayStation", "Xbox", "Nintendo", "PC"]

    for name in consoles:
        repo.add_console(name)


if __name__ == "__main__":
    seed_consoles()
