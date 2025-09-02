from typing import Optional, Callable, Tuple
import thorpy

from game.view.ui.ui_element import UIElement

class Button(thorpy.Button, UIElement):
    def __init__(self, text: str, size:Tuple[int,int] = None, callback: Optional[Callable] = None):
        super().__init__(text)

        if size:
            self.set_size(size)

        if callback:
            self.set_callback(callback)
