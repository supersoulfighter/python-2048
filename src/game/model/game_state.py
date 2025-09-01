from typing import List, Optional, Tuple
import pygame

from game.model.grid import Grid
from game.model.score import Score
from game.model.game_states import GameStates
from game.model.powerups import PowerUpManager



class GameState:
    def __init__(self):
        self.grid = Grid(4)
        self.score_manager = Score()
        self.powerup_manager = PowerUpManager()
        self.state = GameStates.PLAYING
        self.clock = pygame.time.Clock()



    def update(self):
        self.clock.tick(60)

