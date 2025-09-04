from typing import override
from game.view.ui.text import Text
from game.view.ui.tokens import TILE_SIZE, Colors, TILE_FONT_S, TILE_FONT_L
from game.view.ui.ui_element import UIElement



class Cell(Text, UIElement):
    def __init__(self, text: str):
        super().__init__(text=text)
        self.set_size(TILE_SIZE)

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
