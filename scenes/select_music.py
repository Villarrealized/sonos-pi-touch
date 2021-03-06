from pygame import Rect

from sonos import Sonos

from ui.list_view import ListView
from ui.modal_scene import ModalScene

from scenes.select_artist import SelectArtist
from scenes.select_album import SelectAlbum
from scenes.select_genre import SelectGenre
from scenes.select_playlist import SelectPlaylist
from scenes.select_favorite import SelectFavorite

from ui.image import Image
from ui.button import Button
from ui.label import Label

import ui.colors as colors


class SelectMusic(ModalScene):

    CATEGORIES = ['Artists', 'Albums', 'Genres', 'Playlists', 'Favorites']

    def __init__(self, sonos):
        ModalScene.__init__(self, "Music Library")

        self.sonos = sonos
        self.background_color = colors.NAVY
        self.layout()

        self.create_library_list()

    def create_library_list(self):
        y = 80
        for category in SelectMusic.CATEGORIES:
            library_option_button = Button(Rect(40,y,240,40), 34, Label.LEFT, text=category)
            library_option_button.on_tapped.connect(self.select_library_option)
            self.add_child(library_option_button)            
            y += 80

    def select_library_option(self, button):
        option = button.label.text        
        scene = None

        if option == 'Artists':
            scene = SelectArtist(self.sonos)            
        elif option == 'Albums':
            scene = SelectAlbum(self.sonos)            
        elif option == 'Genres':
            scene = SelectGenre(self.sonos)            
        elif option == 'Playlists':
            scene = SelectPlaylist(self.sonos)            
        elif option == 'Favorites':
            scene = SelectFavorite(self.sonos)

        if scene is not None: self.add_child(scene)
            