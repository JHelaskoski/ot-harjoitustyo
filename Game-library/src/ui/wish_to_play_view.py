from tkinter import Frame, Label

class WishToPlayView(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text="Wish to Play").pack()
