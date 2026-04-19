from repositories.console_repository import ConsoleRepository
from repositories.console_model_repository import ConsoleModelRepository
from database_connection import get_database_connection


def seed_console_models():
    console_repo = ConsoleRepository(get_database_connection())
    model_repo = ConsoleModelRepository(get_database_connection())

    consoles = console_repo.get_all_consoles()

    # Sanakirja konsoliperheiden ja niiden alatyyppien osalta.
    console_ids = {console["name"]: console["id"] for console in consoles}

    playstation_models = [
        "PS1",
        "PS2",
        "PS3",
        "PS4",
        "PS5"
    ]

    xbox_models = [
        "Xbox",
        "Xbox 360",
        "Xbox One",
        "Xbox Series X"
    ]

    nintendo_models = [
        "Switch",
        "Switch 2",
        "Nintendo Wii",
        "Nintendo GameCube",
        "Nintendo 64",
        "Nintendo DS"
    ]
    pc_models = [
        "PC"
    ]

    for model in playstation_models:
        model_repo.add_console_model(console_ids["PlayStation"], model)

    for model in xbox_models:
        model_repo.add_console_model(console_ids["Xbox"], model)

    for model in nintendo_models:
        model_repo.add_console_model(console_ids["Nintendo"], model)

    for model in pc_models:
        model_repo.add_console_model(console_ids["PC"], model)


if __name__ == "__main__":
    seed_console_models()
