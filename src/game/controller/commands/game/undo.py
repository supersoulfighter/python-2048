from typing import List, Tuple
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.model.powerups import PowerupType
from game.view.game_view import GameView


def undo(model: GameModel, view: GameView, target_value: int) -> bool:
    """Undo the last move."""
    if model.state != GameStates.PLAYING:
        return False

    if model.powerups.consume(PowerupType.UNDO):
        model.grid.restore()
        model.score.restore()
        return True

    return False
    
