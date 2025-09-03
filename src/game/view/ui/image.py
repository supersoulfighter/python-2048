from typing import Optional, Callable, Tuple, Any
import thorpy

from game.view.ui.ui_element import UIElement

class Image(thorpy.Image, UIElement):
    def __init__(self, img:Any, size:Tuple[int,int] = None, callback: Optional[Callable] = None):
        super().__init__(img)

        if size:
            self.set_size(size)

        if callback:
            self.set_callback(callback)
