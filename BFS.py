from queue import SimpleQueue
import time

from Node import Node



def bfs(initialState:Node,goal = [0,1,2,3,4,5,6,7,8]) :
    
    maxDepth =0
    
    frontier = SimpleQueue()
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
            for neighbourNode in neighbours :
                neighbour = str(neighbourNode.state)
                if neighbour not in frontierSet and neighbour not in explored :
                        frontier.put(neighbourNode)
                        frontierSet.add(neighbour)
    print("not found")
    return False, len(explored), currentNode, maxDepth


initialState = Node([8,0,6,5,4,7,2,3,1])
start = time.time()
out = bfs(initialState)
end = time.time()