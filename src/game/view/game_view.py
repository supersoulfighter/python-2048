import pygame
import thorpy
import tween
from typing import Dict, List, Optional, Tuple

from game.view.ui.button import Button
from game.view.ui.box import Box
from game.view.ui.text import Text
from game.model.game_state import GameState
from game.view.animations import AnimationManager
from game.model.config import TILE_SIZE, TILE_MARGIN, GRID_SIZE, GRID_PADDING, COLORS



class GameView(Box):

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("2048 Plus")
 
        # Animation system
        self.animation_manager = AnimationManager()
     
        # Drag preview state
        self.drag_preview: Optional[Tuple[Tuple[int, int], Tuple[float, float]]] = None
                
        # Mouse state
        self.drag_start: Optional[Tuple[int, int]] = None
        self.selected_tile: Optional[Tuple[int, int]] = None
 
        # Animation state
        self.tile_animations: Dict[Tuple[int, int], tween.Tween] = {}
        self.tile_scales: Dict[Tuple[int, int], float] = {}
        
        super().__init__()
        self._init_ui()
        


    def _init_ui(self):
       
        # Score
        self.score_current = Text("Score: 0")
        self.score_high = Text("Best: 0")
        self.score_container = Box([self.score_current, self.score_high])
        self.add_child(self.score_container)
        self.score_container.sort_children("h")
        
        # Numbers grid
        total_size = TILE_SIZE * GRID_SIZE + TILE_MARGIN * (GRID_SIZE - 1)
        screen_w, screen_h = self.screen.get_size()
        self.grid_offset = (
            (screen_w - total_size) // 2,
            (screen_h - total_size) // 2
        )
        self.numbers_grid = Box()
        self.add_child(self.numbers_grid)
        
        # Tiles
        self.tile_sprites: Dict[Tuple[int, int], pygame.Surface] = {}
        self.tile_positions: Dict[Tuple[int, int], Tuple[float, float]] = {}
   
        
        # Power-up buttons
        self.powerup_buttons = {
            'undo': Button("Undo"),
            'swap': Button("Swap"),
            'delete': Button("Delete"),
        }
        self.powerups_container = Box([self.powerup_buttons[name] for name in self.powerup_buttons])
        self.powerups_container.sort_children("h")
        self.add_child(self.powerups_container)

        self.sort_children("v")
        self.updater = self.get_updater()
   
  


    def get_tile_position(self, grid_pos: Tuple[int, int]) -> Tuple[int, int]:
        """Convert grid coordinates to screen coordinates."""
        x = self.grid_offset[0] + GRID_PADDING + grid_pos[0] * (TILE_SIZE + TILE_MARGIN)
        y = self.grid_offset[1] + GRID_PADDING + grid_pos[1] * (TILE_SIZE + TILE_MARGIN)
        return (x, y)
        


    def create_tile_animation(self, from_pos: Tuple[int, int], to_pos: Tuple[int, int], 
                            duration: float = 0.15) -> None:
        """Create a movement animation for a tile."""
        start = self.get_tile_position(from_pos)
        end = self.get_tile_position(to_pos)
        
        def on_complete():
            if to_pos in self.tile_animations:
                del self.tile_animations[to_pos]
        
        anim = self.animation_manager.create_movement(
            start, end, duration, on_complete
        )
        self.tile_animations[to_pos] = anim
        
    def create_merge_animation(self, pos: Tuple[int, int], value: int,
                             duration: float = 0.1) -> None:
        """Create a merge animation for a tile."""
        tile_pos = self.get_tile_position(pos)
        
        def on_complete():
            if pos in self.tile_scales:
                del self.tile_scales[pos]
        
        anim = self.animation_manager.create_merge(
            tile_pos, duration, on_complete
        )
        self.tile_scales[pos] = 1.0  # Start at normal scale
        


    def create_spawn_animation(self, pos: Tuple[int, int], 
                              duration: float = 0.15) -> None:
        """Create a spawn animation for a new tile."""
        tile_pos = self.get_tile_position(pos)
        
        def on_complete():
            if pos in self.tile_scales:
                del self.tile_scales[pos]
        
        anim = self.animation_manager.create_spawn(
            tile_pos, duration, on_complete
        )
        self.tile_scales[pos] = 0.0  # Start invisible
        
    def update_score(self, score: int, high_score: int):
        self.score_current.set_text(f"Score: {score}")
        self.score_high.set_text(f"Best: {high_score}")
        
    def update_powerups(self, powerups: Dict):
        for name, powerup in powerups.items():
            button = self.powerup_buttons.get(name)
            if button:
                button.set_enabled(powerup.active)
    


    def update_drag_preview(self, tile_pos: Optional[Tuple[int, int]], 
                           offset: Tuple[float, float]):
        """Update the preview of a tile being dragged."""
        self.drag_preview = (tile_pos, offset) if tile_pos else None



    def render(self):
        # Clear screen
        self.screen.fill(self.COLORS['background'])
        
        # Update animations
        current_time = pygame.time.get_ticks() / 1000.0
        self.animation_manager.update(current_time)
        
        # Draw game elements
        self.numbers_grid.draw(self.screen)
        self.score_current.draw(self.screen)
        self.score_high.draw(self.screen)
        self.powerups_container.draw(self.screen)
        
        # Draw grid background
        pygame.draw.rect(self.screen, COLORS['background'],
                       (self.grid_offset[0], self.grid_offset[1],
                        GRID_SIZE * (TILE_SIZE + TILE_MARGIN) - TILE_MARGIN,
                        GRID_SIZE * (TILE_SIZE + TILE_MARGIN) - TILE_MARGIN))
        
        # Draw tiles with animations
        for pos, sprite in self.tile_sprites.items():
            if self.drag_preview and self.drag_preview[0] == pos:
                # Skip the dragged tile, it will be drawn last
                continue
                
            base_x, base_y = self.get_tile_position(pos)
            
            # Apply movement animation
            if pos in self.tile_animations:
                anim = self.tile_animations[pos]
                base_x, base_y = anim.current_pos
            
            # Apply scale animation
            scale = self.tile_scales.get(pos, 1.0)
            if scale != 1.0:
                # Scale sprite around its center
                scaled_size = (int(sprite.get_width() * scale),
                             int(sprite.get_height() * scale))
                if scaled_size[0] > 0 and scaled_size[1] > 0:
                    scaled_sprite = pygame.transform.scale(sprite, scaled_size)
                    # Adjust position to maintain center
                    x = base_x + (sprite.get_width() - scaled_sprite.get_width()) // 2
                    y = base_y + (sprite.get_height() - scaled_sprite.get_height()) // 2
                    self.screen.blit(scaled_sprite, (x, y))
            else:
                self.screen.blit(sprite, (base_x, base_y))
        
        # Draw drag preview if active
        if self.drag_preview:
            pos, (dx, dy) = self.drag_preview
            base_x, base_y = self.get_tile_position(pos)
            sprite = self.tile_sprites.get(pos)
            if sprite:
                self.screen.blit(sprite, (base_x + dx, base_y + dy))
