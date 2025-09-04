from game.view.ui.box import Box
from game.view.ui.label_group import LabelGroup
from game.view.ui.text import Text
from game.view.ui.theme import ScoreValueStyle, ContainerStyle


class Score(Box):
    def __init__(self):

        self.score_current = LabelGroup("SCORE", Text("0", ScoreValueStyle()))
        self.score_best = LabelGroup("BEST", Text("0", ScoreValueStyle()))
        self.score_current.sort_children("v", gap=0)
        self.score_best.sort_children("v", gap=0)

        super().__init__([self.score_current, self.score_best], ContainerStyle())
        self.sort_children("h")



    def update_score(self, score: int, high_score: int):
        self.score_current.element.set_text(f"{score}")
        self.score_best.element.set_text(f"{high_score}")

