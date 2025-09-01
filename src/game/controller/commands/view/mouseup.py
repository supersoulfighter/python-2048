from typing import List, Tuple
from pygame.event import Event
import pygame
from game.view.game_view import GameView


def mouseup(event: Event) -> bool:
    view = event.controller.view
    
    if event.button == 1 and view.drag_start:
        end_pos = pygame.mouse.get_pos()
        dx = end_pos[0] - view.drag_start[0]
        dy = end_pos[1] - view.drag_start[1]
        
        # Only process drag if it exceeds threshold
        if abs(dx) > self.DRAG_THRESHOLD or abs(dy) > self.DRAG_THRESHOLD:
            # Determine primary direction
            if abs(dx) > abs(dy):
                direction = (-1 if dx < 0 else 1, 0)
            else:
                direction = (0, -1 if dy < 0 else 1)
            return self.execute_move(direction)
        self.drag_start = None
        self.selected_tile = None
