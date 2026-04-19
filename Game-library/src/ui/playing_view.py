from tkinter import Frame, Label, Button
from services.game_service import game_service

class PlayingView(Frame):
    def __init__(self, root, open_main_menu):
        super().__init__(root)
        self.root = root
        self.open_main_menu = open_main_menu

        Label(self, text="Playing Now", font=("Arial", 18)).pack(pady=10)

        games = game_service.get_game_by_status("playing")
        for game in games:
            Label(self, text=f"{game.name} ({game.release_year})").pack()

        Button(self, text="Back", command=self.open_main_menu).pack(pady=10)
