from controller.commands.game.activate_mode import activate_mode
from controller.commands.game.update_view import update_view
from model.game_model import GameModel
from model.game_states import GameStates
from model.powerups import PowerupType
from view.game_view import GameView
from view.ui.game.cell import Cell


def swap(model: GameModel, view: GameView, cell:Cell=None) -> bool:
    """Handles all phases of swapping (activation, selection, etc.) so gets called multiple times per swap."""

    # Comes from click on powerup button
    if model.state == GameStates.PLAYING:
        # If user has earned powerups, can enter swapping mode
        if model.powerups.count(PowerupType.SWAP) > 0:
            activate_mode(model, view, GameStates.SWAPPING,True)
        else:
            return False

    # Clicked on cell while in mode
    elif model.state == GameStates.SWAPPING:
        # Click on powerup button again exits mode
        if cell is None:
            activate_mode(model, view, GameStates.SWAPPING, False)

        # Clicking on empty cell ignored
        elif cell.text == "":
            return False

        # Unselect by clicking same cell again
        elif cell in view.grid.selected_cells:
            cell.select(False)
            view.grid.selected_cells.remove(cell)

        else:
            # Select
            cell.select(True)
            view.grid.selected_cells.append(cell)

            # Can swap if two cells selected
            if len(view.grid.selected_cells) > 1:
                __perform_swap(model, view)

    update_view(model, view)
    return True



def __perform_swap(model: GameModel, view: GameView) -> None:
    """Perform the swap."""
    model.powerups.consume(PowerupType.SWAP)
    model.grid.save()
    model.score.save()
    cell1 = view.grid.selected_cells[0]
    cell2 = view.grid.selected_cells[1]
    val1 = int(cell1.text)
    val2 = int(cell2.text)
    model.grid.set_cell(cell1.row, cell1.col, val2)
    model.grid.set_cell(cell2.row, cell2.col, val1)
    cell1.select(False)
    cell2.select(False)
    view.grid.selected_cells.clear()
    activate_mode(model, view, GameStates.SWAPPING, False)
