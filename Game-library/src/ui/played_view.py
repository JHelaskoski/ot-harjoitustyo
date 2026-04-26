from tkinter import Frame, Label, Button, messagebox
from services.game_service import game_service

class PlayedView(Frame):
    def __init__(self, root, open_main_menu, open_rate_game):
        super().__init__(root)
        self.root = root
        self.open_main_menu = open_main_menu
        self.open_rate_game = open_rate_game

        Label(self, text="Played Games", font=("Arial", 18)).pack(pady=10)

        self.game_list_frame = Frame(self)
        self.game_list_frame.pack()

        self.draw_game_list()

        Button(self, text="Back", command=self.open_main_menu).pack(pady=10)

    def draw_game_list(self):
        for widget in self.game_list_frame.winfo_children():
            widget.destroy()

        games = game_service.get_game_by_status("completed")

        for game in games:
            row = Frame(self.game_list_frame)
            row.pack(pady=5)

            Label(row, text=f"{game.name} ({game.release_year})").pack()

            if game.overall_rating is not None:
                Label(row, text=f"Story: {game.story_rating}").pack()
                Label(row, text=f"Graphics: {game.graphics_rating}").pack()
                Label(row, text=f"Gameplay: {game.gameplay_rating}").pack()
                Label(row, text=f"Overall: {game.overall_rating}").pack()
            else:
                Label(row, text="Not rated yet").pack()
                Button(
                    row,
                    text="Rate",
                    command=lambda game_id=game.game_id: self.open_rate_game(game_id)
                ).pack()

            Button(
                row,
                text="Delete",
                command=lambda game_id=game.game_id: self.delete_game(game_id)
            ).pack(pady=5)

    def delete_game(self, game_id):
        confirm = messagebox.askyesno(
            "Delete Game",
            "Are you sure you want to delete this game?"
        )

        if not confirm:
            return

        game_service.delete_game(game_id)
        self.draw_game_list()
