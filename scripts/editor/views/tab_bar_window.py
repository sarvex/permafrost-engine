#
#  This file is part of Permafrost Engine. 
#  Copyright (C) 2018 Eduard Permyakov 
#
#  Permafrost Engine is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Permafrost Engine is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pf
from constants import *

class TabBarWindow(pf.Window):
    SELECTED_COLOR = (90, 90, 90, 255)
    SELECTED_HOVER_COLOR = (75, 75, 75, 255)

    def __init__(self):
        resx, _ = pf.get_resolution()

        dims = (0, 0, resx - UI_TAB_BAR_COL_WIDTH, UI_TAB_BAR_HEIGHT)
        super(TabBarWindow, self).__init__("TabBar", dims, pf.NK_WINDOW_NO_SCROLLBAR)
        self.active_idx = 0
        self.labels = []
        self.child_windows = []

    def push_child(self, label, window):
        assert isinstance(label, basestring)
        assert isinstance(window, pf.Window)

        self.labels.append(label) 
        self.child_windows.append(window)

    def update(self):
        orig_rounding = pf.button_style.rounding
        pf.button_style.rounding = 0.0
        self.layout_row_begin(pf.NK_STATIC, UI_TAB_BAR_HEIGHT-10, UI_TAB_BAR_NUM_COLS)
        for idx in range(0, len(self.child_windows)):

            def on_tab_click():
                self.active_idx = idx;
                self.__show_active()
                pf.global_event(EVENT_TOP_TAB_SELECTION_CHANGED, self.active_idx)

            self.layout_row_push(UI_TAB_BAR_COL_WIDTH)

            if idx == self.active_idx:
                normal_style = pf.button_style.normal
                hover_style = pf.button_style.hover
                pf.button_style.normal = TabBarWindow.SELECTED_COLOR
                pf.button_style.hover = TabBarWindow.SELECTED_HOVER_COLOR
                self.button_label(self.labels[idx], on_tab_click)
                pf.button_style.normal = normal_style
                pf.button_style.hover = hover_style
            else:
                self.button_label(self.labels[idx], on_tab_click)

        self.layout_row_end()
        pf.button_style.rounding = orig_rounding

    def show(self):
        super(TabBarWindow, self).show()
        self.__show_active()

    def __show_active(self):
        for idx, window in enumerate(self.child_windows):
            if idx == self.active_idx:
                window.show()
            else:
                window.hide() 

