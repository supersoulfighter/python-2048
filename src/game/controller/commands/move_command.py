from typing import Tuple
from game.model.game_state import GameState
from game.model.game_states import GameStates
from game.view.game_view import GameView


def execute(model: GameState, view: GameView, direction: Tuple[int, int]) -> bool:
    """Execute a move command in the given direction."""
    # Save current state
    model.grid.save_state()
    model.score_manager.save_state()
    
    # Check if move is allowed
    if model.state not in (GameStates.PLAYING, GameStates.WON):
        return False
        
    # Make the move
    moved, points = model.grid.make_move(direction)
    if not moved:
        return False
        
    # Update game state
    model.state = GameStates.ANIMATING
    model.score_manager.update(points)

    # Check for win condition
    for i in range(model.grid.size):
        for j in range(model.grid.size):
            if model.grid.get_cell(i, j) == 2048:
                model.state = GameStates.WON
                break

    # Check for game over
    if not any(model.grid.is_valid_move(d) for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]):
        model.state = GameStates.LOST

    # Create animations
    for from_pos, to_pos in model.grid.moved_tiles:
        view.create_tile_animation(from_pos, to_pos)
    
    for pos, value in model.grid.merged_tiles:
        view.create_merge_animation(pos, value)
        
    view.update_score(model.score_manager.current, model.score_manager.high_score)
    return True


def undo(model: GameState, view: GameView) -> bool:
    """Undo a move command."""
    # Restore state from model classes
    grid_restored = model.grid.restore_state()
    score_restored = model.score_manager.restore_state()
    
    if grid_restored and score_restored:
        view.update_score(model.score_manager.current, model.score_manager.high_score)
        return True
    return False
