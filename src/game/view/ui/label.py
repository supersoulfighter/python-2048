import thorpy

from game.view.ui.ui_element import UIElement


class Label(thorpy.Text, UIElement):
    def __init__(self, text: str):
        super().__init__(text)
