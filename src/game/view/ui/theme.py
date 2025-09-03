from thorpy import theme_round
from thorpy.styles import RoundStyle
from game.model.config import *
from game.view.ui.box import Box
from game.view.ui.button import Button


class Colors(Enum):
    """Colors in game"""
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
    GRID = BROWN2
    BUTTON_NORMAL = BROWN5
    BUTTON_HOVER = ORANGE
    BUTTON_SELECTED = BROWN3
    BUTTON_DISABLED = BROWN4
    CONTAINER = BROWN6


# class BaseStyle:
#     font = None
#     font_antialias = True
#     font_name = None
#     font_size = p.fallback_font_size
#     font_color = (20,) * 3
#     font_leading = 0
#     font_align = "l"  # can be either "l", "c" or "r"
#     font_auto_multilines_width = 0
#     font_rich_text_tag = None
#     size = "auto"
#     margins = (6, 6)
#     bck_color = (220,) * 3
#     shadowgen: Optional[Shadow] = None
#     offset = (0, 0)
#     radius = 0

# class RoundStyle(BaseStyle):
#     radius = 10 #if radius is less than 1, then its relative to min side
#     force_radius = False
#     n_smooth = 1.5 #impacts perf !
#     border_color = (50,50,50)
#     border_thickness = 0

class BoxStyle(RoundStyle):
    bck_color = Colors.BACKGROUND.value

class GridStyle(RoundStyle):
    bck_color = Colors.GRID.value
    margins = GRID_GAPS

class ContainerStyle(RoundStyle):
    bck_color = Colors.CONTAINER.value
    margins = GRID_GAPS

class ButtonStyleNormal(RoundStyle):
    bck_color = Colors.BUTTON_NORMAL.value
    font_size = 0

class ButtonStyleHover(ButtonStyleNormal):
    bck_color = Colors.BUTTON_HOVER.value

class ButtonStylePressed(ButtonStyleNormal):
    bck_color = Colors.BUTTON_SELECTED.value

class ButtonStyleDisabled(ButtonStyleNormal):
    bck_color = Colors.BUTTON_DISABLED.value


def theme():
    theme_round(base_color=COLORS['background'])

    Box.style_normal = BoxStyle()

    Button.style_normal = ButtonStyleNormal()
    Button.style_hover = ButtonStyleHover()
    Button.style_pressed = ButtonStylePressed()
    Button.style_locked = ButtonStyleDisabled()

    # thorpy.set_style_attr("font_color", (0,)*3, "all")
    # thorpy.set_style_attr("font_color", thorpy.graphics.enlighten(thorpy.Button.style_normal.font_color), "hover")

