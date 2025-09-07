from typing import List, Tuple
from game.model.game_state import GameModel
from model.game_states import GameStates
from model.powerups import PowerupType
from view.game_view import GameView


def bomb(model: GameModel, view: GameView, center_pos: Tuple[int, int]) -> bool:
    """Execute a bomb powerup command to clear a tile and its adjacent tiles."""
    # Save current state
    model.grid.save_state()
    model.powerup_manager.save_state()
    
    # Try to use the powerup
    if not model.powerup_manager.use_powerup(PowerupType.BOMB):
        return False
        
    # Get positions to clear
    positions = _get_bomb_positions(model, center_pos)
    if not positions:
        model.powerup_manager.restore_state()
        return False
        
    # Clear all positions and create animations
    for pos in positions:
        if model.grid.get_cell(*pos) != 0:
            model.grid.set_cell(*pos, 0)
            view.create_merge_animation(pos, 0)
    
    model.state = GameStates.DELETING
    view.update_powerups(model.powerup_manager.counts)
    return True



def _get_bomb_positions(model: GameModel, center_pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Get all positions affected by the bomb (center + adjacent)."""
    row, col = center_pos
    size = model.grid.size
    
    # Check bounds
    if not (0 <= row < size and 0 <= col < size):
        return []
        
    # Center must have a tile
    if model.grid.get_cell(row, col) == 0:
        return []
        
    # Get all positions to clear (center + adjacent)
    positions = [(row, col)]  # Center
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:  # Adjacent
        r, c = row + dr, col + dc
        if 0 <= r < size and 0 <= c < size:
            positions.append((r, c))
            
    return positions
