# Copyright (C) 2020 Respyrator
# This file is part of Respyrator <https://respyrator.github.io>.
#
# Respyrator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrator.  If not, see <http://www.gnu.org/licenses/>.

# Built-in --------------------------------------------------------------------
from pathlib import Path
import configparser
# Installed -------------------------------------------------------------------
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
# Coded -----------------------------------------------------------------------
from src import logapp
# Program ---------------------------------------------------------------------
LOG = 'GUI:'

GUI_DIR = Path(__file__).resolve().parents[0]
# Kivy config -----------------------------------------------------------------
KIVY_CONFIG = GUI_DIR / 'kivyconfig.ini'
logapp.debug(f'{LOG} loading kivy config')
if KIVY_CONFIG.exists():
    Config.read(str(KIVY_CONFIG))
    logapp.debug(f'{LOG} Kivy configuration completed')
else:
    logapp.error(f'{LOG} Kivy not well configured')
# Gui Config ------------------------------------------------------------------
GUI_CONFIG = GUI_DIR / 'guiconfig.ini'
cfg = configparser.ConfigParser()
cfg.read(str(GUI_CONFIG))
# Set colors
colors = {
    'background': get_color_from_hex(cfg.get('COLOR', 'background')),
    'black': get_color_from_hex(cfg.get('COLOR', 'black')),
    'yellow': get_color_from_hex(cfg.get('COLOR', 'yellow')),
    'white': get_color_from_hex(cfg.get('COLOR', 'white'))
}
# Background Window color
Window.clearcolor = colors.get('brand', (0, 1, 0, 1))
logapp.debug(f'{LOG} Window background to {Window.clearcolor}')
# Load kv files
KV_FILES = GUI_DIR
if KV_FILES:
    from . import splashscreen, loginscreen, infoscreen, \
        feedbackscreen, chargescreen, bottlesscreen
    __all__ = ['splashscreen', 'loginscreen', 'infoscreen',
               'feedbackscreen', 'chargescreen', 'bottlesscreen']
logapp.info(f'{LOG} screens loaded')
