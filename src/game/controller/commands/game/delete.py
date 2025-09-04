from typing import List, Tuple

from game.controller.commands.game.update_view import update_view
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def delete(model: GameModel, view: GameView, target_value: int) -> bool:
    """Delete tiles by number."""

    if model.state != GameStates.PLAYING:
        return False

    # Find all tiles with target value
    tiles_to_delete = _find_tiles_with_value(model, target_value)
    if not tiles_to_delete:
        return False
    
    # Try to use the powerup
    if model.powerups.consume(PowerupType.DELETE):
        model.grid.save()
        model.score.save()
        # Delete the first tile found
        row, col = tiles_to_delete[0]
        model.grid.set_cell(row, col, 0)
        update_view(model, view)
        return True

    return False



def _find_tiles_with_value(model: GameModel, value: int) -> List[Tuple[int, int]]:
    """Find all tiles with the given value."""
    tiles = []
    for row in range(model.grid.size):
        for col in range(model.grid.size):
            if model.grid.get_cell(row, col) == value:
                tiles.append((row, col))
    return tiles
