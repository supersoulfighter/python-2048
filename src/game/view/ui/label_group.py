from typing import Optional, Callable

import thorpy

from game.view.ui.label import Label
from game.view.ui.ui_element import UIElement


class LabelGroup(thorpy.Labelled, UIElement):
    def __init__(self, label:str, element:UIElement = None, callback: Optional[Callable] = None):
        super().__init__(label, element, Label)

        if callback:
            self.set_callback(callback)
