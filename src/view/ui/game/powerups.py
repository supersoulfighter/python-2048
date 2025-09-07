from typing import Dict

from pygame.event import post, Event
from pygame.image import load

from model.config import ViewEvents
from view.ui.lib.button import Button
from view.ui.lib.box import Box
from view.ui.lib.image import Image
from view.ui.theme import ContainerStyle
from view.ui.tokens import SELECTED_BORDER_WIDTH, POWERUP_BUTTON_SIZE, UNSELECTED_BORDER_WIDTH


class Powerups(Box):
    def __init__(self):

        self.buttons = {}
        self.powerup_active = None

        powerups = [ViewEvents.UNDO, ViewEvents.SWAP, ViewEvents.DELETE]
        for p in powerups:
            def onclick(powerup=p):
                post(Event(powerup.value))
            n = p.name.lower()
            img = Image(load(f"./assets/images/{n}.svg"))
            btn = Button("", POWERUP_BUTTON_SIZE, onclick)
            btn.add_child(img)
            self.buttons[n] = btn

        super().__init__([self.buttons[name] for name in self.buttons], ContainerStyle())
        self.sort_children("h")



    def update_powerups(self, powerups: Dict):
        for powerup_type, count in powerups.items():
            button = self.buttons.get(powerup_type.name.lower())

            if button:
                if self.powerup_active is None:
                    button.set_enabled(count > 0)
                    button.set_style_attr("border_thickness", UNSELECTED_BORDER_WIDTH)
                else:
                    if powerup_type == self.powerup_active:
                        button.set_style_attr("border_thickness", SELECTED_BORDER_WIDTH)
                        button.set_enabled(True)
                    else:
                        button.set_style_attr("border_thickness", UNSELECTED_BORDER_WIDTH)
                        button.set_enabled(False)
