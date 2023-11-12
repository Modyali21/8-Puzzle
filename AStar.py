import heapq
import time
from Node import Node


def getCoordinate(index: int) -> tuple[int, int]:
    return (index // 3, index % 3)


def getManhattanDistance(index: int, value: int) -> int:
    currentCell = getCoordinate(index)
    goal = getCoordinate(value)
    return abs(currentCell[0] - goal[0]) + abs(currentCell[1] - goal[1])


def getHeuristic(node: Node) -> int:
    state = node.state
    sum = 0
    for index, value in enumerate(state):
        if value == 0:
            continue
        sum += getManhattanDistance(index, value)
    return sum


def searchFrontier(frontier: list[tuple[int, int, Node]], node: Node) -> int:
    for index, item in enumerate(frontier):
        if item[2] == node:
            return index
    return -1


def aStar(initialState: Node, goal: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]):
    maxDepth = 0
    # fmt: off
    frontier: list[tuple[int, int, Node]] = []  # the frontier in this case is a priority queue
    # fmt: on
    heapq.heappush(
        frontier, (getHeuristic(initialState), str(initialState), 0, initialState)
    )
    frontierSet = set()
    frontierSet.add(str(initialState))
    explored: set[Node] = set()  # a set that will hold explored nodes
    count = 1  # works as a tie breaker, we choose the oldest entry
    while frontier:
        currentNode = heapq.heappop(frontier)[3]
        maxDepth = max(maxDepth, currentNode.depth)
        currentState = str(currentNode)
        if currentState in explored:
            continue
        explored.add(currentState)
        frontierSet.remove(currentState)

        if currentNode.state == goal:
            print("found")
            return True, len(explored), currentNode, maxDepth

        neighbours = currentNode.genStates()
        for neighbour in neighbours:
            state = str(neighbour)
            if state not in explored and state not in frontierSet:
                heapq.heappush(
                    frontier,
                    (
                        getHeuristic(neighbour) + neighbour.depth,
                        state,
                        count,
                        neighbour,
                    ),
                )
                frontierSet.add(state)
                count += 1
            elif state in frontierSet:
                heapq.heappush(
                    frontier,
                    (
                        getHeuristic(neighbour) + neighbour.depth,
                        state,
                        count,
                        neighbour,
                    ),
                )
                count += 1
    print("not found")
    return False, len(explored), currentNode, maxDepth


if __name__ == "__main__":
    x = time.time()
    print(len(aStar(Node([8, 0, 6, 5, 4, 7, 2, 3, 1]))[1]))
    print(time.time() - x)
    x = time.time()
    print(len(aStar(Node([1, 2, 4, 5, 7, 3, 8, 6, 0]))[1]))
    print(time.time() - x)
