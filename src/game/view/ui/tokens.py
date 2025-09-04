from enum import Enum

# Layout
GAME_WIDTH = 480
GAME_HEIGHT = 640
GAME_GAP = 30
TILE_SIZE = (90,)*2
GRID_GAPS = (9,)*2

#Fonts
FONT_BOLD_PATH = "./assets/fonts/Rubik-Bold.ttf"
FONT_MEDIUM_PATH = "./assets/fonts/Rubik-Medium.ttf"
TILE_FONT_S = 30
TILE_FONT_L = 36


class Colors(Enum):
    """Colors in game"""
    WHITE = (255,)*3
    CREAM = (250, 248, 240)
    BROWN1 = (117, 100, 82)
    BROWN2 = (145, 128, 113)
    BROWN3 = (152, 135, 118)
    BROWN4 = (186, 172, 154, 77)
    BROWN5 = (186, 172, 154)
    BROWN6 = (234, 231, 217)
    ORANGE = (255, 165, 0)
    BACKGROUND = CREAM
    TEXT = BROWN1
    TEXT_INVERSE = WHITE
    GRID = BROWN2
    BUTTON_NORMAL = BROWN5
    BUTTON_HOVER = ORANGE
    BUTTON_SELECTED = BROWN3
    BUTTON_DISABLED = BROWN4
    CONTAINER = BROWN6
    TILE_ = (205, 193, 180)
    TILE_2 = (238, 228, 218)
    TILE_4 = (237, 224, 200)
    TILE_8 = (242, 177, 121)
    TILE_16 = (245, 149, 99)
    TILE_32 = (246, 124, 95)
    TILE_64 = (246, 94, 59)
    TILE_128 = (237, 207, 114)
    TILE_256 = (237, 204, 97)
    TILE_512 = (237, 200, 80)
    TILE_1024 = (237, 197, 63)
    TILE_2048 = (237, 194, 46)


