from typing import override

from pygame.event import Event, post

from model.config import ViewEvents
from view.ui.lib.text import Text
from view.ui.tokens import TILE_SIZE, Colors, SELECTED_BORDER_WIDTH, UNSELECTED_BORDER_WIDTH
from view.ui.lib.ui_element import UIElement



class Cell(Text, UIElement):
    def __init__(self, text: str,  row:int, col:int):
        self.row = row
        self.col = col
        super().__init__(text=text)
        self.set_size(TILE_SIZE)
        self.at_unclick = lambda r=row,c=col: post(Event(ViewEvents.CELL_CLICK.value, {"cell":self}))



    @override
    def set_text(self, text: str):
        super().set_text(text, False)

        tile_color = getattr(Colors, f"TILE_{text}")
        self.set_bck_color(tile_color.value)

        if text == "2" or text == "4":
            self.set_font_color(Colors.TEXT.value)
        else:
            self.set_font_color(Colors.TEXT_INVERSE.value)

        # Using get_style() did not work here, so using style_normal attribute
        if len(text) > 3:
            s = self.style_normal
            self.set_style_attr("font", s.font_s)
        else:
            s = self.style_normal
            self.set_style_attr("font", s.font_l)



    def select(self, select:bool):
        if select:
            self.set_style_attr("border_thickness", SELECTED_BORDER_WIDTH)
        else:
            self.set_style_attr("border_thickness", UNSELECTED_BORDER_WIDTH)
