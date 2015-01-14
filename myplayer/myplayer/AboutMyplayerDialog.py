# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

import logging
logger = logging.getLogger('myplayer')

from myplayer_lib.AboutDialog import AboutDialog

# See myplayer_lib.AboutDialog.py for more details about how this class works.
class AboutMyplayerDialog(AboutDialog):
    __gtype_name__ = "AboutMyplayerDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutMyplayerDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.
