from typing import Tuple
import pygame
import thorpy

from game.view.ui.ui_element import UIElement

class Text(thorpy.Text, UIElement):
    def __init__(self, text: str):
        super().__init__(text)
