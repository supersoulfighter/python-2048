from typing import List, Tuple

from game.controller.commands.game.activate_mode import activate_mode
from game.controller.commands.game.update_view import update_view
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView
from game.view.ui.game.cell import Cell


def delete(model: GameModel, view: GameView, cell:Cell=None) -> bool:
    """Handles all phases of deleting (activation, selection, etc.) so gets called multiple times per swap."""

    # Comes from click on powerup button
    if model.state == GameStates.PLAYING:
        # If user has earned powerups, can enter swapping mode
        if model.powerups.count(PowerupType.DELETE) > 0:
            activate_mode(model, view, GameStates.DELETING,True)
        else:
            return False

    # Clicked on cell while in mode
    elif model.state == GameStates.DELETING:
        # Click on powerup button again exits mode
        if cell is None:
            activate_mode(model, view, GameStates.DELETING, False)

        # Clicking on empty cell ignored
        elif cell.text == "":
            return False

        else:
            __perform_delete(model, view, int(cell.text))

    update_view(model, view)
    return True


def __perform_delete(model: GameModel, view: GameView, value:int) -> None:
    """Perform the delete."""
    model.powerups.consume(PowerupType.DELETE)
    model.grid.save()
    model.score.save()
    tiles = __find_tiles_with_value(model, value)
    for row, col in tiles:
        model.grid.set_cell(row, col, 0)
    activate_mode(model, view, GameStates.DELETING, False)


def __find_tiles_with_value(model: GameModel, value: int) -> List[Tuple[int, int]]:
    """Find all tiles with the given value."""
    tiles = []
    for row in range(model.grid.size):
        for col in range(model.grid.size):
            if model.grid.get_cell(row, col) == value:
                tiles.append((row, col))
    return tiles

