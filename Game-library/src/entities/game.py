class Game:
    def __init__(self, name, release_year, status, console_model_id, id=None):
        self.id = id
        self.name = name
        self.release_year = release_year
        self.status = status
        self.console_model_id = console_model_id
