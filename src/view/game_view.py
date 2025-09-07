import thorpy
from typing import List

from view.ui.game.grid import Grid
from view.ui.game.powerups import Powerups
from view.ui.game.score import Score
from view.ui.theme import theme, BoxStyle
from view.ui.tokens import Colors, GAME_GAP, GAME_WIDTH, GAME_HEIGHT
from view.ui.lib.box import Box
from model.config import *



class GameView(Box):

    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.screen.fill(Colors.BACKGROUND.value)
        pygame.display.set_caption(GAME_NAME)

        thorpy.init(self.screen, theme)

        self.score = Score()
        self.grid = Grid()
        self.powerups = Powerups()
        super().__init__([self.score, self.grid, self.powerups], BoxStyle())
        self.sort_children("v", gap=GAME_GAP)
        self.center_on(self.screen)

        self.updater = self.get_updater()



    def render(self, events: List[pygame.event.Event]):
        self.updater.update(events=events)
        pygame.display.flip()

