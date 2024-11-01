from rubik import Rubik

class Solver(object):

    def __init__(self, rubik: Rubik):
        self.rubik = rubik
        self.move_counter = 0 # Number of moves

    def __is_solved__(self):
        for i in range(len(self.rubik.cube)):
            for j in range(len(self.rubik.cube[0])):
                if self.rubik.cube[i][j] != Rubik.CUBE[i][j]:
                    return False
        return True

    def solve(self):
        raise NotImplementedError("This method must be implemented in subclasses.")