import sys
from abc import ABC, abstractmethod

from MagicCube.cube_interactive import Cube
from RubicCube import RubicCube
from matplotlib import pyplot as plt

#This is an abstract class to represent what a search state should look like.
#The fact is that search states used by graph-based search methods have to store, at least, their costs and links
#to their best parent.
class SearchState(ABC):
    def __init__(self):
        self.depth = 0
        self._bestParent = None;

    #In addition, search states should be able to produce their descendants, which is not implemented in
    #this abstract class. Nothing to do here.
    @abstractmethod
    def getDescendants(self):
        pass

    #Search states should also be able to check if they represent the same state as another. This
    #method should be defined in the corresponding subclasses. Nothing to do here
    @abstractmethod
    def equals(self, anotherState):
        pass




#This is the actual search state we will use, which is a subclass of the abstract SearchState and has got a
#property to store the state of the rubik cube, and the operation applied on its best parent to get this state
class RubikSearchState(SearchState):

    def __init__(self, cube, depth, bestParent, operation):
        super().__init__()
        self._cube = cube
        self.depth = depth
        self._bestParent = bestParent
        self._operation = operation

    def equals(self, anotherState):
        #this function should return True if the cube state in self is the same as the cube state in anotherState
        return self._cube.equals(anotherState._cube)


    #This funciton must generate the search states produced after applying the operations on self
    def getDescendants(self):
        #My suggestion is to create a list with the names of the operations as strings, ['rotateTopClockwise, ...]
        #Then, a loop goes over the operations and everty time, it clones the current states, applies the corresponding
        #operation with the function
        # getattr(newCube, operation)()
        #and append the new state into a list which is returned at the end of the function
        #Recall that you should return RubickSearchStates with depth incremented, self as the best parent, and the
        #operation that produced it

        ops = ['rotateTopClockwise',
              'rotateTopAntiClockwise',
              'rotateLeftClockwise',
              'rotateLeftAntiClockwise',
              'rotateFrontClockwise',
              'rotateFrontAntiClockwise',
              'rotateRightClockwise',
              'rotateRightAntiClockwise',
              'rotateBackClockwise',
              'rotateBackAntiClockwise',
              'rotateBottomClockwise',
              'rotateBottomAntiClockwise']

        descendants = []

        for op in ops:
            cube = self._cube.clone()
            getattr(cube, op)()
            descendants.append(RubikSearchState(cube, self.depth+1, self, op))

        return descendants

    #This function is similar to the previous one, but the RubikSearchStates that it creates should have the inverse
    #operations, instead of those that produced them. My suggestion is to create a dictionary with the inverse operation
    #for each operation on the Rubik cube
    def getAntecedents(self):
        ops = ['rotateTopClockwise',
              'rotateTopAntiClockwise',
              'rotateLeftClockwise',
              'rotateLeftAntiClockwise',
              'rotateFrontClockwise',
              'rotateFrontAntiClockwise',
              'rotateRightClockwise',
              'rotateRightAntiClockwise',
              'rotateBackClockwise',
              'rotateBackAntiClockwise',
              'rotateBottomClockwise',
              'rotateBottomAntiClockwise']

        inverseOperation = {
            'rotateTopClockwise':'rotateTopAntiClockwise',
            'rotateTopAntiClockwise':'rotateTopClockwise',
            'rotateLeftClockwise':'rotateLeftAntiClockwise',
            'rotateLeftAntiClockwise':'rotateLeftClockwise',
            'rotateFrontClockwise':'rotateFrontAntiClockwise',
            'rotateFrontAntiClockwise':'rotateFrontClockwise',
            'rotateRightClockwise':'rotateRightAntiClockwise',
            'rotateRightAntiClockwise':'rotateRightClockwise',
            'rotateBackClockwise':'rotateBackAntiClockwise',
            'rotateBackAntiClockwise':'rotateBackClockwise',
            'rotateBottomClockwise':'rotateBottomAntiClockwise',
            'rotateBottomAntiClockwise':'rotateBottomClockwise'
        }

        antecedents = []

        for op in ops:
            cube = self._cube.clone()
            getattr(cube, op)()
            antecedents.append(RubikSearchState(cube, self.depth + 1, self, inverseOperation[op]))

        return antecedents


    #This function returns a list with the operations from the initial state to this one, according to the
    #selected best parents. Nothing to do here.
    def getPath(self):
        path = []
        if self._bestParent is not None:
            path = self._bestParent.getPath()

        path.append(self._operation)
        return path


