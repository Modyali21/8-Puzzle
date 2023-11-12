from __future__ import annotations
from queue import LifoQueue
import copy
from typing import Literal

class Node:
    state: list[int]
    parent: Node | None 
    depth: int
    action: Literal["up", "right", "down", "left"] | None

    def __init__(
        self,
        state: list[int],
        parent: Node | None = None,
        action: Literal["up", "right", "down", "left"] | None = None,
        depth: int = 0,
    ) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __str__(self) -> str:
        return f"{self.state}"
    
    def __eq__(self, __value: Node) -> bool:
        return self.state == __value.state

    def genStates(self) -> list[Node]:
        neighbours = []
        zero = self.state.index(0)
        if zero not in [0, 1, 2]:
            newState = self.swap(self.state, zero, -3)
            neighbours.append(Node(newState, self, "up", self.depth + 1))
        if zero not in [2, 5, 8]:
            newState = self.swap(self.state, zero, 1)
            neighbours.append(Node(newState, self, "right", self.depth + 1))
        if zero not in [6, 7, 8]:
            newState = self.swap(self.state, zero, 3)
            neighbours.append(Node(newState, self, "down", self.depth + 1))
        if zero not in [0, 3, 6]:
            newState = self.swap(self.state, zero, -1)
            neighbours.append(Node(newState, self, "left", self.depth + 1))
        return neighbours

    def swap(slef, state, zeroIndex, position):
        newState = copy.deepcopy(state)
        temp = newState[zeroIndex + position]
        newState[zeroIndex + position] = newState[zeroIndex]
        newState[zeroIndex] = temp
        return newState

    def formPath(self):
        finalNode = self
        path = LifoQueue()
        while finalNode is not None:
            path.put(finalNode.state)
            finalNode = finalNode.parent
        return path

    def getPath(self, path):
        while not path.empty():
            print(path.get().state)