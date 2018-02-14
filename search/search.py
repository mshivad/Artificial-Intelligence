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

def getPath(node):
    """
    Returns action path of a node
    """
    path = []
    while node[1] is not None:
        path.append(node[2])
        node = node[1]
    path.reverse()
    return path

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
	
    # initialize start node
    start_state = problem.getStartState()
    start_parent = None
    start_action = None
    start_node = (start_state, start_parent, start_action)
    # create stack for DFS and push the start node
    frontier = util.Stack()
    frontier.push(start_node)
    # initialize set of visited states
    visited_states = set()
    # DFS
    while True:
        # return if stack is empty
        if frontier.isEmpty():
            return
        # pop the last node of the stack
        node = frontier.pop()
        state = node[0]
        # if the state of the node is the goal state, return its path
        if problem.isGoalState(state):
            return getPath(node)
        # add the state of the node to the set of visited states, if not added already
        if state not in visited_states:
            visited_states.add(state)
            # push all the child nodes of the node into the stack
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_parent = node
                next_action = successor[1]
                next_node = (next_state, next_parent, next_action)
                frontier.push(next_node)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # initialize start node
    start_state = problem.getStartState()
    start_parent = None
    start_action = None
    start_node = (start_state, start_parent, start_action)
    # create queue for BFS and push the start node
    frontier = util.Queue()
    frontier.push(start_node)
    # initialize set of visited states
    visited_states = set()
    # BFS
    while True:
        # return if queue is empty
        if frontier.isEmpty():
            return
        # pop the first node of the queue
        node = frontier.pop()
        state = node[0]
        # if the state of the node is the goal state, return its path
        if problem.isGoalState(state):
            return getPath(node)
        # add the state of the node to the set of visited states, if not added already
        if state not in visited_states:
            visited_states.add(state)
            # push all the child nodes of the node into the queue
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_parent = node
                next_action = successor[1]
                next_node = (next_state, next_parent, next_action)
                frontier.push(next_node)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # initialize start node
    start_state = problem.getStartState()
    start_parent = None
    start_action = None
    start_cost = 0
    start_node = (start_state, start_parent, start_action, start_cost)
    # create priority queue for UCS and push the start node
    frontier = util.PriorityQueue()
    frontier.push(start_node, start_cost)
    # initialize set of visited states
    visited_states = set()
    # UCS
    while True:
        # return if priority queue is empty
        if frontier.isEmpty():
            return
        # pop the first node of the priority queue
        node = frontier.pop()
        state = node[0]
        # if the state of the node is the goal state, return its path
        if problem.isGoalState(state):
            return getPath(node)
        # add the state of the node to the set of visited states, if not added already
        if state not in visited_states:
            visited_states.add(state)
            # push all the child nodes of the node into the priority queue
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_parent = node
                next_action = successor[1]
                next_cost = node[3] + successor[2]
                next_node = (next_state, next_parent, next_action, next_cost)
                frontier.push(next_node, next_cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # initialize start node
    start_state = problem.getStartState()
    start_parent = None
    start_action = None
    start_cost = 0
    start_node = (start_state, start_parent, start_action, start_cost)
    # create priority queue for A* search and push the start node
    frontier = util.PriorityQueue()
    h = start_cost + heuristic(start_state, problem) # add the heuristic at the state to the cost
    frontier.push(start_node, h)
    # initialize set of visited states
    visited_states = set()
    # A* search
    while True:
        # return if priority queue is empty
        if frontier.isEmpty():
            return
        # pop the first node of the priority queue
        node = frontier.pop()
        state = node[0]
        # if the state of the node is the goal state, return its path
        if problem.isGoalState(state):
            return getPath(node)
        # add the state of the node to the set of visited states, if not added already
        if state not in visited_states:
            visited_states.add(state)
            # push all the child nodes of the node into the priority queue
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_parent = node
                next_action = successor[1]
                next_cost = node[3] + successor[2]
                next_node = (next_state, next_parent, next_action, next_cost)
                h = next_cost + heuristic(next_state, problem) # add the heuristic at the state to the cost
                frontier.push(next_node, h)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
