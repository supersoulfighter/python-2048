from typing import Any
import thorpy

from game.view.ui.ui_element import UIElement

class Text(thorpy.Text, UIElement):
    def __init__(self, text: str, style:Any = None):
        super().__init__(text=text, style_normal=style)
