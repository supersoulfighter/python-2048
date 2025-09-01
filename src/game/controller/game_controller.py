import pygame
from typing import List, Optional, Tuple
from collections import deque
import math

from game.model.game_state import GameState
from game.model.game_states import GameStates
from game.view.game_view import GameView
from game.controller.commands import Command, MoveCommand, PowerUpCommand
from game.controller.commands.view.mouseup import mouseup


class GameController:
    DRAG_THRESHOLD = 50  # Minimum pixels to trigger a swipe
    
    def __init__(self, model: GameState, view: GameView):
        self.model = model
        self.view = view
        
        # Set up input mappings
        self.direction_keys = {
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1),
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0)
        }
        
        # Bind powerup callbacks
        for name, button in self.view.powerup_buttons.items():
            button.set_callback(lambda n=name: self.execute_powerup(n))
    
    def get_grid_position(self, mouse_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """Convert mouse coordinates to grid position."""
        x, y = mouse_pos
        # Get grid offset from view
        grid_x = (x - self.view.grid_offset[0]) // self.view.TILE_SIZE
        grid_y = (y - self.view.grid_offset[1]) // self.view.TILE_SIZE
        
        if 0 <= grid_x < self.model.grid_size and 0 <= grid_y < self.model.grid_size:
            return (int(grid_x), int(grid_y))
        return None




    def update(self) -> None:
        for event in pygame.event.get():
            event.controller = self
            
            if event.type == pygame.QUIT:
                self.model.state = GameStates.QUITING

            elif event.type == pygame.KEYDOWN:
                if event.key in self.direction_keys:
                    direction = self.direction_keys[event.key]
                    return self.execute_move(direction)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.drag_start = event.pos
                    self.selected_tile = self.get_grid_position(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                mouseup(event)

            elif event.type == pygame.MOUSEMOTION:
                if self.drag_start:
                    # Update view to show drag preview
                    dx = event.pos[0] - self.drag_start[0]
                    dy = event.pos[1] - self.drag_start[1]
                    self.view.update_drag_preview(self.selected_tile, (dx, dy))
