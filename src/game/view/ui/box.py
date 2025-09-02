from typing import List, Optional
import pygame
import thorpy
from game.view.ui.ui_element import UIElement

class Box(thorpy.Box, UIElement):
    def __init__(self, elements_list: Optional[List[UIElement]] = None):
        if elements_list is None:
            elements_list = []
        super().__init__(elements_list, False)
