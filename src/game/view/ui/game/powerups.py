from typing import Dict

from pygame.event import post, Event

from game.model.config import *
from game.view.ui.button import Button
from game.view.ui.box import Box
from game.view.ui.image import Image
from game.view.ui.theme import ContainerStyle


class Powerups(Box):
    def __init__(self):

        self.buttons = {}

        powerups = [ViewEvents.UNDO, ViewEvents.SWAP, ViewEvents.DELETE]
        for p in powerups:
            n = p.name.lower()
            img = Image(pygame.image.load(f"./assets/images/{n}.svg"))
            btn = Button("", (48,48), lambda: post(Event(p.value)))
            btn.add_child(img)
            self.buttons[n] = btn

        super().__init__([self.buttons[name] for name in self.buttons], ContainerStyle())
        self.sort_children("h")



    def update_powerups(self, powerups: Dict):
        for name, powerup in powerups.items():
            button = self.buttons.get(name)
            if button:
                button.set_enabled(powerup.active)
