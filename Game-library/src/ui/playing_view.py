from tkinter import Frame, Label, Button, messagebox
from services.game_service import game_service

class PlayingView(Frame):
    """Näkymä parhaillaan pelattaville peleille.

    Args:
        root: Tkinter-juuri-ikkuna.
        open_main_menu: Funktio, joka avaa päävalikon.
    """
    def __init__(self, root, open_main_menu):
        """_summary_

        Args:
            root (_type_): _description_
            open_main_menu (_type_): _description_
        """

        super().__init__(root)
        self.root = root
        self.open_main_menu = open_main_menu

        Label(self, text="Playing Now", font=("Arial", 18)).pack(pady=10)

        self.game_list_frame = Frame(self)
        self.game_list_frame.pack()

        self.draw_game_list()

        Button(self, text="Back", command=self.open_main_menu).pack(pady=10)

    def draw_game_list(self):
        for widget in self.game_list_frame.winfo_children():
            widget.destroy()

        games = game_service.get_game_by_status("playing")

        for game in games:
            row = Frame(self.game_list_frame)
            row.pack(pady=5)

            Label(row, text=f"{game.name} ({game.release_year})").pack(side="left")

            Button(
                row,
                text="Delete",
                command=lambda game_id=game.game_id: self.delete_game(game_id)
            ).pack(side="left", padx=10)

            Button(
                row,
                text="Move to Completed",
                command=lambda game_id=game.game_id: self.change_status(game_id, "completed")
            ).pack(side="left", padx=10)

    def delete_game(self, game_id):
        """Poistaa pelin.
        Args:
            game_id: Poistettavan pelin ID.
        """

        confirm = messagebox.askyesno(
            "Delete Game",
            "Are you sure you want to delete this game?"
        )

        if not confirm:
            return

        game_service.delete_game(game_id)
        self.draw_game_list()

    def change_status(self, game_id, new_status):
        game_service.change_status(game_id, new_status)
        self.draw_game_list()
