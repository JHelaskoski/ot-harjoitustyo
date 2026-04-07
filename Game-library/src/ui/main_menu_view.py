from tkinter import Frame, Label, Button

class MainMenuView(Frame):
    def __init__(self, root, open_add_game, open_wish, open_playing, open_played, open_search):
        super().__init__(root)

        Label(self, text="Game Library", font=("Arial", 20)).pack(pady=20)

        Button(self, text="Add Game", width=20, command=open_add_game).pack(pady=5)
        Button(self, text="Wishes", width=20, command=open_wish).pack(pady=5)
        Button(self, text="In Action", width=20, command=open_playing).pack(pady=5)
        Button(self, text="Game Over", width=20, command=open_played).pack(pady=5)
        Button(self, text="Explore", width=20, command=open_search).pack(pady=5)
