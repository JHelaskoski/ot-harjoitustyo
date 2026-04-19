from tkinter import Frame, Label, Button

class MainMenuView(Frame):
    def __init__(self, root,
                 open_wish_to_play,
                 open_playing,
                 open_played,
                 open_search,
                 open_add_game):

        super().__init__(root)

        Button(self, text="Wishes", command=open_wish_to_play).pack()
        Button(self, text="In Action", command=open_playing).pack()
        Button(self, text="Game Over", command=open_played).pack()
        Button(self, text="Explore", command=open_search).pack()
        Button(self, text="Add Game", command=open_add_game).pack()

