class Game:
    def __init__(self, name, console_model_id, release_year, status, id=None):
        self.id = id
        self.name = name
        self.console_model_id = console_model_id
        self.release_year = release_year
        self.status = status