#This class is in charge of applying the Bidirectional search
class BidirectionalSearch():

    #The initialization receives the initial and the goal states, and this should create the frontier and explored
    #lists of the two searches. My suggestion is to use lists. Besides, the frontiers should contain
    #RubikSearchStates of the initial and goal states
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState
        self.top_frontera = [RubikSearchState(initialState, 0, None, None)]
        self.top_explorados = []
        self.bottom_frontera = [RubikSearchState(goalState, 0, None, None)]
        self.bottom_explorados = []
        self.counter = 0


    #This function gets the first state of the frontier structure in the top search.
    #Then, it checks if the same state is in the frontier or the explored structures of the bottom search.
    #In that case, it gets the path of the state from the bottom search, invert it, and append it to the path
    #of the state of the top search. And returns it.
    #Otherwise, it generates the descendants of the state, checks that they are not in the frontier or the explored
    #states of the top search, and in this case, insert it in frontier at the end.
    def _iterateTopSearch(self):
        state = self.top_frontera.pop(0)
        for s in self.bottom_frontera:
            if state.equals(s):
                bottom_path = s.getPath()[::-1]
                top_path = state.getPath()
                return top_path + bottom_path

        for s in self.bottom_explorados:
            if state.equals(s):
                bottom_path = s.getPath()[::-1]
                top_path = state.getPath()
                return top_path + bottom_path

        descendants = state.getDescendants()
        for descendant in descendants:
            if descendant not in self.top_frontera and descendant not in self.top_explorados:
                self.top_frontera.append(descendant)

        self.top_explorados.append(state)
        return None

    #This function is similar to the previous one, but instead of generating the descendants, it generates
    #the antecendents of the state (obviously, using frontier and explored from the bottom search).
    # In addition, if this function finds the state in the the top search, it creates the path the same way.
    # This means, the path from the state from the top search is taken as it is, and the path from the state from
    # the bottom search should be inverted.
    def _iterateBottomSearch(self):
        state = self.bottom_frontera.pop(0)
        for s in self.top_frontera:
            if state.equals(s):
                bottom_path = state.getPath()[::-1]
                top_path = s.getPath()
                return top_path + bottom_path

        for s in self.top_explorados:
            if state.equals(s):
                bottom_path = state.getPath()[::-1]
                top_path = s.getPath()
                return top_path + bottom_path

        antecedents = state.getAntecedents()
        for antecedent in antecedents:
            if antecedent not in self.bottom_frontera and antecedent not in self.bottom_explorados:
                self.bottom_frontera.append(antecedent)

        self.bottom_explorados.append(state)
        return None

    #This method should iterate while there are RubikSearchStates in any frontier, calling iterateTopSearch and
    #iterateBottomSearch alterantively, and returning the solution as soon as it is found.
    def run(self):
        while len(self.top_frontera) > 0 or len(self.bottom_frontera) > 0:
            path = self._iterateTopSearch()
            if path is not None:
                return path
            path = self._iterateBottomSearch()
            if path is not None:
                return path


def drawCube(cube):
    c3 = cube.clone()
    c3._rotateClockwise(c3._top)
    c3._rotateClockwise(c3._left)
    c3._rotateClockwise(c3._right)
    c3._rotateClockwise(c3._bottom)
    c3._rotateClockwise(c3._front)
    c3._rotateClockwise(c3._back)
    cube_graph = Cube(N, arrays=[c3._top, c3._bottom, c3._left, c3._right, c3._back, c3._front])
    cube_graph.draw_interactive()
    plt.show()



if __name__ == "__main__":
    c1 = RubicCube()
    c1.setStandardSolution()
    c2 = c1.clone()
    N = 3  # Esto es una cosa que necesita el cube_interactive
    print("Impresión gráfica del cubo gracias a: https://github.com/davidwhogg/MagicCube")

    thisIsTheTest = False

    while not thisIsTheTest:
        c1.setStandardSolution()
        ops = c1.shuffle(6)

        search = BidirectionalSearch(c1,c2)
        result = search.run()
        result.pop()
        result.pop(0)

        if len(result) == len(ops):
            thisIsTheTest = True
            ops_traslation = {'rotateTopClockwise': 'u',
                              'rotateTopAntiClockwise': 'U',
                              'rotateLeftClockwise': 'l',
                              'rotateLeftAntiClockwise': 'L',
                              'rotateFrontClockwise': 'f',
                              'rotateFrontAntiClockwise': 'F',
                              'rotateRightClockwise': 'r',
                              'rotateRightAntiClockwise': 'R',
                              'rotateBackClockwise': 'b',
                              'rotateBackAntiClockwise': 'B',
                              'rotateBottomClockwise': 'd',
                              'rotateBottomAntiClockwise': 'D'}
            ops.reverse()
            print("Shuffle in reverse order:",ops)
            print("Solution:", result)
            operations = list(map(lambda x: ops_traslation[x], result))
            print("Press keys:", operations)
            thisIsTheTest = True
            drawCube(c1)
        else:
            print("Starting again because I found a shorter (better) solution")
