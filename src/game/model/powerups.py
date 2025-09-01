from typing import Dict
from enum import Enum, auto



class PowerUpType(Enum):
    """Types of powerups available in the game."""
    UNDO = auto()
    SWAP = auto()  # Swap Two Tiles
    DELETE = auto()  # Delete by number
    TELEPORT = auto()  # Teleport a Tile
    ROTATE = auto()  # Rotate Outer Ring
    BOMB = auto()  # Delete tile and all adjacent tiles



class PowerUpManager:
    """Manages the counts of available powerups.
    Powerups are earned at score thresholds and spent when used."""
    
    def __init__(self):
        # Initialize all powerups with 0 count
        self.counts: Dict[PowerUpType, int] = {p: 0 for p in PowerUpType}
        self.previous_state = None



    def save_state(self):
        """Save current state for undo."""
        self.previous_state = self.counts.copy()



    def restore_state(self) -> bool:
        """Restore previous state for undo. Returns True if successful."""
        if not self.previous_state:
            return False
        self.counts = self.previous_state.copy()
        return True



    def get_count(self, powerup_type: PowerUpType) -> int:
        """Get the number of available uses for a powerup."""
        return self.counts[powerup_type]



    def add_powerup(self, powerup_type: PowerUpType, count: int = 1):
        """Add powerups of the specified type."""
        self.counts[powerup_type] += count



    def use_powerup(self, powerup_type: PowerUpType) -> bool:
        """Try to use a powerup. Returns True if successful."""
        if self.counts[powerup_type] > 0:
            self.counts[powerup_type] -= 1
            return True
        return False



    def activate_powerup(self, name: str, current_state: GameStates) -> Tuple[bool, GameStates]:
        """Activate a powerup. Returns (success, new_state)."""
        if current_state not in (GameStates.PLAYING, GameStates.WON):
            return False, current_state
            
        powerup = self.powerups.get(name)
        if not powerup or not powerup.active or powerup.cooldown > 0:
            return False, current_state
            
        new_state = current_state
        
        if name == 'shuffle':
            self.grid.shuffle()
            powerup.cooldown = 10
            new_state = GameStates.SWAPPING
            
        elif name == 'remove_tile':
            if self.grid.remove_lowest_tile():
                powerup.cooldown = 15
                new_state = GameStates.DELETING
            else:
                return False, current_state
                
        elif name == 'double_score':
            powerup.active = True
            powerup.duration = 5
            powerup.cooldown = 20
            self.score_manager.set_multiplier(2)
            
        return True, new_state
    



    def update_powerups(self):
        """Update powerup cooldowns and durations."""
        for name, powerup in self.powerups.items():
            if powerup.cooldown > 0:
                powerup.cooldown -= 1
            if powerup.duration is not None:
                if powerup.duration > 0:
                    powerup.duration -= 1
                else:
                    powerup.active = False
                    if name == 'double_score':
                        self.score_manager.set_multiplier(1)
