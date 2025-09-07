import pygame
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController
from model.game_states import GameStates



class Game:
    def __init__(self):
        pygame.init()
        self.model = GameModel()
        self.view = GameView()
        self.controller = GameController(self.model, self.view)

    def run(self):
        while self.model.state != GameStates.QUITING:
            events = pygame.event.get()
            self.model.update()          
            self.controller.update(events)
            self.view.render(events)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
