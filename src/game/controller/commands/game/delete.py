from typing import List, Tuple
from game.model.game_state import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def delete(model: GameModel, view: GameView, target_value: int) -> bool:
    """Execute a delete powerup command for a specific tile value."""
    # Save current state
    model.grid.save_state()
    model.powerup_manager.save_state()
    
    # Try to use the powerup
    if not model.powerup_manager.use_powerup(PowerupType.DELETE):
        return False
        
    # Find all tiles with target value
    tiles_to_delete = _find_tiles_with_value(model, target_value)
    if not tiles_to_delete:
        model.powerup_manager.restore_state()
        return False
        
    # Delete the first tile found
    row, col = tiles_to_delete[0]
    model.grid.set_cell(row, col, 0)
    
    # Create delete animation
    view.create_merge_animation((row, col), 0)
    
    model.state = GameStates.DELETING
    view.update_powerups(model.powerup_manager.counts)
    return True


def _find_tiles_with_value(model: GameModel, value: int) -> List[Tuple[int, int]]:
    """Find all tiles with the given value."""
    tiles = []
    for row in range(model.grid.size):
        for col in range(model.grid.size):
            if model.grid.get_cell(row, col) == value:
                tiles.append((row, col))
    return tiles
