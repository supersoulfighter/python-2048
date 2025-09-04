from thorpy import theme_round, set_style_attr
from thorpy.styles import RoundStyle
from game.model.config import *
from game.view.ui.game.cell import Cell
from game.view.ui.game.grid import Grid
from game.view.ui.box import Box
from game.view.ui.button import Button
from game.view.ui.label import Label
from game.view.ui.tokens import Colors, GRID_GAPS, FONT_MEDIUM_PATH, FONT_BOLD_PATH, TILE_FONT_L, TILE_FONT_S


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

class GameStyle(RoundStyle):
    pass

class LabelStyle(GameStyle):
    font_color = Colors.TEXT.value
    bck_color = Colors.CONTAINER.value
    margins = (0,0)
    radius = 0

class ScoreValueStyle(GameStyle):
    font_color = Colors.TEXT.value
    bck_color = Colors.CONTAINER.value
    margins = (0,0)
    radius = 0

class BoxStyle(GameStyle):
    bck_color = Colors.BACKGROUND.value

class GridStyle(GameStyle):
    bck_color = Colors.GRID.value
    margins = GRID_GAPS

class CellStyle(GameStyle):
    bck_color = Colors.TILE_.value

class ContainerStyle(GameStyle):
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
    theme_round(base_color=Colors.BACKGROUND.value)

    s = LabelStyle()
    s.font = pygame.font.Font(FONT_MEDIUM_PATH, 12)
    Label.style_normal = s

    ScoreValueStyle.font = pygame.font.Font(FONT_BOLD_PATH, 20)

    Box.style_normal = BoxStyle()

    Button.style_normal = ButtonStyleNormal()
    Button.style_hover = ButtonStyleHover()
    Button.style_pressed = ButtonStylePressed()
    Button.style_locked = ButtonStyleDisabled()

    Grid.style_normal = GridStyle()

    s = CellStyle()
    s.font_l = pygame.font.Font(FONT_BOLD_PATH, TILE_FONT_L)
    s.font_s = pygame.font.Font(FONT_BOLD_PATH, TILE_FONT_S)
    s.font = s.font_l
    Cell.style_normal = s

    # set_style_attr(attr="font_name", value=font_bold_path, states="all", only_to_cls=Label)
    # thorpy.set_style_attr("font_color", (0,)*3, "all")
    # thorpy.set_style_attr("font_color", thorpy.graphics.enlighten(thorpy.Button.style_normal.font_color), "hover")

