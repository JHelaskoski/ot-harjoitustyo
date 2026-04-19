from tkinter import Frame, Label, Button
from services.game_service import game_service

class PlayedView(Frame):
    def __init__(self, root, open_main_menu, open_rate_game):
        super().__init__(root)
        self.root = root
        self.open_main_menu = open_main_menu
        self.open_rate_game = open_rate_game

        Label(self, text="Played Games", font=("Arial", 18)).pack(pady=10)

        self.refresh_list()

        Button(self, text="Back", command=self.open_main_menu).pack(pady=10)

    def refresh_list(self):
        games = game_service.get_game_by_status("completed")

        for game in games:
            frame = Frame(self)
            frame.pack(pady=5)

            Label(frame, text=f"{game.name} ({game.release_year})").pack()

            # Arvosanat
            if game.overall_rating is not None:
                Label(frame, text=f"Story: {game.story_rating}").pack()
                Label(frame, text=f"Graphics: {game.graphics_rating}").pack()
                Label(frame, text=f"Gameplay: {game.gameplay_rating}").pack()
                Label(frame, text=f"Overall: {game.overall_rating}").pack()
            else:
                Label(frame, text="Not rated yet").pack()
                Button(frame, text="Rate", command=lambda g=game: self.open_rate_game(g.id)).pack()
