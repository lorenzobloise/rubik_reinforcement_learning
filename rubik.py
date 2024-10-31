import random
import utils
import copy

class Rubik(object):

    class Orientation(object):

        def __init__(self, front, top):
            self.front = front
            self.top = top
            self.__infer_other_faces__()

        def __infer_other_faces__(self):
            other_faces = utils.CONFIGURATIONS[(self.front, self.top)]
            self.back = other_faces[0]
            self.bottom = other_faces[1]
            self.left = other_faces[2]
            self.right = other_faces[3]

        def __str__(self):
            return f"- Front: {self.front},\n- Top: {self.top},\n- Back: {self.back},\n- Bottom: {self.bottom},\n- Left: {self.left},\n- Right: {self.right}"

    def __init__(self):
        self.cube = [
            [[utils.WHITE for _ in range(3)] for _ in range(3)],
            [[utils.RED for _ in range(3)] for _ in range(3)],
            [[utils.GREEN for _ in range(3)] for _ in range(3)],
            [[utils.ORANGE for _ in range(3)] for _ in range(3)],
            [[utils.BLUE for _ in range(3)] for _ in range(3)],
            [[utils.YELLOW for _ in range(3)] for _ in range(3)]
        ]
        self.orientation = self.Orientation(utils.RED, utils.WHITE)
        #self.__scramble__()

    def __str__(self):
        return f"--------------------\nCube:\n{self.__str_cube__()}\n--------------------\nOrientation:\n{self.orientation}"

    def __str_cube__(self): # TODO
        s = ""
        """
        SOLVED CUBE:                                            _________
                    0   0   0                                  |         |
                    0   0   0                                  |    U    |
                    0   0   0                        __________|_________|__________
        2   2   2   1   1   1   4   4   4           |          |         |          |
        2   2   2   1   1   1   4   4   4           |     L    |    F    |     R    |
        2   2   2   1   1   1   4   4   4           |__________|_________|__________|
                    5   5   5                                  |         |          
                    5   5   5                                  |    D    |
                    5   5   5                                  |_________|
                    3   3   3                                  |         |
                    3   3   3                                  |    B    |
                    3   3   3                                  |_________|      
        """
        s += '\t\t\t'
        s += f"{self.cube[0][2][2]}\t{self.cube[0][2][1]}\t{self.cube[0][2][0]}"
        s += '\t\t\t\t\t\t\n'
        s += '\t\t\t'
        s += f"{self.cube[0][1][2]}\t{self.cube[0][1][1]}\t{self.cube[0][1][0]}"
        s += '\t\t\t\t\t\t\n'
        s += '\t\t\t'
        s += f"{self.cube[0][0][2]}\t{self.cube[0][0][1]}\t{self.cube[0][0][0]}"
        s += '\t\t\t\t\t\t\n'
        s += f"{self.cube[2][0][0]}\t{self.cube[2][0][1]}\t{self.cube[2][0][2]}\t"
        s += f"{self.cube[1][0][0]}\t{self.cube[1][0][1]}\t{self.cube[1][0][2]}\t"
        s += f"{self.cube[4][0][0]}\t{self.cube[4][0][1]}\t{self.cube[4][0][2]}\t"
        s += f"{self.cube[3][0][0]}\t{self.cube[3][0][1]}\t{self.cube[3][0][2]}\t\n"
        s += f"{self.cube[2][1][0]}\t{self.cube[2][1][1]}\t{self.cube[2][1][2]}\t"
        s += f"{self.cube[1][1][0]}\t{self.cube[1][1][1]}\t{self.cube[1][1][2]}\t"
        s += f"{self.cube[4][1][0]}\t{self.cube[4][1][1]}\t{self.cube[4][1][2]}\t"
        s += f"{self.cube[3][1][0]}\t{self.cube[3][1][1]}\t{self.cube[3][1][2]}\t\n"
        s += f"{self.cube[2][2][0]}\t{self.cube[2][2][1]}\t{self.cube[2][2][2]}\t"
        s += f"{self.cube[1][2][0]}\t{self.cube[1][2][1]}\t{self.cube[1][2][2]}\t"
        s += f"{self.cube[4][2][0]}\t{self.cube[4][2][1]}\t{self.cube[4][2][2]}\t"
        s += f"{self.cube[3][2][0]}\t{self.cube[3][2][1]}\t{self.cube[3][2][2]}\t\n"
        s += '\t\t\t'
        s += f"{self.cube[5][0][0]}\t{self.cube[5][0][1]}\t{self.cube[5][0][2]}"
        s += '\t\t\t\t\t\t\n'
        s += '\t\t\t'
        s += f"{self.cube[5][1][0]}\t{self.cube[5][1][1]}\t{self.cube[5][1][2]}"
        s += '\t\t\t\t\t\t\n'
        s += '\t\t\t'
        s += f"{self.cube[5][2][0]}\t{self.cube[5][2][1]}\t{self.cube[5][2][2]}"
        s += '\t\t\t\t\t\t'
        return s

    def __scramble__(self):
        """
        Applies the scramble algorithm starting from a random face of the cube.
        """
        self.front = random.choice(utils.COLORS)
        self.top = random.choice([t for (f,t) in utils.CONFIGURATIONS if f==self.front]) # Only two possibilities
        self.orientation = self.Orientation(self.front, self.top)
        self.__U__()
        self.__R__()
        self.__R__()
        self.__B__()
        self.__B__()
        self.__R__()
        self.__R__()
        self.__L__()
        self.__L__()
        self.__B_p__()
        self.__U__()
        self.__U__()
        self.__D__()
        self.__D__()
        self.__R_p__()
        self.__U__()
        self.__D_p__()
        self.__R__()
        self.__B__()
        self.__D__()
        self.__B__()
        self.__R__()
        self.__D_p__()
        self.__D__()
        self.__L__()
        self.__L__()

    """
    MOVES
    
    Notation:
    - We refer to the horizontal axis as the X axis
    - We refer to the vertical axis as the Y axis
    - We refer to the other axis as the Z axis
    As shown in the following:
    
    y ^
      |         ^ z
      |        /
      |       /      _________
      |      /      /|       /|
      |     /      /_|______/_|
      |    /      |  |_____|__|
      |   /       | /      | /
      |  /        |/_______|/
      | /   
    --|/------------------------------> x
     /|
    """

    def __R__(self):
        # Ring that has to rotate clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy([self.cube[front][0][2], self.cube[front][1][2], self.cube[front][2][2]])
        top = self.orientation.top
        top_squares = copy.deepcopy([self.cube[top][0][2], self.cube[top][1][2], self.cube[top][2][2]])
        back = self.orientation.back
        back_squares = copy.deepcopy([self.cube[back][0][2], self.cube[back][1][2], self.cube[back][2][2]])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy([self.cube[bottom][0][2], self.cube[bottom][1][2], self.cube[bottom][2][2]])
        # Rotate the ring clockwise
        # Top face gets the squares from front face
        self.cube[top][0][2] = front_squares[0]
        self.cube[top][1][2] = front_squares[1]
        self.cube[top][2][2] = front_squares[2]
        # Back face gets the squares from top face
        self.cube[back][0][2] = top_squares[0]
        self.cube[back][1][2] = top_squares[1]
        self.cube[back][2][2] = top_squares[2]
        # Bottom face gets the squares from back face
        self.cube[bottom][0][2] = back_squares[0]
        self.cube[bottom][1][2] = back_squares[1]
        self.cube[bottom][2][2] = back_squares[2]
        # Front face gets the squares from bottom face
        self.cube[front][0][2] = bottom_squares[0]
        self.cube[front][1][2] = bottom_squares[1]
        self.cube[front][2][2] = bottom_squares[2]
        # Rotate also the right face clockwise
        right = self.orientation.right
        right_squares = copy.deepcopy(self.cube[right])
        self.cube[right][0] = [right_squares[2][0], right_squares[1][0], right_squares[0][0]]
        self.cube[right][1] = [right_squares[2][1], right_squares[1][1], right_squares[0][1]]
        self.cube[right][2] = [right_squares[2][2], right_squares[1][2], right_squares[0][2]]

    def __R_p__(self):
        # Right ring that has to rotate counter-clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy([self.cube[front][0][2], self.cube[front][1][2], self.cube[front][2][2]])
        top = self.orientation.top
        top_squares = copy.deepcopy([self.cube[top][0][2], self.cube[top][1][2], self.cube[top][2][2]])
        back = self.orientation.back
        back_squares = copy.deepcopy([self.cube[back][0][2], self.cube[back][1][2], self.cube[back][2][2]])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy([self.cube[bottom][0][2], self.cube[bottom][1][2], self.cube[bottom][2][2]])
        # Rotate the ring counter-clockwise
        # Top face gets the squares from back face
        self.cube[top][0][2] = back_squares[0]
        self.cube[top][1][2] = back_squares[1]
        self.cube[top][2][2] = back_squares[2]
        # Back face gets the squares from bottom face
        self.cube[back][0][2] = bottom_squares[0]
        self.cube[back][1][2] = bottom_squares[1]
        self.cube[back][2][2] = bottom_squares[2]
        # Bottom face gets the squares from front face
        self.cube[bottom][0][2] = front_squares[0]
        self.cube[bottom][1][2] = front_squares[1]
        self.cube[bottom][2][2] = front_squares[2]
        # Front face gets the squares from top face
        self.cube[front][0][2] = top_squares[0]
        self.cube[front][1][2] = top_squares[1]
        self.cube[front][2][2] = top_squares[2]
        # Rotate also the right face counter-clockwise
        right = self.orientation.right
        right_squares = copy.deepcopy(self.cube[right])
        self.cube[right][0] = [right_squares[0][2], right_squares[1][2], right_squares[2][2]]
        self.cube[right][1] = [right_squares[0][1], right_squares[1][1], right_squares[2][1]]
        self.cube[right][2] = [right_squares[0][0], right_squares[1][0], right_squares[2][0]]

    def __L__(self):
        # Left ring that has to rotate clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy([self.cube[front][0][0], self.cube[front][1][0], self.cube[front][2][0]])
        top = self.orientation.top
        top_squares = copy.deepcopy([self.cube[top][0][0], self.cube[top][1][0], self.cube[top][2][0]])
        back = self.orientation.back
        back_squares = copy.deepcopy([self.cube[back][0][0], self.cube[back][1][0], self.cube[back][2][0]])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy([self.cube[bottom][0][0], self.cube[bottom][1][0], self.cube[bottom][2][0]])
        # Rotate the left ring clockwise
        # Top face gets the squares from back face
        self.cube[top][0][0] = back_squares[0]
        self.cube[top][1][0] = back_squares[1]
        self.cube[top][2][0] = back_squares[2]
        # Back face gets the squares from bottom face
        self.cube[back][0][0] = bottom_squares[0]
        self.cube[back][1][0] = bottom_squares[1]
        self.cube[back][2][0] = bottom_squares[2]
        # Bottom face gets the squares from front face
        self.cube[bottom][0][0] = front_squares[0]
        self.cube[bottom][1][0] = front_squares[1]
        self.cube[bottom][2][0] = front_squares[2]
        # Front face gets the squares from top face
        self.cube[front][0][0] = top_squares[0]
        self.cube[front][1][0] = top_squares[1]
        self.cube[front][2][0] = top_squares[2]
        # Rotate also the left face clockwise
        left = self.orientation.left
        left_squares = copy.deepcopy(self.cube[left])
        self.cube[left][0] = [left_squares[0][2], left_squares[1][2], left_squares[2][2]]
        self.cube[left][1] = [left_squares[0][1], left_squares[1][1], left_squares[2][1]]
        self.cube[left][2] = [left_squares[0][0], left_squares[1][0], left_squares[2][0]]

    def __L_p__(self):
        # Left ring that has to rotate counter-clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy([self.cube[front][0][0], self.cube[front][1][0], self.cube[front][2][0]])
        top = self.orientation.top
        top_squares = copy.deepcopy([self.cube[top][0][0], self.cube[top][1][0], self.cube[top][2][0]])
        back = self.orientation.back
        back_squares = copy.deepcopy([self.cube[back][0][0], self.cube[back][1][0], self.cube[back][2][0]])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy([self.cube[bottom][0][0], self.cube[bottom][1][0], self.cube[bottom][2][0]])
        # Rotate the left ring counter-clockwise
        # Top face gets the squares from front face
        self.cube[top][0][0] = front_squares[0]
        self.cube[top][1][0] = front_squares[1]
        self.cube[top][2][0] = front_squares[2]
        # Back face gets the squares from top face
        self.cube[back][0][0] = top_squares[0]
        self.cube[back][1][0] = top_squares[1]
        self.cube[back][2][0] = top_squares[2]
        # Bottom face gets the squares from back face
        self.cube[bottom][0][0] = back_squares[0]
        self.cube[bottom][1][0] = back_squares[1]
        self.cube[bottom][2][0] = back_squares[2]
        # Front face gets the squares from bottom face
        self.cube[front][0][0] = bottom_squares[0]
        self.cube[front][1][0] = bottom_squares[1]
        self.cube[front][2][0] = bottom_squares[2]
        # Rotate also the left face counter-clockwise
        left = self.orientation.left
        left_squares = copy.deepcopy(self.cube[left])
        self.cube[left][0] = [left_squares[2][0], left_squares[1][0], left_squares[0][0]]
        self.cube[left][1] = [left_squares[2][1], left_squares[1][1], left_squares[0][1]]
        self.cube[left][2] = [left_squares[2][2], left_squares[1][2], left_squares[0][2]]

    def __U__(self):
        # Top ring that has to rotate clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy([self.cube[front][0][0], self.cube[front][0][1], self.cube[front][0][2]])
        left = self.orientation.left
        left_squares = copy.deepcopy([self.cube[left][0][0], self.cube[left][0][1], self.cube[left][0][2]])
        back = self.orientation.back
        back_squares = copy.deepcopy([self.cube[back][0][0], self.cube[back][0][1], self.cube[back][0][2]])
        right = self.orientation.right
        right_squares = copy.deepcopy([self.cube[right][0][0], self.cube[right][0][1], self.cube[right][0][2]])
        # Rotate the top ring clockwise
        # Left face gets the squares from front face
        self.cube[left][0][0] = front_squares[0]
        self.cube[left][0][1] = front_squares[1]
        self.cube[left][0][2] = front_squares[2]
        # Back face gets the squares from left face
        self.cube[back][0][0] = left_squares[0]
        self.cube[back][0][1] = left_squares[1]
        self.cube[back][0][2] = left_squares[2]
        # Right face gets the squares from back face
        self.cube[right][0][0] = back_squares[0]
        self.cube[right][0][1] = back_squares[1]
        self.cube[right][0][2] = back_squares[2]
        # Front face gets the squares from right face
        self.cube[front][0][0] = right_squares[0]
        self.cube[front][0][1] = right_squares[1]
        self.cube[front][0][2] = right_squares[2]
        # Rotate also the top face clockwise
        top = self.orientation.top
        top_squares = copy.deepcopy(self.cube[top])
        self.cube[top][0] = [top_squares[0][2], top_squares[1][2], top_squares[2][2]]
        self.cube[top][1] = [top_squares[0][1], top_squares[1][1], top_squares[2][1]]
        self.cube[top][2] = [top_squares[0][0], top_squares[1][0], top_squares[2][0]]

    def __U_p__(self):
        # Top ring that has to rotate counter-clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy([self.cube[front][0][0], self.cube[front][0][1], self.cube[front][0][2]])
        left = self.orientation.left
        left_squares = copy.deepcopy([self.cube[left][0][0], self.cube[left][0][1], self.cube[left][0][2]])
        back = self.orientation.back
        back_squares = copy.deepcopy([self.cube[back][0][0], self.cube[back][0][1], self.cube[back][0][2]])
        right = self.orientation.right
        right_squares = copy.deepcopy([self.cube[right][0][0], self.cube[right][0][1], self.cube[right][0][2]])
        # Rotate the top ring counter-clockwise
        # Left face gets the squares from back face
        self.cube[left][0][0] = back_squares[0]
        self.cube[left][0][1] = back_squares[1]
        self.cube[left][0][2] = back_squares[2]
        # Back face gets the squares from right face
        self.cube[back][0][0] = right_squares[0]
        self.cube[back][0][1] = right_squares[1]
        self.cube[back][0][2] = right_squares[2]
        # Right face gets the squares from front face
        self.cube[right][0][0] = front_squares[0]
        self.cube[right][0][1] = front_squares[1]
        self.cube[right][0][2] = front_squares[2]
        # Front face gets the squares from left face
        self.cube[front][0][0] = left_squares[0]
        self.cube[front][0][1] = left_squares[1]
        self.cube[front][0][2] = left_squares[2]
        # Rotate also the top face counter-clockwise
        top = self.orientation.top
        top_squares = copy.deepcopy(self.cube[top])
        self.cube[top][0] = [top_squares[2][0], top_squares[1][0], top_squares[0][0]]
        self.cube[top][1] = [top_squares[2][1], top_squares[1][1], top_squares[0][1]]
        self.cube[top][2] = [top_squares[2][2], top_squares[1][2], top_squares[0][2]]

    def __D__(self):
        pass

    def __D_p__(self):
        pass

    def __F__(self):
        # Front ring that has to rotate clockwise
        top = self.orientation.top
        top_squares = copy.deepcopy([self.cube[top][2][0], self.cube[top][2][1], self.cube[top][2][2]])
        right = self.orientation.right
        right_squares = copy.deepcopy([self.cube[right][2][0], self.cube[right][2][1], self.cube[right][2][2]])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy([self.cube[bottom][2][0], self.cube[bottom][2][1], self.cube[bottom][2][2]])
        left = self.orientation.left
        left_squares = copy.deepcopy([self.cube[left][2][0], self.cube[left][2][1], self.cube[left][2][2]])
        # Rotate the front ring clockwise
        # Right face gets the squares from top face
        self.cube[right][2][0] = top_squares[0]
        self.cube[right][2][1] = top_squares[1]
        self.cube[right][2][2] = top_squares[2]
        # Bottom face gets the squares from right face
        self.cube[bottom][2][0] = right_squares[0]
        self.cube[bottom][2][1] = right_squares[1]
        self.cube[bottom][2][2] = right_squares[2]
        # Left face gets the squares from bottom face
        self.cube[left][2][0] = bottom_squares[0]
        self.cube[left][2][1] = bottom_squares[1]
        self.cube[left][2][2] = bottom_squares[2]
        # Top face gets the squares from left face
        self.cube[top][2][0] = left_squares[0]
        self.cube[top][2][1] = left_squares[1]
        self.cube[top][2][2] = left_squares[2]
        # Rotate also the front face clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy(self.cube[front])
        self.cube[front][0] = [front_squares[0][2], front_squares[1][2], front_squares[2][2]]
        self.cube[front][1] = [front_squares[0][1], front_squares[1][1], front_squares[2][1]]
        self.cube[front][2] = [front_squares[0][0], front_squares[1][0], front_squares[2][0]]

    def __F_p__(self):
        # Front ring that has to rotate counter-clockwise
        top = self.orientation.top
        top_squares = copy.deepcopy([self.cube[top][2][0], self.cube[top][2][1], self.cube[top][2][2]])
        right = self.orientation.right
        right_squares = copy.deepcopy([self.cube[right][2][0], self.cube[right][2][1], self.cube[right][2][2]])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy([self.cube[bottom][2][0], self.cube[bottom][2][1], self.cube[bottom][2][2]])
        left = self.orientation.left
        left_squares = copy.deepcopy([self.cube[left][2][0], self.cube[left][2][1], self.cube[left][2][2]])
        # Rotate the front ring counter-clockwise
        # Right face gets the squares from bottom face
        self.cube[right][2][0] = bottom_squares[0]
        self.cube[right][2][1] = bottom_squares[1]
        self.cube[right][2][2] = bottom_squares[2]
        # Bottom face gets the squares from left face
        self.cube[bottom][2][0] = left_squares[0]
        self.cube[bottom][2][1] = left_squares[1]
        self.cube[bottom][2][2] = left_squares[2]
        # Left face gets the squares from top face
        self.cube[left][2][0] = top_squares[0]
        self.cube[left][2][1] = top_squares[1]
        self.cube[left][2][2] = top_squares[2]
        # Top face gets the squares from right face
        self.cube[top][2][0] = right_squares[0]
        self.cube[top][2][1] = right_squares[1]
        self.cube[top][2][2] = right_squares[2]
        # Rotate also the front face counter-clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy(self.cube[front])
        self.cube[front][0] = [front_squares[0][2], front_squares[1][2], front_squares[2][2]]
        self.cube[front][1] = [front_squares[0][1], front_squares[1][1], front_squares[2][1]]
        self.cube[front][2] = [front_squares[0][0], front_squares[1][0], front_squares[2][0]]

    def __B__(self):
        pass

    def __B_p__(self):
        pass