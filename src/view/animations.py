"""Animation utilities for 2048 game."""
from typing import Dict, Optional, Tuple

import tween


class AnimationManager:
    def __init__(self):
        self.animations = []
        self.callbacks = {}
        self.positions = {}
    
    def create_movement(self, start_pos: Tuple[float, float], 
                       end_pos: Tuple[float, float],
                       duration: float = 0.15,
                       on_complete: Optional[callable] = None):
        """Create a movement animation from start to end position."""
        pos = {'x': start_pos[0], 'y': start_pos[1]}
        self.positions[id(pos)] = pos
        
        # Create x animation
        tx = tween.to(pos, 'x', end_pos[0], duration, 'easeOutCubic')
        # Create y animation
        ty = tween.to(pos, 'y', end_pos[1], duration, 'easeOutCubic')
        if on_complete:
            self.callbacks[ty] = on_complete
        self.animations.append(ty)
        return ty
    
    def create_merge(self, scale_center: Tuple[float, float],
                    duration: float = 0.1,
                    on_complete: Optional[callable] = None):
        """Create a merge animation that scales up then down."""
        scale = {'value': 1.0}
        self.positions[id(scale)] = scale
        
        # Scale up
        t1 = tween.to(scale, 'value', 1.2, duration/2, 'easeOutCubic')
        t2 = tween.to(scale, 'value', 1.0, duration / 2, 'easeInCubic')
        t1.chain(t2)
        if on_complete:
            self.callbacks[t2] = on_complete
        self.animations.append(t1)
        return t1
    
    def create_spawn(self, pos: Tuple[float, float],
                    duration: float = 0.15,
                    on_complete: Optional[callable] = None) -> Dict[str, float]:
        """Create a spawn animation that scales from 0 to 1."""
        scale = {'value': 0.0}
        self.positions[id(scale)] = scale
        
        # Scale from 0 to 1
        t = tween.to(scale, 'value', 1.0, duration, 'easeOutCubic')
        if on_complete:
            t.on_complete(on_complete)
        self.animations.append(t)
        return scale
    
    def update(self, dt: float):
        """Update all running animations."""
        tween.update(dt)
        # Clean up finished animations
        self.animations = [a for a in self.animations if not a.complete]
        # Clean up positions for finished animations
        for pos_id in list(self.positions.keys()):
            if not any(id(a.obj) == pos_id for a in self.animations):
                del self.positions[pos_id]
    
    def clear(self):
        """Clear all animations."""
        self.animations.clear()
        self.callbacks.clear()
