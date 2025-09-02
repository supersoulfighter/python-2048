from typing import Tuple
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def teleport(model: GameModel, view: GameView, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> bool:
    """Execute a teleport powerup command to move a tile to an empty cell."""
    # Save current state
    model.grid.save()
    model.powerups.save_state()
    
    # Try to use the powerup
    if not model.powerups.consume(PowerupType.TELEPORT):
        return False
        
    # Validate positions
    if not _are_valid_positions(model, from_pos, to_pos):
        model.powerups.restore_state()
        return False
        
    # Get value at source position
    value = model.grid.get_cell(*from_pos)
    
    # Clear source cell and set destination cell
    model.grid.set_cell(*from_pos, 0)
    model.grid.set_cell(*to_pos, value)
    
    # Create teleport animation
    view.create_tile_animation(from_pos, to_pos)
    
    model.state = GameStates.SWAPPING
    view.update_powerups(model.powerups.counts)
    return True



def _are_valid_positions(model: GameModel, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> bool:
    """Check if the positions are valid for teleporting."""
    size = model.grid.size
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    
    # Check bounds
    if not (0 <= from_row < size and 0 <= from_col < size and
            0 <= to_row < size and 0 <= to_col < size):
        return False
        
    # Source must have a tile and destination must be empty
    if (model.grid.get_cell(from_row, from_col) == 0 or
        model.grid.get_cell(to_row, to_col) != 0):
        return False
        
    return True
