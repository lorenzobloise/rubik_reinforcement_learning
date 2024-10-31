from solvers.solver import Solver
from rubik import Rubik
import utils

class LayerByLayer(Solver):

    def __init__(self, rubik: Rubik):
        super().__init__(rubik)

    def solve(self):
        self.__solve_first_layer__()
        self.__solve_second_layer__()
        self.__solve_third_layer__()
        self.__rotate_until_solution__()

    # FIRST LAYER

    def __solve_first_layer__(self):
        self.rubik.face = utils.WHITE
        self.__make_white_cross__()
        self.__fix_white_cross_edges__()
        self.__fix_white_cross_corners__()

    def __make_white_cross__(self):
        pass

    def __fix_white_cross_edges__(self):
        pass

    def __fix_white_cross_corners__(self):
        pass

    # SECOND LAYER

    def __solve_second_layer__(self):
        while not self.__is_second_layer_solved__():
            pass

    def __is_second_layer_solved__(self):
        pass

    # THIRD LAYER

    def __solve_third_layer__(self):
        self.__make_yellow_cross__()
        self.__fix_yellow_cross_edges__()
        self.__fix_yellow_cross_corners__()

    def __make_yellow_cross__(self):
        pass

    def __fix_yellow_cross_edges__(self):
        pass

    def __fix_yellow_cross_corners__(self):
        pass

    # FINAL STEPS

    def __rotate_until_solution__(self):
        pass