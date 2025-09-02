from typing import List, Tuple
import random
from game.model.config import GRID_SIZE


class Grid:
    def __init__(self):
        self.size = GRID_SIZE
        self.cells = [[0] * self.size for _ in range(self.size)]
        self.moved_tiles: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []  # [(from_pos, to_pos), ...]
        self.merged_tiles: List[Tuple[Tuple[int, int], int]] = []  # [(pos, value), ...]
        self.previous_state = None  # For undo/redo
        self._spawn_initial_tiles()



    def save(self):
        """Save current state for undo."""
        self.previous_state = [row[:] for row in self.cells]



    def restore(self) -> bool:
        """Restore previous state for undo. Returns True if successful."""
        if not self.previous_state:
            return False
        self.cells = [row[:] for row in self.previous_state]
        self.moved_tiles.clear()
        self.merged_tiles.clear()
        return True
        


    def _spawn_initial_tiles(self):
        """Spawn two initial tiles when starting a new game."""
        for _ in range(2):
            self._spawn_new_tile()



    def _spawn_new_tile(self) -> bool:
        """Spawn a new tile (2 or 4) in a random empty cell."""
        empty_cells = self.get_empty_cells()
        if not empty_cells:
            return False
            
        row, col = random.choice(empty_cells)
        self.cells[row][col] = 2 if random.random() < 0.9 else 4
        return True
    


    def get_empty_cells(self) -> List[Tuple[int, int]]:
        """Return a list of (row, col) tuples for all empty cells."""
        empty = []
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col] == 0:
                    empty.append((row, col))
        return empty



    def get_cell(self, row: int, col: int) -> int:
        """Get the value of a cell at the given position."""
        return self.cells[row][col]
    
    
    
    def set_cell(self, row: int, col: int, value: int):
        """Set the value of a cell at the given position."""
        self.cells[row][col] = value



    def is_full(self) -> bool:
        """Check if the grid is full (no empty cells)."""
        return len(self.get_empty_cells()) == 0
    
    
    
    def copy(self) -> 'Grid':
        """Create a deep copy of the grid."""
        new_grid = Grid(self.size)
        new_grid.cells = [row[:] for row in self.cells]
        return new_grid



    def _get_farthest_position(self, row: int, col: int, direction: Tuple[int, int]) -> Tuple[int, int]:
        """Get the farthest valid position in the given direction."""
        dx, dy = direction
        while True:
            new_row = row + dx
            new_col = col + dy
            if not (0 <= new_row < self.size and 0 <= new_col < self.size):
                break
            if self.cells[new_row][new_col] != 0:
                break
            row, col = new_row, new_col
        return row, col
    
    
    
    def is_valid_move(self, direction: Tuple[int, int]) -> bool:
        """Check if moving in the given direction would change the grid."""
        dx, dy = direction
        for row in range(self.size):
            for col in range(self.size):
                if self.cells[row][col] != 0:
                    new_row, new_col = self._get_farthest_position(row, col, (dx, dy))
                    if new_row != row or new_col != col:
                        return True
                    # Check for possible merge
                    next_row, next_col = new_row + dx, new_col + dy
                    if (0 <= next_row < self.size and 
                        0 <= next_col < self.size and 
                        self.cells[next_row][next_col] == self.cells[row][col]):
                        return True
        return False



    def make_move(self, direction: Tuple[int, int]) -> Tuple[bool, int]:
        """Make a move in the given direction. Returns (moved, points_gained)."""
        if not self.is_valid_move(direction):
            return False, 0
            
        self.moved_tiles.clear()
        self.merged_tiles.clear()
        dx, dy = direction
        points_gained = 0
        
        # Determine traversal order
        rows = range(self.size)
        cols = range(self.size)
        if dx > 0: rows = range(self.size - 1, -1, -1)
        if dy > 0: cols = range(self.size - 1, -1, -1)
        
        moved = False
        merged = [[False] * self.size for _ in range(self.size)]
        
        for i in rows:
            for j in cols:
                if self.cells[i][j] == 0:
                    continue
                    
                current_val = self.cells[i][j]
                new_i, new_j = self._get_farthest_position(i, j, (dx, dy))
                
                # Try to merge
                next_i, next_j = new_i + dx, new_j + dy
                if (0 <= next_i < self.size and 
                    0 <= next_j < self.size and 
                    self.cells[next_i][next_j] == current_val and 
                    not merged[next_i][next_j]):
                    # Merge tiles
                    self.cells[next_i][next_j] *= 2
                    self.cells[i][j] = 0
                    merged[next_i][next_j] = True
                    points_gained += self.cells[next_i][next_j]
                    self.moved_tiles.append(((i, j), (next_i, next_j)))
                    self.merged_tiles.append(((next_i, next_j), self.cells[next_i][next_j]))
                    moved = True
                else:
                    # Move tile
                    if (new_i, new_j) != (i, j):
                        self.cells[new_i][new_j] = current_val
                        self.cells[i][j] = 0
                        self.moved_tiles.append(((i, j), (new_i, new_j)))
                        moved = True
        
        if moved:
            self._spawn_new_tile()
                
        return moved, points_gained
    

    
