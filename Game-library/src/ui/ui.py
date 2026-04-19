from ui.main_menu_view import MainMenuView
from ui.played_view import PlayedView
from ui.playing_view import PlayingView
from ui.search_view import SearchView
from ui.wish_to_play_view import WishToPlayView
from ui.add_game_view import AddGameView
from ui.rate_game_view import RateGameView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu()

    def _hide_current_view(self):
        #Edellinen näkymä tulee aina piilottaa, ennen kuin uusi sivu näytetään
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_main_menu(self):
        #Tuhotaan ed.näkymä, jos tällainen on
        self._hide_current_view()

        #Vaihdetaan näkymä nykyiseen valittuun
        self._current_view = MainMenuView(
            self._root,
            self._show_wish_to_play,
            self._show_playing,
            self._show_played,
            self._show_search,
            self._show_add_game_view
        )

        self._current_view.pack()

    def _show_wish_to_play(self):
        self._hide_current_view()
        self._current_view = WishToPlayView(self._root, self._show_main_menu)
        self._current_view.pack()

    def _show_playing(self):
        self._hide_current_view()

        self._current_view = PlayingView(self._root, self._show_main_menu)
        self._current_view.pack()

    def _show_played(self):
        self._hide_current_view()
        self._current_view = PlayedView(self._root, self._show_main_menu, self.show_rate_game)
        self._current_view.pack()

    def _show_search(self):
        self._hide_current_view()
        self._current_view = SearchView(self._root, self._show_main_menu)
        self._current_view.pack()

    def _show_add_game_view(self):
        self._hide_current_view()
        self._current_view = AddGameView(
            self._root,
            self._show_main_menu,
            self.show_rate_game
        )
        self._current_view.pack()

    def show_rate_game(self, game_id):
        self._hide_current_view()
        self._current_view = RateGameView(self._root, game_id, self._show_played)
        self._current_view.pack()
