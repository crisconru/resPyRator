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
# Coded -----------------------------------------------------------------------
from src import logapp
# Program ---------------------------------------------------------------------
LOG = 'GUI:'

__all__ = ['logapp']

BASE_DIR = Path(__file__).resolve().parents[0]
GUI_CONFIG = BASE_DIR / 'guiconfig.ini'
cfg = configparser.ConfigParser()
cfg.read(str(GUI_CONFIG))
# COLORs
gui_colors = {
    'background': cfg.get('COLOR', 'background'),
    'black': cfg.get('COLOR', 'black'),
    'yellow': cfg.get('COLOR', 'yellow'),
    'white': cfg.get('COLOR', 'white')
}
# IMGs
gui_img = {}
# TXTs
gui_txts = {}

logapp.info(f'{LOG} configuration completed')