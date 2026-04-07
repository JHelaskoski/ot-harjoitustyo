from tkinter import Frame, Label

class PlayingView(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text="Playing Now").pack()
