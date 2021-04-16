from abc import ABC, abstractmethod
from RubicCube import RubicCube


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
        # TODO this function should return True if the cube state in self is the same as the cube state in anotherState
        pass


    #This funciton must generate the search states produced after applying the operations on self
    def getDescendants(self):
        #TODO. My suggestion is to create a list with the names of the operations as strings, ['rotateTopClockwise, ...]
        #Then, a loop goes over the operations and everty time, it clones the current states, applies the corresponding
        #operation with the function
        # getattr(newCube, operation)()
        #and append the new state into a list which is returned at the end of the function
        #Recall that you should return RubickSearchStates with depth incremented, self as the best parent, and the
        #operation that produced it
        pass

    #This function is similar to the previous one, but the RubikSearchStates that it creates should have the inverse
    #operations, instead of those that produced them. My suggestion is to create a dictionary with the inverse operation
    #for each operation on the Rubik cube
    def getAntecedents(self):
        #TODO
        pass


    #This function returns a list with the operations from the initial state to this one, according to the
    #selected best parents. Nothing to do here.
    def getPath(self):
        path = []
        if self._bestParent is not None:
            path = self._bestParent.getPath

        path.append(self._operation)
        return path


#This class is in charge of applying the Bidirectional search
class BidirectionalSearch():

    #The initialization receives the initial and the goal states, and this should create the frontier and explored
    #lists of the two searches. My suggestion is to use lists. Besides, the frontiers should contain
    #RubikSearchStates of the initial and goal states
    def __init__(self, initialState, goalState):
        #TODO
        pass


    #This function gets the first state of the frontier structure in the top search.
    #Then, it checks if the same state is in the frontier or the explored structures of the bottom search.
    #In that case, it gets the path of the state from the bottom search, invert it, and append it to the path
    #of the state of the top search. And returns it.
    #Otherwise, it generates the descendants of the state, checks that they are not in the frontier or the explored
    #states of the top search, and in this case, insert it in frontier at the end.
    def _iterateTopSearch(self):
        #TODO
        pass

    #This function is similar to the previous one, but instead of generating the descendants, it generates
    #the antecendents of the state (obviously, using frontier and explored from the bottom search).
    # In addition, if this function finds the state in the the top search, it creates the path the same way.
    # This means, the path from the state from the top search is taken as it is, and the path from the state from
    # the bottom search should be inverted.
    def _iterateBottomSearch(self):
        #TODO
        pass

    #This method should iterate while there are RubikSearchStates in any frontier, calling iterateTopSearch and
    #iterateBottomSearch alterantively, and returning the solution as soon as it is found.
    def run(self):
        #TODO
        pass



if __name__ == "__main__":
    c1 = RubicCube()
    c1.setStandardSolution()
    c2 = c1.clone()

    thisIsTheTest = False

    while not thisIsTheTest:
        c1.setStandardSolution()
        ops = c1.shuffle(4)

        search = BidirectionalSearch(c1,c2)
        result = search.run()
        result.pop()
        result.pop(0)

        if len(result) == len(ops):
            thisIsTheTest = True
            print(ops)
            print(result)
        else:
            print("Starting again because I found a shorter (better) solution")
