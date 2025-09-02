from pygame.event import Event, post
import thorpy
from typing import Dict, List

from game.view.ui.button import Button
from game.view.ui.box import Box
from game.view.ui.text import Text
from game.model.config import *



class GameView(Box):

    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        thorpy.set_default_font("./assets/fonts/Rubik-Bold.ttf", font_size=24)

        thorpy.init(self.screen, thorpy.theme_round2)
        super().__init__()

        # Score
        self.score_current = Text("Score: 0")
        self.score_high = Text("Best: 0")
        self.score_container = Box([self.score_current, self.score_high])
        self.score_container.sort_children("h")
        self.add_child(self.score_container)
        
        # Grid
        self.grid_cells = []
        grid_buttons = []
        for row in range(GRID_SIZE):
            grid_row = []
            for col in range(GRID_SIZE):
                cell_button = Button("", TILE_SIZE)
                grid_row.append(cell_button)
                grid_buttons.append(cell_button)
            self.grid_cells.append(grid_row)
        
        self.numbers_grid = Box(grid_buttons)
        # ThorPy Grid layout is buggy. Setting nx and ny, and setting them to n-1 seems to compensate.
        self.numbers_grid.sort_children(
            mode="grid",
            nx=GRID_SIZE-1,
            ny=GRID_SIZE-1,
            grid_gaps=(0, 0)
        )
        self.add_child(self.numbers_grid)
 
        # Powerups
        self.powerup_buttons = {
            'undo': Button("Undo", None, lambda: post(Event(ViewEvents.UNDO.value))),
            'swap': Button("Swap", None, lambda: post(Event(ViewEvents.SWAP.value))),
            'delete': Button("Delete", None, lambda: post(Event(ViewEvents.DELETE.value))),
        }
        self.powerups_container = Box([self.powerup_buttons[name] for name in self.powerup_buttons])
        self.powerups_container.sort_children("h")
        self.add_child(self.powerups_container)

        self.sort_children("v")
        self.updater = self.get_updater()
        self.center_on(self.screen)
     


    def update_score(self, score: int, high_score: int):
        self.score_current.set_text(f"Score: {score}")
        self.score_high.set_text(f"Best: {high_score}")
        


    def update_grid(self, cells: list[list[int]]):
        """Update the grid display to reflect the current state of the grid model."""
        for row in range(len(cells)):
            for col in range(len(cells[row])):
                cell_value = cells[row][col]
                cell_button = self.grid_cells[row][col]
                if cell_value == 0:
                    cell_button.set_text("")
                else:
                    cell_button.set_text(str(cell_value))



    def update_powerups(self, powerups: Dict):
        for name, powerup in powerups.items():
            button = self.powerup_buttons.get(name)
            if button:
                button.set_enabled(powerup.active)
    


    def render(self, events: List[pygame.event.Event]):
        self.updater.update(events=events)
        pygame.display.flip()

