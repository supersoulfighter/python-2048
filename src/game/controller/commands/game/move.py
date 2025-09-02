from typing import Tuple

from game.controller.commands.game.update_view import update_view
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.view.game_view import GameView



def move(model: GameModel, view: GameView, direction: Tuple[int, int]) -> bool:
    """Execute a move command in the given direction."""
    
    # Check if move is allowed
    if model.state != GameStates.PLAYING:
        return False
        
    # Make the move
    model.grid.save()
    model.score.save()
    moved, points = model.grid.make_move(direction)
    if not moved:
        return False
        
    # Update game state
    model.score.update(points)

    # Check for win condition
    for i in range(model.grid.size):
        for j in range(model.grid.size):
            if model.grid.get_cell(i, j) == 2048:
                model.state = GameStates.WON
                break

    # Check for game over
    if not any(model.grid.is_valid_move(d) for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]):
        model.state = GameStates.LOST

    # Update view with current state
    update_view(model, view)
    return True
