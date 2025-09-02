from typing import Tuple
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def swap(model: GameModel, view: GameView, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    """Execute a swap powerup command between two positions."""
    # Save current state
    model.grid.save_state()
    model.powerup_manager.save_state()
    
    # Try to use the powerup
    if not model.powerup_manager.use_powerup(PowerupType.SWAP):
        return False
        
    # Validate positions
    if not _are_valid_positions(model, pos1, pos2):
        model.powerup_manager.restore_state()
        return False
        
    # Get values at positions
    val1 = model.grid.get_cell(*pos1)
    val2 = model.grid.get_cell(*pos2)
    
    # Don't allow swapping with empty cells
    if val1 == 0 or val2 == 0:
        model.powerup_manager.restore_state()
        return False
        
    # Perform the swap
    model.grid.set_cell(*pos1, val2)
    model.grid.set_cell(*pos2, val1)
    
    # Create swap animation
    view.create_tile_animation(pos1, pos2)
    view.create_tile_animation(pos2, pos1)
    
    model.state = GameStates.SWAPPING
    view.update_grid(model.grid)
    view.update_powerups(model.powerup_manager.counts)
    return True



def _are_valid_positions(model: GameModel, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    """Check if the positions are valid for swapping."""
    size = model.grid.size
    row1, col1 = pos1
    row2, col2 = pos2
    
    # Check bounds
    if not (0 <= row1 < size and 0 <= col1 < size and
            0 <= row2 < size and 0 <= col2 < size):
        return False
        
    # Don't allow swapping with self
    if pos1 == pos2:
        return False
        
    return True
