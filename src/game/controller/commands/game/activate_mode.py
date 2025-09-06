from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView

modes = {
    GameStates.SWAPPING: PowerupType.SWAP,
    GameStates.DELETING: PowerupType.DELETE
}


def activate_mode(model: GameModel, view: GameView, state:GameStates, activate:bool) -> None:
    """Some powerups enter a mode in the UI where other input is blocked."""

    if activate:
        view.powerups.powerup_active = modes[state]
        model.state = state
    else:
        view.powerups.powerup_active = None
        model.state = GameStates.PLAYING
        if len(view.grid.selected_cells) > 0:
            for cell in view.grid.selected_cells:
                cell.select(False)
            view.grid.selected_cells.clear()

