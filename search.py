# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #first we define our stack
    #each element of our stack consists of: ((x,y),[path])
    #where (x,y) is the current position and [path] is the path taken to get there
    #note that the current position comes from problem class
    stk = util.Stack()

    #visitedPos holds all of the visited positions already (this is required for
    #the graph-search implementation of DFS)
    visitedPos = []

    #push starting state onto the stack with an empty path
    stk.push((problem.getStartState(),[]))

    #Then we can start looping, note our loop condition is if the stack is empty
    #if the stack is empty at any point we failed to find a solution

    """
        Note that what's happening here is as follows:
        First we pop a state off the stack, and grab it's position and path history
        Then we append that position to the listed of visited positions
        If that position is a goal state, then we return the path we took to reach it
        
        However, if it's not a goal state, we use the problem class to get a list of successors
        Then, we check to make sure we actually have successors
        If we DON'T have successors that path is a dead end and we just ditch the state, and move
        to the next node on the stack.
        If we DO have successors, we iterate through them until we find one that we haven't visited yet
        Then push that onto the stack after calculating the new path
        
        Note that this is DFS because we are always expanding the first unvisited successor we see.
    """
    while(not stk.isEmpty()):

        #since our stack elements contain two elements
        #we have to fetch them both like this
        currentPos,currentPath = stk.pop()

        #then we append the currentPos to the list of visited positions
        visitedPos.append(currentPos)

        #check if current state is a goal state, if it is, return the path
        if (problem.isGoalState(currentPos)):
            return currentPath;

        #obtain the list of successors from our currentPos
        successors = problem.getSuccessors(currentPos)

        #if we have successors, note that these successors have a position and the path to get there
        if (len(successors) != 0):
            #iterate through them
            for state in successors:
                #if we find one that has not already been visisted
                if (state[0] not in visitedPos):
                    #calculate the new path (currentPath + path to reach new state's position)
                    newPath = currentPath + [state[1]]
                    #push it onto the stack with the new path
                    stk.push((state[0],newPath))

    return [];

def breadthFirstSearch(problem):
    """
    Basically same approach as DFS except we use a queue instead, and have a slight conditional change in our successors area
    """
    #first we define our stack
    #each element of our stack consists of: ((x,y),[path])
    #where (x,y) is the current position and [path] is the path taken to get there
    #note that the current position comes from problem class
    q = util.Queue()

    #visitedPos holds all of the visited positions already (this is required for
    #the graph-search implementation of BFS)
    visitedPos = []

    #push starting state onto the stack with an empty path
    q.push((problem.getStartState(),[]))

    #Then we can start looping, note our loop condition is if the stack is empty
    #if the stack is empty at any point we failed to find a solution
    while(not q.isEmpty()):

        #since our stack elements contain two elements
        #we have to fetch them both like this
        currentPos,currentPath = q.pop()
        #print("Currently Visiting:", currentPos, "\nPath=", end="");
        #print(currentPath);
        #then we append the currentPos to the list of visited positions
        visitedPos.append(currentPos)

        #check if current state is a goal state, if it is, return the path
        if (problem.isGoalState(currentPos)):
            return currentPath;

        #obtain the list of successors from our currentPos
        successors = problem.getSuccessors(currentPos)

        #if we have successors, note that these successors have a position and the path to get there
        if (len(successors) != 0):
            #iterate through them
            for state in successors:
                #if we find one that has not already been visisted
                if ((state[0] not in visitedPos) and (state[0] not in (stateQ[0] for stateQ in q.list))):
                    #calculate the new path (currentPath + path to reach new state's position)
                    newPath = currentPath + [state[1]]
                    #push it onto the stack with the new path
                    q.push((state[0],newPath))

    return [];

def uniformCostSearch(problem):
    q = util.PriorityQueue()

    visitedPos = []

    q.push((problem.getStartState(),[]), 0)

    while(not q.isEmpty()):


        currentPos,currentPath = q.pop()

        visitedPos.append(currentPos)

        if (problem.isGoalState(currentPos)):
            return currentPath;

        successors = problem.getSuccessors(currentPos)

        if (len(successors) != 0):
            for state in successors:
                if (state[0] not in visitedPos) and (state[0] not in (stateQ[2][0] for stateQ in q.heap)):
                    newPath = currentPath + [state[1]]
                    q.push((state[0],newPath),problem.getCostOfActions(newPath))

                elif (state[0] not in visitedPos) and (state[0] in (stateQ[2][0] for stateQ in q.heap)):
                    for stateQ in q.heap:
                        if stateQ[2][0] == state[0]:
                            oldPriority = problem.getCostOfActions(stateQ[2][1])

                    newPriority = problem.getCostOfActions(currentPath + [state[1]])

                    # State is cheaper with his hew father -> update and fix parent #
                    if oldPriority > newPriority:
                        newPath = currentPath + [state[1]]
                        q.update((state[0],newPath),newPriority)

    return [];

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #define priority queue
    q = util.PriorityQueue()

    visitedPos = []
    #format we store things is similar to UCS, but with the A* cost metric of f(n)=h(n)+g(n)
    #problem.getCostOfActions() = g(n)
    #heuristic(state, problem) = f(n)
    q.push((problem.getStartState(), {}), (problem.getCostOfActions({}) + heuristic(problem.getStartState(), problem)))
    #same thing as the other searches basically, we just store our vaules differently so the priority queue operates differently
    while (not q.isEmpty()):
        currentPos,currentPath = q.pop()

        if problem.isGoalState(currentPos):
            return currentPath

        if not currentPos in visitedPos: #didn't need this check in previous search algs but needed it here, interesting
            visitedPos.append(currentPos)
            successors = problem.getSuccessors(currentPos)

            for state in successors: #priority queue manages order for us so we don't have to use if statements
                newPath = list(currentPath)
                newPath.append(state[1])
                q.push((state[0], newPath), (problem.getCostOfActions(newPath) + heuristic(state[0], problem)))
    return []

