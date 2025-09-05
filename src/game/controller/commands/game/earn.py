from game.model.config import PowerupType
from game.model.game_model import GameModel


def earn(model: GameModel, points:int):
    """Check if any powerups were earned"""
    if points > 8:
        model.powerups.earn(PowerupType.DELETE, 1)
    elif points > 4:
        model.powerups.earn(PowerupType.SWAP, 1)
    elif points > 2:
        model.powerups.earn(PowerupType.UNDO, 1)

