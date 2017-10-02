from typing import List


class Stack:
    _stack: List[object]

    def __init__(self):
        self.stack = []

    def push(self, elm: object) -> None:
        self.stack.append(elm)

    def pop(self) -> object:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0
