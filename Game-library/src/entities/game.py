class Game:
    def __init__(self, name, console_model_id, release_year, status,
                 game_id=None, story_rating=None, graphics_rating=None,
                 gameplay_rating=None, overall_rating=None):

        self.game_id = game_id
        self.name = name
        self.console_model_id = console_model_id
        self.release_year = release_year
        self.status = status

        self.story_rating = story_rating
        self.graphics_rating = graphics_rating
        self.gameplay_rating = gameplay_rating
        self.overall_rating = overall_rating
