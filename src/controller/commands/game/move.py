from typing import Tuple

from controller.commands.game.earn import earn
from controller.commands.game.update_view import update_view
from model.game_model import GameModel
from model.game_states import GameStates
from view.game_view import GameView



def move(model: GameModel, view: GameView, direction: Tuple[int, int]) -> bool:
    """Execute a move command in the given direction."""
    
    # Check if move is allowed
    if model.state != GameStates.PLAYING:
        return False
        
    # Make the move
    model.grid.save()
    model.score.save()
    moved, points, highest = model.grid.make_move(direction)
    if not moved:
        return False

    # Check for win condition
    for i in range(model.grid.size):
        for j in range(model.grid.size):
            if model.grid.get_cell(i, j) == 2048:
                model.state = GameStates.WON
                return True

    # Check for game over
    if not any(model.grid.is_valid_move(d) for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]):
        model.state = GameStates.LOST
        return True

    # Update game state
    # TODO: This should be a list of all merges (points scored) so that multiple can be earned in one turn
    earn(model, highest)
    model.score.update(points)
    update_view(model, view)
    return True
