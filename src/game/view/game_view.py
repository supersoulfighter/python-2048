import pygame
import thorpy
import tween
from typing import Dict, List, Optional, Tuple

from game.view.ui.button import Button
from game.view.ui.box import Box
from game.view.ui.text import Text
from game.view.animations import AnimationManager
from game.model.config import *


class GameView(Box):

    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        thorpy.init(self.screen)
        super().__init__()
       
        # Score
        self.score_current = Text("Score: 0")
        self.score_high = Text("Best: 0")
        self.score_container = Box([self.score_current, self.score_high])
        self.score_container.sort_children("h")
        self.add_child(self.score_container)
        
        # Grid

        self.numbers_grid = Box()
        self.add_child(self.numbers_grid)
 
        # Powerups
        self.powerup_buttons = {
            'undo': Button("Undo", lambda: pygame.event.post(pygame.event.Event(ViewEvents.UNDO))),
            'swap': Button("Swap", lambda: pygame.event.post(pygame.event.Event(ViewEvents.SWAP))),
            'delete': Button("Delete", lambda: pygame.event.post(pygame.event.Event(ViewEvents.DELETE))),
        }
        self.powerups_container = Box([self.powerup_buttons[name] for name in self.powerup_buttons])
        self.powerups_container.sort_children("h")
        self.add_child(self.powerups_container)

        self.sort_children("v")
        self.updater = self.get_updater()
     



    def update_score(self, score: int, high_score: int):
        self.score_current.set_text(f"Score: {score}")
        self.score_high.set_text(f"Best: {high_score}")
        


    def update_powerups(self, powerups: Dict):
        for name, powerup in powerups.items():
            button = self.powerup_buttons.get(name)
            if button:
                button.set_enabled(powerup.active)
    


    def render(self, events: List[pygame.event.Event]):
        self.updater.update(events=events)
        pygame.display.flip()

