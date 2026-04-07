from tkinter import Frame, Label

class PlayedView(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text="Played Games").pack()
