from model.config import PowerupType
from model.game_model import GameModel


def earn(model: GameModel, points:int):
    """Check if any powerups were earned"""
    if points == 512:
        model.powerups.earn(PowerupType.DELETE, 1)
    elif points == 256:
        model.powerups.earn(PowerupType.SWAP, 1)
    elif points == 128:
        model.powerups.earn(PowerupType.UNDO, 1)

