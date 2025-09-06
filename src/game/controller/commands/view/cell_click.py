from game.controller.commands.game.delete import delete
from game.controller.commands.game.swap import swap
from game.view.game_view import GameView
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.view.ui.game.cell import Cell


def cell_click(model: GameModel, view: GameView, cell:Cell) -> bool:
    if model.state == GameStates.SWAPPING:
        swap(model, view, cell)

    elif model.state == GameStates.DELETING:
        delete(model, view, cell)

    return True
