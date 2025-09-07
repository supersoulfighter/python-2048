from view.game_view import GameView
from model.game_model import GameModel
from model.game_states import GameStates
from controller.commands.game.move import move
from model.config import DIRECTION_KEYS



def keyup(model: GameModel, view: GameView, key:int) -> bool:
    if model.state != GameStates.PLAYING:
        return False

    if key in DIRECTION_KEYS:
        move(model, view, DIRECTION_KEYS[key])
        return True

    return False
