from rubik import Rubik

class Solver(object):

    def __init__(self, rubik: Rubik):
        self.rubik = rubik
        self.moves = 0

    def solve(self):
        raise NotImplementedError("This method must be implemented in subclasses.")