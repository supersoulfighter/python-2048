from abc import ABC, abstractmethod
from typing import Tuple, Optional, Callable
import pygame
from thorpy import loops
import thorpy


class UIElement(thorpy.elements.Element):
    
    def set_position(self, x: int, y: int):
        self.set_topleft((x, y))
    
    def get_position(self) -> Tuple[int, int]:
        return self.get_rect().topleft
    
    def get_size(self) -> Tuple[int, int]:
        rect = self.get_rect()
        return (rect.width, rect.height)
    
    def set_callback(self, callback: Callable):
        self.at_unclick = callback
    
    def set_enabled(self, enabled: bool):
        self.set_invisible(not enabled)
