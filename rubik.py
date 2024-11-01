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
            return (f"|\t- Front (F): {utils.COLOR_LEGEND[self.front]} ({self.front})\t\t\t\t\t\t\t|\n"
                    f"|\t- Top (U): {utils.COLOR_LEGEND[self.top]} ({self.top})\t\t\t\t\t\t\t|\n"
                    f"|\t- Back (B): {utils.COLOR_LEGEND[self.back]} ({self.back})\t\t\t\t\t\t\t|\n"
                    f"|\t- Bottom (D): {utils.COLOR_LEGEND[self.bottom]} ({self.bottom})\t\t\t\t\t\t|\n"
                    f"|\t- Left (L): {utils.COLOR_LEGEND[self.left]} ({self.left})\t\t\t\t\t\t\t|\n"
                    f"|\t- Right (R): {utils.COLOR_LEGEND[self.right]} ({self.right})\t\t\t\t\t\t\t|")

    def __init__(self):
        self.cube = [
            [[utils.WHITE for _ in range(3)] for _ in range(3)],
            [[utils.RED for _ in range(3)] for _ in range(3)],
            [[utils.GREEN for _ in range(3)] for _ in range(3)],
            [[utils.ORANGE for _ in range(3)] for _ in range(3)],
            [[utils.BLUE for _ in range(3)] for _ in range(3)],
            [[utils.YELLOW for _ in range(3)] for _ in range(3)]
        ]
        self.__scramble__()

    def __str__(self):
        return (f" ___________________________________________________ \n"
                f"|\tCube:\t\t\t\t\t\t\t\t\t\t\t|\n"
                f"{self.__str_cube__()}\n"
                f"|---------------------------------------------------|\n"
                f"|\tOrientation:\t\t\t\t\t\t\t\t\t|\n"
                f"{self.orientation}\n"
                f"|___________________________________________________|")

    def __str_cube__(self):
        front = self.orientation.front
        top = self.orientation.top
        bottom = self.orientation.bottom
        back = self.orientation.back
        left = self.orientation.left
        right = self.orientation.right
        s = ""
        """
        SOLVED CUBE:                                            
                    0   0   0
                    0   0   0
                    0   0   0
        2   2   2   1   1   1   4   4   4   3   3   3
        2   2   2   1   1   1   4   4   4   3   3   3
        2   2   2   1   1   1   4   4   4   3   3   3
                    5   5   5
                    5   5   5
                    5   5   5
                    _________
                   |         |
                   |    U    |
         __________|_________|_____________________
        |          |         |          |          |
        |     L    |    F    |     R    |     B    |
        |__________|_________|__________|__________|
                   |         |
                   |    D    |
                   |_________|
        """
        s += '|\t\t\t\t'
        s += f"{self.cube[top][0][0]}\t{self.cube[top][0][1]}\t{self.cube[top][0][2]}"
        s += '\t\t\t\t\t\t\t|\n'
        s += '|\t\t\t\t'
        s += f"{self.cube[top][1][0]}\t{self.cube[top][1][1]}\t{self.cube[top][1][2]}"
        s += '\t\t\t\t\t\t\t|\n'
        s += '|\t\t\t\t'
        s += f"{self.cube[top][2][0]}\t{self.cube[top][2][1]}\t{self.cube[top][2][2]}"
        s += '\t\t\t\t\t\t\t|\n'
        s += f"|\t{self.cube[left][0][0]}\t{self.cube[left][0][1]}\t{self.cube[left][0][2]}\t"
        s += f"{self.cube[front][0][0]}\t{self.cube[front][0][1]}\t{self.cube[front][0][2]}\t"
        s += f"{self.cube[right][0][0]}\t{self.cube[right][0][1]}\t{self.cube[right][0][2]}\t"
        s += f"{self.cube[back][0][0]}\t{self.cube[back][0][1]}\t{self.cube[back][0][2]}\t|\n"
        s += f"|\t{self.cube[left][1][0]}\t{self.cube[left][1][1]}\t{self.cube[left][1][2]}\t"
        s += f"{self.cube[front][1][0]}\t{self.cube[front][1][1]}\t{self.cube[front][1][2]}\t"
        s += f"{self.cube[right][1][0]}\t{self.cube[right][1][1]}\t{self.cube[right][1][2]}\t"
        s += f"{self.cube[back][1][0]}\t{self.cube[back][1][1]}\t{self.cube[back][1][2]}\t|\n"
        s += f"|\t{self.cube[left][2][0]}\t{self.cube[left][2][1]}\t{self.cube[left][2][2]}\t"
        s += f"{self.cube[front][2][0]}\t{self.cube[front][2][1]}\t{self.cube[front][2][2]}\t"
        s += f"{self.cube[right][2][0]}\t{self.cube[right][2][1]}\t{self.cube[right][2][2]}\t"
        s += f"{self.cube[back][2][0]}\t{self.cube[back][2][1]}\t{self.cube[back][2][2]}\t|\n"
        s += '|\t\t\t\t'
        s += f"{self.cube[bottom][0][0]}\t{self.cube[bottom][0][1]}\t{self.cube[bottom][0][2]}"
        s += '\t\t\t\t\t\t\t|\n'
        s += '|\t\t\t\t'
        s += f"{self.cube[bottom][1][0]}\t{self.cube[bottom][1][1]}\t{self.cube[bottom][1][2]}"
        s += '\t\t\t\t\t\t\t|\n'
        s += '|\t\t\t\t'
        s += f"{self.cube[bottom][2][0]}\t{self.cube[bottom][2][1]}\t{self.cube[bottom][2][2]}"
        s += '\t\t\t\t\t\t\t|\n'
        s += '|               _________                           |\n'
        s += '|              |         |                          |\n'
        s += '|              |    U    |                          |\n'
        s += '|    __________|_________|_____________________     |\n'
        s += '|   |          |         |          |          |    |\n'
        s += '|   |     L    |    F    |     R    |     B    |    |\n'
        s += '|   |__________|_________|__________|__________|    |\n'
        s += '|              |         |                          |\n'
        s += '|              |    D    |                          |\n'
        s += '|              |_________|                          |'
        return s

    def __scramble__(self): # TODO generate random scramble
        """
        Applies a scramble algorithm starting from the green face on the front and the white face on the top.
        """
        self.front = utils.GREEN
        self.top = utils.WHITE
        self.orientation = self.Orientation(self.front, self.top)
        self.__D__()
        self.__D__()
        self.__U__()
        self.__F__()
        self.__F__()
        self.__D_p__()
        self.__B__()
        self.__B__()
        self.__F__()
        self.__U__()
        self.__L_p__()
        self.__B_p__()
        self.__U__()
        self.__U__()
        self.__R__()
        self.__U_p__()
        self.__B_p__()
        self.__F_p__()
        self.__R__()
        self.__R__()
        self.__F__()
        self.__F__()
        self.__B_p__()
        self.__L_p__()
        self.__R__()
        self.__R__()
        self.__B__()
        self.__B__()
        self.__U__()
        self.__U__()
        self.__B_p__()
        self.__U__()
        self.__B_p__()
        self.__D__()
        self.__D__()

    """
    MOVES
    
    Notation:
    - We refer to the horizontal axis as the X axis
    - We refer to the vertical axis as the Y axis
    - We refer to the other axis as the Z axis
    As shown in the following:
    
    Y ^
      |         ^ Z
      |        /
      |       /      _________
      |      /      /|       /|
      |     /      /_|______/_|
      |    /      |  |_____|__|
      |   /       | /      | /
      |  /        |/_______|/
      | /   
    --|/------------------------------> X
     /|
     
    Whole cube rotations:
    - X: 90 degrees on the X axis
    - X_p: -90 degrees on the X axis
    - Y: 90 degrees on the Y axis
    - Y_p: -90 degrees on the Y axis
    - Z: 90 degrees on the Z axis
    - Z_p: -90 degrees on the Z axis
    
    Face rotations:
    - R: rotate the right face 90 degrees on the X axis
    - R_p: rotate the right face -90 degrees on the X axis
    - L: rotate the left face -90 degrees on the X axis
    - L_p: rotate the left face 90 degrees on the X axis
    - U: rotate the top face 90 degrees on the Y axis
    - U_p: rotate the top face -90 degrees on the Y axis
    - D: rotate the bottom face -90 degrees on the Y axis
    - D_p: rotate the bottom face 90 degrees on the Y axis
    - F: rotate the front face 90 degrees on the Z axis
    - F_p: rotate the front face -90 degrees on the Z axis
    - B: rotate the back face -90 degrees on the Z axis
    - B_p: rotate the back face 90 degrees on the Z axis
    """

    # Utility methods

    def __clockwise_rotation__(self, face):
        face_squares = copy.deepcopy(self.cube[face])
        self.cube[face][0] = [face_squares[2][0], face_squares[1][0], face_squares[0][0]]
        self.cube[face][1] = [face_squares[2][1], face_squares[1][1], face_squares[0][1]]
        self.cube[face][2] = [face_squares[2][2], face_squares[1][2], face_squares[0][2]]

    def __counter_clockwise_rotation__(self, face):
        face_squares = copy.deepcopy(self.cube[face])
        self.cube[face][0] = [face_squares[0][2], face_squares[1][2], face_squares[2][2]]
        self.cube[face][1] = [face_squares[0][1], face_squares[1][1], face_squares[2][1]]
        self.cube[face][2] = [face_squares[0][0], face_squares[1][0], face_squares[2][0]]

    def __180_degrees_rotation__(self, face):
        face_squares = copy.deepcopy(self.cube[face])
        self.cube[face][0] = [face_squares[2][2], face_squares[2][1], face_squares[2][0]]
        self.cube[face][1] = [face_squares[1][2], face_squares[1][1], face_squares[1][0]]
        self.cube[face][2] = [face_squares[0][2], face_squares[0][1], face_squares[0][0]]

    # Whole cube rotations

    def __X__(self):
        # Change the L face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.left)
        # Change the R face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.right)
        # Change the U face doing a 180 degrees rotation
        self.__180_degrees_rotation__(self.orientation.top)
        # Change the B face doing a 180 degrees rotation
        self.__180_degrees_rotation__(self.orientation.back)
        # Fix the orientation
        self.orientation = self.Orientation(self.orientation.bottom, self.orientation.front)

    def __X_p__(self):
        # Change the L face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.left)
        # Change the R face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.right)
        # Change the U face doing a 180 degrees rotation
        self.__180_degrees_rotation__(self.orientation.top)
        # Change the B face doing a 180 degrees rotation
        self.__180_degrees_rotation__(self.orientation.back)
        # Fix the orientation
        self.orientation = self.Orientation(self.orientation.top, self.orientation.back)

    def __Y__(self):
        # Change the top face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.top)
        # Change the bottom face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.bottom)
        # Fix the orientation
        self.orientation = self.Orientation(self.orientation.right, self.orientation.top)

    def __Y_p__(self):
        # Change the top face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.top)
        # Change the bottom face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.bottom)
        # Fix the orientation
        self.orientation = self.Orientation(self.orientation.left, self.orientation.top)

    def __Z__(self):
        # Change the front face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.front)
        # Change the left face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.left)
        # Change the back face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.back)
        # Change the right face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.right)
        # Change the top face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.top)
        # Change the bottom face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.bottom)
        # Fix the orientation
        self.orientation = self.Orientation(self.orientation.front, self.orientation.left)

    def __Z_p__(self):
        # Change the front face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.front)
        # Change the left face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.left)
        # Change the back face doing a clockwise rotation
        self.__clockwise_rotation__(self.orientation.back)
        # Change the right face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.right)
        # Change the top face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.top)
        # Change the bottom face doing a counter-clockwise rotation
        self.__counter_clockwise_rotation__(self.orientation.bottom)
        # Fix the orientation
        self.orientation = self.Orientation(self.orientation.front, self.orientation.right)

    # Face rotations

    def __R__(self):
        # Ring that has to rotate clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy(self.cube[front])
        top = self.orientation.top
        top_squares = copy.deepcopy(self.cube[top])
        back = self.orientation.back
        back_squares = copy.deepcopy(self.cube[back])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy(self.cube[bottom])
        # Rotate the ring clockwise according to each face orientation (the indexes may be different for each face)
        # Top face gets the squares from front face
        self.cube[top][0][2] = front_squares[0][2]
        self.cube[top][1][2] = front_squares[1][2]
        self.cube[top][2][2] = front_squares[2][2]
        # Back face gets the squares from top face
        self.cube[back][0][0] = top_squares[2][2]
        self.cube[back][1][0] = top_squares[1][2]
        self.cube[back][2][0] = top_squares[0][2]
        # Bottom face gets the squares from back face
        self.cube[bottom][0][2] = back_squares[2][0]
        self.cube[bottom][1][2] = back_squares[1][0]
        self.cube[bottom][2][2] = back_squares[0][0]
        # Front face gets the squares from bottom face
        self.cube[front][0][2] = bottom_squares[0][2]
        self.cube[front][1][2] = bottom_squares[1][2]
        self.cube[front][2][2] = bottom_squares[2][2]
        # Rotate also the right face clockwise
        self.__clockwise_rotation__(self.orientation.right)

    def __R_p__(self):
        # Right ring that has to rotate counter-clockwise
        front = self.orientation.front
        front_squares = copy.deepcopy(self.cube[front])
        top = self.orientation.top
        top_squares = copy.deepcopy(self.cube[top])
        back = self.orientation.back
        back_squares = copy.deepcopy(self.cube[back])
        bottom = self.orientation.bottom
        bottom_squares = copy.deepcopy(self.cube[bottom])
        # Rotate the ring counter-clockwise according to each face orientation (the indexes may be different for each face)
        # Top face gets the squares from back face
        self.cube[top][0][2] = back_squares[2][0]
        self.cube[top][1][2] = back_squares[1][0]
        self.cube[top][2][2] = back_squares[0][0]
        # Back face gets the squares from bottom face
        self.cube[back][0][0] = bottom_squares[2][2]
        self.cube[back][1][0] = bottom_squares[1][2]
        self.cube[back][2][0] = bottom_squares[0][2]
        # Bottom face gets the squares from front face
        self.cube[bottom][0][2] = front_squares[0][2]
        self.cube[bottom][1][2] = front_squares[1][2]
        self.cube[bottom][2][2] = front_squares[2][2]
        # Front face gets the squares from top face
        self.cube[front][0][2] = top_squares[0][2]
        self.cube[front][1][2] = top_squares[1][2]
        self.cube[front][2][2] = top_squares[2][2]
        # Rotate also the right face counter-clockwise
        self.__counter_clockwise_rotation__(self.orientation.right)

    def __L__(self):
        # Rotating the left face -90 degrees means to perform Y2 (180 degrees on the Y axis),
        # then doing an R move and doing Y2 again
        self.__Y__()
        self.__Y__()
        self.__R__()
        self.__Y__()
        self.__Y__()

    def __L_p__(self):
        # Rotating the left face 90 degrees means to perform Y2 (180 degrees on the Y axis),
        # then doing an R_p move and doing Y2 again
        self.__Y__()
        self.__Y__()
        self.__R_p__()
        self.__Y__()
        self.__Y__()

    def __U__(self):
        # Rotating the top face 90 degrees on the Y axis means to perform Z (90 degrees on the Z axis),
        # then doing an R move and doing Z_p
        self.__Z__()
        self.__R__()
        self.__Z_p__()

    def __U_p__(self):
        # Rotating the top face -90 degrees on the Y axis means to perform Z (90 degrees on the Z axis),
        # then doing an R_p move and doing Z_p
        self.__Z__()
        self.__R_p__()
        self.__Z_p__()

    def __D__(self):
        # Rotating the bottom face -90 degrees on the Y axis means to perform Z_p (-90 degrees on the Z axis),
        # then doing an R move and doing Z
        self.__Z_p__()
        self.__R__()
        self.__Z__()

    def __D_p__(self):
        # Rotating the bottom face 90 degrees on the Y axis means to perform Z_p (-90 degrees on the Z axis),
        # then doing an R_p move and doing Z
        self.__Z_p__()
        self.__R_p__()
        self.__Z__()

    def __F__(self):
        # Rotating the front face 90 degrees on the Z axis means to perform Y_p (-90 degrees on the Y axis),
        # then doing an R move and doing Y
        self.__Y_p__()
        self.__R__()
        self.__Y__()

    def __F_p__(self):
        # Rotating the front face -90 degrees on the Z axis means to perform Y_p (-90 degrees on the Y axis),
        # then doing an R_p move and doing Y
        self.__Y_p__()
        self.__R_p__()
        self.__Y__()

    def __B__(self):
        # Rotating the back face -90 degrees on the Z axis means to perform Y (90 degrees on the Y axis),
        # then doing an R move and doing Y_p
        self.__Y__()
        self.__R__()
        self.__Y_p__()

    def __B_p__(self):
        # Rotating the back face 90 degrees on the Z axis means to perform Y (90 degrees on the Y axis),
        # then doing an R move and doing Y_p
        self.__Y__()
        self.__R_p__()
        self.__Y_p__()