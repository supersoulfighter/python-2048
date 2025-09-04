import json
import os


class Score:
    def __init__(self):
        self.current = 0
        self.high_score = self._load_high_score()
        self.multiplier = 1
        self.previous_state = None  # For undo/redo



    def save(self):
        """Save current state for undo."""
        self.previous_state = {
            'current': self.current,
            'multiplier': self.multiplier
        }



    def restore(self) -> bool:
        """Restore previous state for undo. Returns True if successful."""
        if not self.previous_state:
            return False
        self.current = self.previous_state['current']
        self.multiplier = self.previous_state['multiplier']
        return True



    def _load_high_score(self) -> int:
        """Load the high score from persistent storage."""
        try:
            if os.path.exists('high_score.json'):
                with open('high_score.json', 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except:
            pass
        return 0



    def _save_high_score(self):
        """Save the high score to persistent storage."""
        try:
            with open('high_score.json', 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except:
            pass



    def update(self, points: int):
        """Update the score with the given points, applying any active multiplier."""
        points *= self.multiplier
        self.current += points
        if self.current > self.high_score:
            self.high_score = self.current
            self._save_high_score()
            



    def set_multiplier(self, value: int):
        """Set the score multiplier (e.g., for double score powerup)."""
        self.multiplier = value
