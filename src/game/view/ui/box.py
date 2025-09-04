from typing import List, Optional, Any
import thorpy
from game.view.ui.ui_element import UIElement

class Box(thorpy.Box, UIElement):
    def __init__(self, children: Optional[List[UIElement]] = None, style:Any=None):
        if children is None:
            children = []
        super().__init__(children, False, style)

        #Tried setting size here, but doesn't work in init apparently

