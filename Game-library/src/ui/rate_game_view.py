from tkinter import Frame, Label, Button, Entry
from services.game_service import game_service

class RateGameView(Frame):
    def __init__(self, root, game_id, go_back):
        super().__init__(root)
        self.game_id = game_id
        self.go_back = go_back

        Label(self, text="Rate the Game", font=("Arial", 18)).pack(pady=10)

        # Tarina
        Label(self, text="Story (0–10):").pack()
        self.story_entry = Entry(self)
        self.story_entry.pack()

        # Visuaalisuus
        Label(self, text="Graphics (0–10):").pack()
        self.graphics_entry = Entry(self)
        self.graphics_entry.pack()

        # Pelattavuus
        Label(self, text="Gameplay (0–10):").pack()
        self.gameplay_entry = Entry(self)
        self.gameplay_entry.pack()

        # Yleisarvosana
        Label(self, text="Overall (0–10):").pack()
        self.overall_entry = Entry(self)
        self.overall_entry.pack()

        Button(self, text="Save Rating", command=self.save_rating).pack(pady=10)
        Button(self, text="Back", command=self.go_back).pack()

    def save_rating(self):
        try:
            story = int(self.story_entry.get())
            graphics = int(self.graphics_entry.get())
            gameplay = int(self.gameplay_entry.get())
            overall = int(self.overall_entry.get())

            for value in [story, graphics, gameplay, overall]:
                if value < 0 or value > 10:
                    raise ValueError

            game_service.add_ratings(
                self.game_id, story, graphics, gameplay, overall
            )

            self.go_back()

        except ValueError:
            print("Invalid rating. Please enter numbers 0–10.")
