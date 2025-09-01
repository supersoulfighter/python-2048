from typing import List, Optional
import pygame
import thorpy.elements.Box
from game.view.ui.ui_element import UIElement

class Box(thorpy.elements.Box, UIElement):
    def __init__(self, elements_list: Optional[List[UIElement]] = None):
        super().__init__(elements_list, False)
