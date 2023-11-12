from queue import LifoQueue
import time

from Node import Node



def dfs(initialState:Node,goal = [0,1,2,3,4,5,6,7,8]) :
    
    maxDepth =0
    
    frontier = LifoQueue()
    frontierSet = set()
    explored: set[Node] = set()  # a set that will hold explored nodes
    
    frontier.put(initialState)
    frontierSet.add(str(initialState))
    
    



    while not frontier.empty() :
        
        currentNode : Node = frontier.get()
        state = str(currentNode.state)
        
        frontierSet.remove(state)
        explored.add(state)

        maxDepth = max(maxDepth, currentNode.depth)
        
        if(currentNode.state == goal) :
            print("found")
            return True, len(explored), currentNode, maxDepth
        else :
            neighbours = currentNode.genStates()
            for i in range(len(neighbours)) :
                neighbour = str(neighbours[len(neighbours)-1-i].state)
                if neighbour not in frontierSet and neighbour not in explored :
                        frontier.put(neighbours[len(neighbours)-1-i])
                        frontierSet.add(neighbour)
    print("not found")
    return False, len(explored), currentNode, maxDepth


initialState = Node([8,0,6,5,4,7,2,3,1])
start = time.time()
out = dfs(initialState)
end = time.time()