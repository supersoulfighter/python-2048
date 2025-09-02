from typing import List, Optional, Tuple
import pygame

from game.model.grid import Grid
from game.model.score import Score
from game.model.game_states import GameStates
from game.model.powerups import Powerups



class GameModel:
    def __init__(self):
        self.grid = Grid()
        self.score = Score()
        self.powerups = Powerups()
        self.state = GameStates.PLAYING
        self.clock = pygame.time.Clock()



    def update(self):
        self.clock.tick(60)

