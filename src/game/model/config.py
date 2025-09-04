import pygame
from enum import Enum, auto


GAME_NAME = "Pygame ThorPy 2048"
GRID_SIZE = 4

        
# Keyboard
DIRECTION_KEYS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0)
}


class ViewEvents(Enum):
    """Enum representing the possible events that can be triggered by the view."""
    UNDO = pygame.event.custom_type()
    SWAP = pygame.event.custom_type()
    DELETE = pygame.event.custom_type()


class PowerupType(Enum):
    """Types of powerups available in the game."""
    UNDO = auto()
    SWAP = auto()
    DELETE = auto()
    ROTATE = auto()
    BOMB = auto()


