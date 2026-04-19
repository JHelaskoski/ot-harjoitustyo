from tkinter import Frame, Label, Entry, Button

class SearchView(Frame):
    def __init__(self, root, open_main_menu):
        super().__init__(root)
        self.root = root
        self.open_main_menu = open_main_menu

        Label(self, text="Search Games", font=("Arial", 18)).pack(pady=10)

        Entry(self).pack(pady=5)

        Button(self, text="Back", command=self.open_main_menu).pack(pady=10)
