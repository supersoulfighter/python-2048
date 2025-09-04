from typing import List, Tuple
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def rotate(model: GameModel, view: GameView) -> bool:
    """Execute a rotate powerup command to rotate the outer ring clockwise."""
    # Save current state
    model.grid.save_state()
    model.powerup_manager.save_state()
    
    # Try to use the powerup
    if not model.powerup_manager.use_powerup(PowerupType.ROTATE):
        return False
        
    size = model.grid.size
    if size < 3:  # Need at least a 3x3 grid to have an outer ring
        model.powerup_manager.restore_state()
        return False
        
    # Get the outer ring positions and values
    ring = _get_outer_ring(model)
    values = [val for _, _, val in ring]
    values = [values[-1]] + values[:-1]  # Rotate right
    
    # Set new values and create animations
    for i, (row, col, _) in enumerate(ring):
        new_val = values[i]
        if new_val != model.grid.get_cell(row, col):
            model.grid.set_cell(row, col, new_val)
            # Create animation from previous position to new position
            prev_pos = ring[i-1][0:2] if i > 0 else ring[-1][0:2]
            view.create_tile_animation(prev_pos, (row, col))
    
    model.state = GameStates.SWAPPING
    view.update_powerups(model.powerup_manager.counts)
    return True



def _get_outer_ring(model: GameModel) -> List[Tuple[int, int, int]]:
    """Get positions and values of the outer ring tiles."""
    size = model.grid.size
    ring = []
    
    # Top row
    for col in range(size):
        ring.append((0, col, model.grid.get_cell(0, col)))
        
    # Right column (except top)
    for row in range(1, size):
        ring.append((row, size-1, model.grid.get_cell(row, size-1)))
        
    # Bottom row (except right)
    for col in range(size-2, -1, -1):
        ring.append((size-1, col, model.grid.get_cell(size-1, col)))
        
    # Left column (except bottom and top)
    for row in range(size-2, 0, -1):
        ring.append((row, 0, model.grid.get_cell(row, 0)))
        
    return ring
