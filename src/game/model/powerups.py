from typing import Dict
from game.model.config import PowerupType



class Powerups:
    """Manages the counts of available powerups.
    Powerups are earned at score thresholds and spent when used."""
    
    def __init__(self):
        # Initialize all powerups with 0 count
        self.counts: Dict[PowerupType, int] = {p: 0 for p in PowerupType}



    def earn(self, powerup_type: PowerupType, count: int = 1):
        """Add powerups of the specified type."""
        self.counts[powerup_type] += count



    def consume(self, powerup_type: PowerupType) -> bool:
        """Try to use a powerup. Returns True if successful."""
        if self.counts[powerup_type] > 0:
            self.counts[powerup_type] -= 1
            return True
        return False
