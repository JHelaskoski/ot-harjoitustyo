from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar
from services.game_service import game_service
from services.console_service import console_service
from services.genre_service import genre_service

class SearchView(Frame):
    def __init__(self, root, open_main_menu):
        super().__init__(root)
        self.root = root
        self.open_main_menu = open_main_menu

        Label(self, text="Search Games", font=("Arial", 18)).pack(pady=10)

        # haetaan nimellä
        self.search_entry = Entry(self)
        self.search_entry.pack(pady=5)

        # konsoli
        Label(self, text="Filter by console:").pack()
        consoles = console_service.get_all_consoles()
        self.console_map = {console["name"]: console["id"] for console in consoles}

        self.console_var = StringVar(self)
        self.console_var.set("None")

        OptionMenu(self, self.console_var, "None", *self.console_map.keys()).pack()

        # genre
        Label(self, text="Filter by genre:").pack()
        genres = genre_service.get_all_genres()
        self.genre_map = {genre["name"]: genre["id"] for genre in genres}

        self.genre_var = StringVar(self)
        self.genre_var.set("None")

        OptionMenu(self, self.genre_var, "None", *self.genre_map.keys()).pack()

        Button(self, text="Search", command=self.search_games).pack(pady=5)

        # hakutulos
        self.results_frame = Frame(self)
        self.results_frame.pack(pady=10)

        Button(self, text="Back", command=self.open_main_menu).pack(pady=10)

    def search_games(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        query = self.search_entry.get().strip()
        console = self.console_var.get()
        genre = self.genre_var.get()

        if query:
            results = game_service.search_games(query=query)
        elif console != "None":
            results = game_service.search_games(console_id=self.console_map[console])
        elif genre != "None":
            results = game_service.search_games(genre_id=self.genre_map[genre])
        else:
            Label(self.results_frame, text="Enter search or choose filter").pack()
            return

        if not results:
            Label(self.results_frame, text="No results found").pack()
            return

        for game in results:
            Label(self.results_frame, text=f"{game['name']} ({game['status']})").pack(anchor="w")
