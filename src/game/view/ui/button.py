from typing import Optional, Callable
import pygame
import thorpy.elements.Button

from game.view.ui.ui_element import UIElement

class Button(thorpy.elements.Button, UIElement):
    def __init__(self, text: str, callback: Optional[Callable] = None):
        super().__init__(text)
