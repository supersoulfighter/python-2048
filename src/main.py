import pygame
import thorpy
from game.model.game_state import GameState
from game.view.game_view import GameView
from game.controller.game_controller import GameController

class Game:
    def __init__(self):
        pygame.init()
       
        # Initialize MVC components
        self.model = GameState()
        self.view = GameView(screen)
        self.controller = GameController(self.model, self.view)
        
        self.running = True

    def run(self):
        while self.model.state != GameStates.QUITING:
            self.model.update()          
            self.controller.update()
            self.view.render()
            
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
