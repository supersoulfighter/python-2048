from typing import Tuple

from game.controller.commands.game.update_view import update_view
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def swap(model: GameModel, view: GameView, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    """Execute a swap powerup command between two positions."""

    if model.state != GameStates.PLAYING:
        return False

    # Validate positions
    val1 = model.grid.get_cell(*pos1)
    val2 = model.grid.get_cell(*pos2)
    if not _are_valid_positions(model, pos1, pos2, val1, val2):
        return False

    # Try to use the powerup
    if model.powerups.consume(PowerupType.SWAP):
        model.grid.save()
        model.score.save()
        # Perform the swap
        model.grid.set_cell(*pos1, val2)
        model.grid.set_cell(*pos2, val1)
        update_view(model, view)
        return True

    return False



def _are_valid_positions(model: GameModel, pos1: Tuple[int, int], pos2: Tuple[int, int], val1:int, val2:int) -> bool:
    """Check if the positions are valid for swapping."""

   # Don't allow swapping with self
    if pos1 == pos2:
        return False

    # Don't allow swapping with empty cells
    if val1 == 0 or val2 == 0:
        return False

    # Check bounds
    size = model.grid.size
    row1, col1 = pos1
    row2, col2 = pos2
    if not (0 <= row1 < size and 0 <= col1 < size and
            0 <= row2 < size and 0 <= col2 < size):
        return False

    return True
