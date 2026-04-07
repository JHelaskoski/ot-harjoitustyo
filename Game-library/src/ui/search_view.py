from tkinter import Frame, Label

class SearchView(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text="Search Games").pack()
