import pygame
from typing import List

from game.controller.commands.game.update_view import update_view
from game.model.game_model import GameModel
from game.model.game_states import GameStates
from game.view.game_view import GameView
from game.controller.commands.view.keyup import keyup
from game.controller.commands.game.swap import swap
from game.controller.commands.game.undo import undo
from game.controller.commands.game.delete import delete
from game.model.config import ViewEvents



class GameController:
    
    def __init__(self, model: GameModel, view: GameView):
        self.model = model
        self.view = view
        update_view(model, view)


    def update(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            t = event.type

            if t == pygame.QUIT:
                self.model.state = GameStates.QUITING

            elif t == pygame.KEYUP:
                keyup(self.model, self.view, event.key)

            elif t == ViewEvents.SWAP.value:
                swap(self.model, self.view, event.pos)

            elif t == ViewEvents.UNDO.value:
                undo(self.model, self.view)

            elif t == ViewEvents.DELETE.value:
                delete(self.model, self.view)
            
            # Apparently, Event has an undocumented pos attribute
            # https://www.geeksforgeeks.org/python/pygame-event-handling/

