from game.model.config import GRID_SIZE
from game.view.ui.button import Button
from game.view.ui.box import Box
from game.view.ui.tokens import TILE_SIZE, GRID_GAPS


class Grid(Box):
    def __init__(self):

        self.grid_cells = []

        grid_buttons = []
        for row in range(GRID_SIZE):
            grid_row = []
            for col in range(GRID_SIZE):
                cell_button = Button("", TILE_SIZE)
                grid_row.append(cell_button)
                grid_buttons.append(cell_button)
            self.grid_cells.append(grid_row)

        # ThorPy Grid auto layout is buggy. Setting nx and ny manually, and setting them to n-1, seems to compensate.
        super().__init__(grid_buttons)
        self.sort_children(
            mode="grid",
            nx=GRID_SIZE - 1,
            ny=GRID_SIZE - 1,
            grid_gaps=GRID_GAPS
        )


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
