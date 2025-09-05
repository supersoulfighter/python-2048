from typing import Dict

from pygame.event import post, Event
from pygame.image import load

from game.model.config import ViewEvents
from game.view.ui.button import Button
from game.view.ui.box import Box
from game.view.ui.image import Image
from game.view.ui.theme import ContainerStyle


class Powerups(Box):
    def __init__(self):

        self.buttons = {}

        powerups = [ViewEvents.UNDO, ViewEvents.SWAP, ViewEvents.DELETE]
        for p in powerups:
            def onclick(powerup=p):
                post(Event(powerup.value))
            n = p.name.lower()
            img = Image(load(f"./assets/images/{n}.svg"))
            btn = Button("", (48,48), onclick)
            btn.add_child(img)
            self.buttons[n] = btn

        super().__init__([self.buttons[name] for name in self.buttons], ContainerStyle())
        self.sort_children("h")



    def update_powerups(self, powerups: Dict):
        for powerup_type, count in powerups.items():
            button = self.buttons.get(powerup_type.name.lower())
            if button:
                button.set_enabled(count > 0)
