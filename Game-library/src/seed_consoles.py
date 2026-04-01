from repositories.console_repository import ConsoleRepository


def seed_consoles():
    repo = ConsoleRepository()

    # konsoliperheet/yläotsikot
    consoles = ["PlayStation", "Xbox", "Nintendo", "PC"]

    for name in consoles:
        repo.add_console(name)


if __name__ == "__main__":
    seed_consoles()
