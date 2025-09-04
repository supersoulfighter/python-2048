import pygame

from game.model.game_states import GameStates
from game.model.grid import Grid
from game.model.powerups import Powerups
from game.model.score import Score


class GameModel:
    def __init__(self):
        self.grid = Grid()
        self.score = Score()
        self.powerups = Powerups()
        self.state = GameStates.PLAYING
        self.clock = pygame.time.Clock()



    def update(self):
        self.clock.tick(60)

