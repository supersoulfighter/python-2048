import pygame
from enum import Enum, auto


GAME_NAME = "Pygame ThorPy 2048"

# Layout
GAME_WIDTH = 480
GAME_HEIGHT = 640
TILE_SIZE = (94, 94)
GRID_SIZE = 4
GRID_GAPS = (9,9)


# Colors
COLORS = {
    0: (205, 193, 180),      # Empty tile
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    'grid': (152, 135, 118),
    'container': (234, 231, 217),
    'background': (250, 248, 240),
    'text_light': (249, 246, 242),
    'text_dark': (119, 110, 101)
}

        
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
    SWAP = auto()  # Swap Two Tiles
    DELETE = auto()  # Delete by number
    TELEPORT = auto()  # Teleport a Tile
    ROTATE = auto()  # Rotate Outer Ring
    BOMB = auto()  # Delete tile and all adjacent tiles


