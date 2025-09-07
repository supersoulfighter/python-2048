from enum import Enum, auto

class GameStates(Enum):
    """Possible states of the game."""
    PLAYING = auto()
    WON = auto()
    LOST = auto()
    ANIMATING = auto()
    SWAPPING = auto()
    DELETING = auto()
    QUITING = auto()