direction = {'North': 'South', 'East': 'West', 'South': 'North', 'West': 'East'}


def bDSearchMM0(problem):

    # mm0 is essentially bidrectional BFS
    # initialize everything we need, so 2 queues, and 2 visited position dicts
    q1, q2 = util.Queue(),  util.Queue()

    # Note these are dicts because each key is a visited position
    # the value for each of those keys is the path we took to get there
    visitedPos1, visitedPos2 = {}, {}

    # Set up initial starting conditions
    # so q1 starts from start and q2 starts from goal
    q1.push(problem.getStartState())
    q2.push(problem.goal)

    # Mark those states as visited
    visitedPos1[problem.getStartState()] = ''
    visitedPos2[problem.goal] = ''

    # Run until either queue is empty meaning there is no path from start to goal
    while not q1.isEmpty() and not q2.isEmpty():
        # While q2 is not empty
        while not q1.isEmpty():
            # Pop current pos and current path to get to that ops off priority queue
            cpos1 = q1.pop()

            # Check if we have a goal state
            if problem.isGoalState(cpos1, visitedPos2):
                revd = [direction[x] for x in visitedPos2[cpos1]]
                # If so, reverse the other path that other search took to meet us, then append
                return visitedPos1[cpos1] + revd[::-1]

            # If no goal state, expand all successors
            for state in problem.getSuccessors(cpos1):  # Priority queue manages order for us so we don't have to use if statements
                if state[0] in visitedPos1: # If already visited, don't visit again
                    continue

                # Push each state and mark visited
                q1.push(state[0])
                visitedPos1[state[0]] = list(visitedPos1[cpos1]) + [state[1]]

        # Second bfs instance, same as first just searching in reverse!
        while not q2.isEmpty():
            cpos2 = q2.pop()

            if problem.isGoalState(cpos2, visitedPos1):
                return [direction[x] for x in visitedPos1[cpos2]][::-1] + visitedPos2[cpos2]

            for state in problem.getSuccessors(cpos2):
                if state[0] in visitedPos2:
                    continue

                q2.push(state[0])
                visitedPos2[state[0]] = list(visitedPos2[cpos2]) + [state[1]]
    return []


def bDSearchMM(problem, heuristic):

    # Now MM search, which is astar in each direction
    q1, q2 = util.PriorityQueue(), util.PriorityQueue()

    # Declare dict to store visited positions
    visitedPos1,visitedPos2 = {}, {}

    # Add both starting states to visited Dicts
    visitedPos1[problem.getStartState()] = []
    visitedPos2[problem.goal] = []

    # We use a priority que to store nodes in the frontier with the A* cost metric of f(n)=h(n)+g(n)
    # problem.getCostOfActions() = g(n)
    # heuristic(state, problem) = f(n)
    q1.push((problem.getStartState()), (problem.getCostOfActions({}) + heuristic(problem.getStartState(), problem, "g")))
    q2.push((problem.goal), (problem.getCostOfActions({}) + heuristic(problem.goal, problem, "s")))

    # Run while both frontier's are not empty and return [] in the case the goal is not reachable from the start
    while not q1.isEmpty() and not q2.isEmpty():

        # Run both searches at simultaneously
        cpos1 = q1.pop()

        if problem.isGoalState(cpos1, visitedPos2):
            revd = [direction[x] for x in visitedPos2[cpos1]]
            return visitedPos1[cpos1] + revd[::-1]

        successors = problem.getSuccessors(cpos1)

        for state in successors:  # priority queue manages order for us so we don't have to use if statements
            if state[0] in visitedPos1:
                continue

            visitedPos1[state[0]] = list(visitedPos1[cpos1]) + [state[1]]
            q1.push(state[0], (problem.getCostOfActions(visitedPos1[state[0]]) + heuristic(state[0], problem, "g")))

        cpos2 = q2.pop()

        if problem.isGoalState(cpos2, visitedPos1):
            return visitedPos1[cpos2] + [direction[x] for x in visitedPos2[cpos2]][::-1]

        successors = problem.getSuccessors(cpos2)

        for state in successors:  # priority queue manages order for us so we don't have to use if statements
            if state[0] in visitedPos2:
                continue

            visitedPos2[state[0]] = list(visitedPos2[cpos2]) + [state[1]]
            q2.push(state[0],
                    (problem.getCostOfActions(visitedPos2[state[0]]) + heuristic(state[0], problem, "s")))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bd0 = bDSearchMM0
bd = bDSearchMM
