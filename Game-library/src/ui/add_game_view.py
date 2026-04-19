from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, messagebox
from services.game_service import game_service
from services.console_service import console_service
from services.console_model_service import console_model_service

class AddGameView(Frame):
    def __init__(self, root, open_main_menu, open_rate_game):
        super().__init__(root)
        self.open_main_menu = open_main_menu
        self.open_rate_game = open_rate_game

        Label(self, text="Add New Game", font=("Arial", 18)).pack(pady=10)

        # nimi
        Label(self, text="Name:").pack()
        self.name_entry = Entry(self)
        self.name_entry.pack()

        # konsoli/konsolimalli yhtee otsikkoo
        Label(self, text="Console:").pack()

        console_frame = Frame(self)
        console_frame.pack()

        # eka konsoliperhe
        self.console_var = StringVar(self)
        self.console_var.set("Select console")

        consoles = console_service.get_all_consoles()
        self.console_map = {console["name"]: console["id"] for console in consoles}

        OptionMenu(
            console_frame,
            self.console_var,
            "Select console",
            *self.console_map.keys(),
            command=self.update_models
        ).pack(side="left")

        # konsolimalli
        self.model_var = StringVar(self)
        self.model_var.set("Select model")

        self.model_menu = OptionMenu(console_frame, self.model_var, "Choose console first")
        self.model_menu.pack(side="left")

        self.model_map = {}

        # julkaisu vuosi
        Label(self, text="Release Year:").pack()
        self.year_entry = Entry(self)
        self.year_entry.pack()

        # kirjaston status
        Label(self, text="Status:").pack()
        self.status_var = StringVar(self)
        self.status_var.set("Status")
        OptionMenu(self, self.status_var, "wishlist", "playing", "completed").pack()

        # napit
        Button(self, text="Add Game", command=self.add_game).pack(pady=10)
        Button(self, text="Back", command=self.open_main_menu).pack()

   #päivittää konsoli mallit, jos konsoli vaihtuu
    def update_models(self, selected_console):
        if selected_console == "Select console":
            self.model_var.set("Select model")
            self.model_map = {}
            return

        console_id = self.console_map[selected_console]
        models = console_model_service.get_models_by_console(console_id)

        self.model_map = {model["name"]: model["id"] for model in models}

        self.model_var.set("Select model")
        menu = self.model_menu["menu"]
        menu.delete(0, "end")

        for name in self.model_map.keys():
            menu.add_command(
                label=name,
                command=lambda value=name: self.model_var.set(value)
            )

    def add_game(self):
        try:
            name = self.name_entry.get()
            model_name = self.model_var.get()
            console_model_id = self.model_map[model_name]

            year_text = self.year_entry.get()
            year = int(year_text) if year_text else None

            status = self.status_var.get()

            game_id = game_service.add_game(
                name,
                console_model_id,
                year,
                status,
                []
            )

            #jos pelattu, peli arvostellaan
            if status == "completed":
                self.open_rate_game(game_id)
                return

            self.open_main_menu()

        except ValueError as error:
            messagebox.showerror("Invalid input", str(error))

        except KeyError as error:
            messagebox.showerror("Selection error", f"Invalid selection: {error}")
