class RubicCube:
    def __init__(self):
        # For debugging purposes, it is interesting that each little face has a different name
        self._top = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        self._left = [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]
        self._front = [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', '!']]
        self._right = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        self._back = [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]
        self._bottom = [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '?']]

    def setStandardSolution(self):
        self._top = [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']]
        self._left = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
        self._front = [['c', 'c', 'c'], ['c', 'c', 'c'], ['c', 'c', 'c']]
        self._right = [['d', 'd', 'd'], ['d', 'd', 'd'], ['d', 'd', 'd']]
        self._back = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
        self._bottom = [['f', 'f', 'f'], ['f', 'f', 'f'], ['f', 'f', 'f']]

    def print(self):
        for i in range(3):
            print("    ", end='')
            for j in range(3):
                print(self._top[i][j], end='')
            print('')

        for i in range(3):
            for j in range(3):
                print(self._left[i][j], end='')
            print('|', end='')
            for j in range(3):
                print(self._front[i][j], end='')
            print('|', end='')
            for j in range(3):
                print(self._right[i][j], end='')
            print('|', end='')
            for j in range(3):
                print(self._back[i][j], end='')
            print('')

        for i in range(3):
            print("    ", end='')
            for j in range(3):
                print(self._bottom[i][j], end='')
            print('')

    def clone(self):
        # TODO: This method should return another instance of RubicCube with the same configuration as self
        c = RubicCube()
        c.copy(self)
        return c

    def copy(self, aCube):
        # TODO: This method should copy the configuration of aCube into self
        self._top = aCube._top
        self._left = aCube._left
        self._front = aCube._front
        self._right = aCube._right
        self._back = aCube._back
        self._bottom = aCube._bottom

    def equals(self, aCube):
        faces1 = [self._top, self._bottom, self._left, self._front, self._right, self._back]
        faces2 = [aCube._top, aCube._bottom, aCube._left, aCube._front, aCube._right, aCube._back]

        for face1, face2 in zip(faces1, faces2):
            for i in range(3):
                for j in range(3):
                    if face1[i][j] != face2[i][j]:
                        return False
        return True

    def write(self, filename):
        # TODO: It is interesting to have a method that writes the configuration of the cube into a file
        try:
            f = open(filename, 'w')
            for i in range(3):
                f.write("    ")
                for j in range(3):
                    f.write(self._top[i][j])
                f.write('\n')

            for i in range(3):
                for j in range(3):
                    f.write(self._left[i][j])
                f.write('|')
                for j in range(3):
                    f.write(self._front[i][j])
                f.write('|')
                for j in range(3):
                    f.write(self._right[i][j])
                f.write('|')
                for j in range(3):
                    f.write(self._back[i][j])
                f.write('\n')

            for i in range(3):
                f.write("    ")
                for j in range(3):
                    f.write(self._bottom[i][j])
                f.write('\n')
        except:
            print('An error ocurred trying to create the file: ', filename)
        finally:
            f.close()

    def read(self, filename):
        # TODO: It is interesting to have a method that reads the configuration of the cube from a file
        try:
            f = open(filename, 'r')
            for i in range(3):
                f.read(4)
                for j in range(3):
                    self._top[i][j] = f.read(1)
                f.read(1)

            for i in range(3):
                for j in range(3):
                    self._left[i][j] = f.read(1)
                f.read(1)
                for j in range(3):
                    self._front[i][j] = f.read(1)
                f.read(1)
                for j in range(3):
                    self._right[i][j] = f.read(1)
                f.read(1)
                for j in range(3):
                    self._back[i][j] = f.read(1)
                f.read(1)

            for i in range(3):
                f.read(4)
                for j in range(3):
                    self._bottom[i][j] = f.read(1)
                f.read(1)
        except:
            print('An error ocurred trying to open the file: ', filename)
        finally:
            f.close()

    def rotateFrontClockwise(self):
        # TODO: This method should modify the configuration of the cube resulting in the rotation of the front face
        # clockwisely
        aux = [self._right[i][0] for i in range(3)]

        for i in range(3):
            self._right[i][0] = self._top[2][i]

        for i in range(3):
            self._top[2][2 - i] = self._left[i][2]

        for i in range(3):
            self._left[i][2] = self._bottom[0][i]

        for i in range(3):
            self._bottom[0][2 - i] = aux[i]

        self._rotateClockwise(self._front)

    def rotateFrontAntiClockwise(self):

        # TODO: This method should modify the configuration of the cube resulting in the rotation of the front face
        # anticlockwisely
        aux = [self._bottom[0][i] for i in range(3)]

        for i in range(3):
            self._bottom[0][i] = self._left[i][2]
        for i in range(3):
            self._left[i][2] = self._top[2][
                2 - i]  # not possible to make the rotation with only one for, becouse of the modification of the top face in the same for. The problem is with ther first itereation in top face
        for i in range(3):
            self._top[2][i] = self._right[i][0]
        for i in range(3):
            self._right[2 - i][0] = aux[i]

        self._rotateAntiClockwise(self._front)

    def rotateTopClockwise(self):
        # TODO: This method should modify the configuration of the cube resulting in the rotation of the front face
        # clockwisely

        aux = [self._front[0][i] for i in range(3)]
        for i in range(3):
            self._front[0][i] = self._right[0][i]
            self._right[0][i] = self._back[0][i]
            self._back[0][i] = self._left[0][i]
            self._left[0][i] = aux[i]

        self._rotateClockwise(self._top)

    def rotateTopAntiClockwise(self):

        aux = [self._front[0][i] for i in range(3)]
        for i in range(3):
            self._front[0][i] = self._left[0][i]
            self._left[0][i] = self._back[0][i]
            self._back[0][i] = self._right[0][i]
            self._right[0][i] = aux[i]

        self._rotateAntiClockwise(self._top)

    def rotateLeftClockwise(self):

        aux = [self._bottom[i][0] for i in range(3)]

        for i in range(3):
            self._bottom[i][0] = self._front[i][0]
            self._front[i][0] = self._top[i][0]
            self._top[i][0] = self._back[2 - i][2]
            self._back[2 - i][2] = aux[i]

        self._rotateClockwise(self._left)

    def rotateLeftAntiClockwise(self):

        aux = [self._bottom[i][0] for i in range(3)]

        for i in range(3):
            self._bottom[i][0] = self._back[2 - i][2]
            self._back[2 - i][2] = self._top[i][0]
            self._top[i][0] = self._front[i][0]
            self._front[i][0] = aux[i]

        self._rotateAntiClockwise(self._left)

    def rotateBackClockwise(self):
        # TODO: This method should modify the configuration of the cube resulting in the rotation of the back face
        # clockwisely
        aux = [self._bottom[2][2 - i] for i in range(3)]

        for i in range(3):
            self._bottom[2][2 - i] = self._left[2 - i][0]
        for i in range(3):
            self._left[2 - i][0] = self._top[0][i]
        for i in range(3):
            self._top[0][i] = self._right[i][2]
        for i in range(3):
            self._right[i][2] = aux[i]

        self._rotateClockwise(self._back)

    def rotateBottomClockwise(self):
        # TODO: This method should modify the configuration of the cube resulting in the rotation of the bottom face
        # clockwisely
        aux = [self._front[2][i] for i in range(3)]

        for i in range(3):
            self._front[2][i] = self._left[2][i]
            self._left[2][i] = self._back[2][i]
            self._back[2][i] = self._right[2][i]
            self._right[2][i] = aux[i]

        self._rotateClockwise(self._bottom)

    def rotateRightClockwise(self):
        #TODO...
        print("ERROR: rotateRightClockwise is not implemented yet")

    def rotateRightAntiClockwise(self):
        #TODO...
        print("ERROR: rotateRightAntiClockwise is not implemented yet")

    def rotateBackAntiClockwise(self):
        #TODO...
        print("ERROR: rotateBackAntiClockwise is not implemented yet")

    def rotateBottomAntiClockwise(self):
        #TODO...
        print("ERROR: rotateBottomAntiClockwise is not implemented yet")


    # The following function generalizes the process of rotating a face clockwise.
    # BUT JUST THE FACE. This does not consider the adyacent columns and rows of other faces
    def _rotateClockwise(self, face):
        aux = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = aux

        aux = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = aux

    # The following function generalizes the process of rotating a face clockwise.
    # BUT JUST THE FACE. This does not consider the adyacent columns and rows of other faces
    def _rotateAntiClockwise(self, face):
        aux = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = aux

        aux = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = aux

    # The following functions are not to be used to find the solution of the problem. However, they are interesting
    # to check that the code is right. For instance, rotating the left face clockwisely should be exactly the same as
    # rotating the whole cube from left to right, rotating the front face clockwise and rotating the whole cube from
    # right to left
    def _rotateCubeLeftToRight(self):
        aux = self._left
        self._left = self._back
        self._back = self._right
        self._right = self._front
        self._front = aux

        # Rotate top and bottom faces accordingly
        self._rotateAntiClockwise(self._top)
        self._rotateClockwise(self._bottom)

    def _rotateCubeRightToLeft(self):
        aux = self._right
        self._right = self._back
        self._back = self._left
        self._left = self._front
        self._front = aux

        # Rotate top and bottom faces accordingly
        self._rotateClockwise(self._top)
        self._rotateAntiClockwise(self._bottom)

    def _rotateCubeTopToBottom(self):
        #TODO...
        print("ERROR: _rotateCubeTopToBottom is not implemented yet")

    def _rotateCubeBottomToTop(self):
        #TODO...
        print("ERROR: _rotateCubeBottomToTop is not implemented yet")

    def _rotateCubeClockwise(self):
        #TODO...
        print("ERROR: _rotateCubeClockwise is not implemented yet")

    def _rotateCubeAntiClockwise(self):
        #TODO...
        print("ERROR: _rotateCubeAntiClockwise is not implemented yet")

#######
# TEST FUNCTIONS
#######

# It is very common to make mistakes in the rotate functions. That's why it is interesting to desing test cases
def rotateTopClockwise_test1():
    c1 = RubicCube()
    c2 = RubicCube()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()

    if not c1.equals(c2):
        print('ERROR: There is an error rotating top clockwisely')


def rotateTopAnticlockwise_test1():
    c1 = RubicCube()
    c2 = RubicCube()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c1.rotateTopClockwise()
    c2.rotateTopAntiClockwise()

    if not c1.equals(c2):
        print('ERROR: There is an error rotating top either clockwisely or anticlockwisely')


def rotateLeftClockwise_test1():
    c1 = RubicCube()
    c2 = RubicCube()

    c2.rotateLeftClockwise()
    c1._rotateCubeLeftToRight()
    c1.rotateFrontClockwise()
    c1._rotateCubeRightToLeft()

    if not c1.equals(c2):
        print(
            'ERROR: There is an error rotating either left clockwise, the whole cube from left to right or from right to'
            ' left, or front clockwise')


def rotateCubeLeftToRight_test1():
    c1 = RubicCube()
    c2 = RubicCube()

    c1._rotateCubeLeftToRight()
    c1._rotateCubeLeftToRight()
    c1._rotateCubeLeftToRight()
    c1._rotateCubeLeftToRight()

    if not c1.equals(c2):
        print('ERROR: There is an error rotating the whole cube from left to right')


def copyCube_test1():
    c1 = RubicCube()
    c2 = RubicCube()

    if not c1.equals(c2):
        print("ERROR: Two cubes have been created, but their initial states are not the same")

    c1.rotateTopClockwise()

    if c1.equals(c2):
        print("ERROR: Two exepected equal cubes remain the same after a rotateTopClockwise operation has been"
              " performed on one of them")

    c2.copy(c1)

    if not c1.equals(c2):
        print("ERROR: Two cubes are different just after one copy the state of the other")

    c1.rotateTopClockwise()

    if c1.equals(c2):
        print(
            "ERROR: Two exepected equal cubes remain the same after a copy and a rotateTopClockwise operation has been"
            " performed on one of them. This means that both cubes use the same internal matrices. They have not been"
            " copied, but the cubes use the same matrices instead")

def test_4rotationsDonothing(func):
    '''This function tests that one application of func on the cube modifies the cube, and that four operations
    get it back to the original state'''
    c1 = RubicCube()
    c2 = RubicCube()

    getattr(c1, func)()

    if c1.equals(c2):
        print("ERROR: ", func, " has done nothing")

    getattr(c1, func)()
    getattr(c1, func)()
    getattr(c1, func)()

    if not c1.equals(c2):
        print("ERROR: Applying ", func, " four times has not produced the original state")

def test_3and1oppositeOperations(func1, func2):
    c1 = RubicCube()
    c2 = RubicCube()

    getattr(c1, func1)()

    if c1.equals(c2):
        print("ERROR: ", func1, " has done nothing")

    getattr(c1, func1)()
    getattr(c1, func1)()
    getattr(c2, func2)()

    if not c1.equals(c2):
        print("ERROR: Applying ", func1, " three times and ", func2, " once on an original copy does not produce the same result")


def rotateCubeLeftToRight_test1():
    c1 = RubicCube()
    c2 = RubicCube()

    c1._rotateCubeLeftToRight()
    c1._rotateCubeLeftToRight()
    c1._rotateCubeLeftToRight()
    c1._rotateCubeLeftToRight()

    if not c1.equals(c2):
        print('ERROR: There is an error rotating the whole cube from left to right')


def copyCube_test1():
    c1 = RubicCube()
    c2 = RubicCube()

    if not c1.equals(c2):
        print("ERROR: Two cubes have been created, but their initial states are not the same")

    c1.rotateTopClockwise()

    if c1.equals(c2):
        print("ERROR: Two exepected equal cubes remain the same after a rotateTopClockwise operation has been"
              " performed on one of them")

    c2.copy(c1)

    if not c1.equals(c2):
        print("ERROR: Two cubes are different just after one copy the state of the other")

    c1.rotateTopClockwise()

    if c1.equals(c2):
        print(
            "ERROR: Two exepected equal cubes remain the same after a copy and a rotateTopClockwise operation has been"
            " performed on one of them. This means that both cubes use the same internal matrices. They have not been"
            " copied, but the cubes use the same matrices instead")


def runTests():
    copyCube_test1()
    rotateTopClockwise_test1()
    rotateTopAnticlockwise_test1()
    rotateCubeLeftToRight_test1()
    rotateLeftClockwise_test1()

    test_4rotationsDonothing('rotateTopClockwise')
    test_4rotationsDonothing('rotateLeftClockwise')
    test_4rotationsDonothing('rotateFrontClockwise')
    test_4rotationsDonothing('rotateRightClockwise')
    test_4rotationsDonothing('rotateBackClockwise')
    test_4rotationsDonothing('rotateBottomClockwise')
    test_4rotationsDonothing('rotateTopAntiClockwise')
    test_4rotationsDonothing('rotateLeftAntiClockwise')
    test_4rotationsDonothing('rotateFrontAntiClockwise')
    test_4rotationsDonothing('rotateRightAntiClockwise')
    test_4rotationsDonothing('rotateBackAntiClockwise')
    test_4rotationsDonothing('rotateBottomAntiClockwise')
    test_4rotationsDonothing('_rotateCubeLeftToRight')
    test_4rotationsDonothing('_rotateCubeRightToLeft')
    test_4rotationsDonothing('_rotateCubeTopToBottom')
    test_4rotationsDonothing('_rotateCubeBottomToTop')
    test_4rotationsDonothing('_rotateCubeClockwise')
    test_4rotationsDonothing('_rotateCubeAntiClockwise')

    test_3and1oppositeOperations('rotateTopClockwise', 'rotateTopAntiClockwise')
    test_3and1oppositeOperations('rotateTopAntiClockwise', 'rotateTopClockwise')
    test_3and1oppositeOperations('rotateLeftClockwise', 'rotateLeftAntiClockwise')
    test_3and1oppositeOperations('rotateLeftAntiClockwise', 'rotateLeftClockwise')
    test_3and1oppositeOperations('rotateFrontClockwise', 'rotateFrontAntiClockwise')
    test_3and1oppositeOperations('rotateFrontAntiClockwise', 'rotateFrontClockwise')
    test_3and1oppositeOperations('rotateRightClockwise', 'rotateRightAntiClockwise')
    test_3and1oppositeOperations('rotateRightAntiClockwise', 'rotateRightClockwise')
    test_3and1oppositeOperations('rotateBackClockwise', 'rotateBackAntiClockwise')
    test_3and1oppositeOperations('rotateBackAntiClockwise', 'rotateBackClockwise')
    test_3and1oppositeOperations('rotateBottomClockwise', 'rotateBottomAntiClockwise')
    test_3and1oppositeOperations('rotateBottomAntiClockwise', 'rotateBottomClockwise')
    test_3and1oppositeOperations('_rotateCubeLeftToRight','_rotateCubeRightToLeft')
    test_3and1oppositeOperations('_rotateCubeRightToLeft','_rotateCubeLeftToRight')
    test_3and1oppositeOperations('_rotateCubeTopToBottom','_rotateCubeBottomToTop')
    test_3and1oppositeOperations('_rotateCubeBottomToTop','_rotateCubeTopToBottom')
    test_3and1oppositeOperations('_rotateCubeClockwise','_rotateCubeAntiClockwise')
    test_3and1oppositeOperations('_rotateCubeAntiClockwise','_rotateCubeClockwise')



if __name__ == "__main__":
    c = RubicCube()
    c.print()
    print('\n\n----------------------------')
    print('-------TOP ROTATION---------')
    c.rotateTopClockwise()
    c.print()

    print('\n\n----------------------------')
    print('-------FRONT ROTATION---------')
    c.rotateFrontClockwise()
    c.print()

    print('\n\n----------------------------------------')
    c = RubicCube()
    c.print()
    print('-------CUBE LEFT->RIGHT ROTATION---------')
    c._rotateCubeLeftToRight()
    c.print()

    runTests()
