from enum import Enum, auto



class GameStates(Enum):
    """Enum representing the possible states of the game."""
    PLAYING = auto()    # Normal gameplay
    WON = auto()       # Player has reached 2048
    LOST = auto()      # No more valid moves
    ANIMATING = auto() # Tiles are currently animating
    SWAPPING = auto()  # Tiles are being swapped (shuffle)
    DELETING = auto()  # Tile is being removed (remove_tile powerup)
    QUITING = auto()   # Game is quitting
