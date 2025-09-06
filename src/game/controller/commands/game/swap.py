from game.controller.commands.game.update_view import update_view
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView
from game.view.ui.game.cell import Cell


def swap(model: GameModel, view: GameView, cell:Cell=None) -> bool:
    """Handles all phases of swapping (activation, selection, etc.) so gets called multiple times per swap."""

    # Comes from click on swap button
    if model.state == GameStates.PLAYING:
        # If user has swap powerups, can enter swapping mode
        if model.powerups.count(PowerupType.SWAP) > 0:
            __activate_swap_mode(model, view, True)
        else:
            return False

    # Clicked on cell while in swap mode
    elif model.state == GameStates.SWAPPING:
        # Click on swap button again exits swapping mode
        if cell is None:
            __activate_swap_mode(model, view, False)

        # Don't allow swapping with empty cells
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



def __activate_swap_mode(model: GameModel, view: GameView, activate:bool) -> None:
    """Activate swap mode."""
    if activate:
        view.powerups.powerup_active = PowerupType.SWAP
        model.state = GameStates.SWAPPING
    else:
        view.powerups.powerup_active = None
        model.state = GameStates.PLAYING
        if len(view.grid.selected_cells) > 0:
            for cell in view.grid.selected_cells:
                cell.select(False)
            view.grid.selected_cells.clear()



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
    __activate_swap_mode(model, view, False)