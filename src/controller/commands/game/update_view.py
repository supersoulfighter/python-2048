from model.game_model import GameModel
from view.game_view import GameView


def update_view(model: GameModel, view: GameView):
    """Update view with current state"""
    view.score.update_score(model.score.current, model.score.high_score)
    view.grid.update_grid(model.grid.cells)
    view.powerups.update_powerups(model.powerups.counts)

