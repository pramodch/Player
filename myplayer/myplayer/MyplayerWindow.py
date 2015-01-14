# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk, Gst # pylint: disable=E0611
import logging
logger = logging.getLogger('myplayer')

from myplayer_lib import Window
from myplayer.AboutMyplayerDialog import AboutMyplayerDialog
from myplayer.PreferencesMyplayerDialog import PreferencesMyplayerDialog
from quickly import prompts

Gst.is_initialized() or Gst.init(None)

from quickly.widgets.dictionary_grid import DictionaryGrid
from quickly.widgets.media_player_box import MediaPlayerBox
import sys

import os



# See myplayer_lib.Window.py for more details about how this class works
class MyplayerWindow(Window):
    __gtype_name__ = "MyplayerWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MyplayerWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMyplayerDialog
        self.PreferencesDialog = PreferencesMyplayerDialog
        
        self.openbutton = self.builder.get_object("openbutton")
        self.supported_video_formats = [".ogv", ".avi", ".mkv", ".mp4", ".flv"]
        self.supported_audio_formats = [".ogg", ".mp3", ".wav"]
        self.player = MediaPlayerBox(True)
        self.player.show()
        self.ui.paned1.add2(self.player)

    def on_openbutton_clicked(self, widget, data = None):
      response, path = prompts.choose_directory()
      if response == Gtk.ResponseType.OK:
        media_files = []
        formats = self.supported_video_formats + self.supported_audio_formats
        for root, dirs, files in os.walk(path):
          for f in files:
            for format in formats:
              if f.lower().endswith(format):
                file_uri = "file://" + os.path.join(root, f)
                media_files.append({"File":f, "uri":file_uri, "format":format})
        
        for c in self.ui.scrolledwindow1.get_children():
          self.ui.scrolledwindow1.remove(c)

        media_grid = DictionaryGrid(media_files, keys=["File"])
        media_grid.show()
        self.ui.scrolledwindow1.add(media_grid)
