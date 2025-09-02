from game.model.game_model import GameModel
from game.view.game_view import GameView


def update_view(model: GameModel, view: GameView):
    """Update view with current state"""
    view.update_score(model.score.current, model.score.high_score)
    view.update_grid(model.grid.cells)
    view.update_powerups(model.powerups.counts)

