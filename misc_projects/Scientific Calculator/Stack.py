from typing import List


class Stack:
    """A stack is a Last in First out (LIFO, or FILO) list system."""
    _stack: List[object]

    def __init__(self):
        """Initializes an empty Stack object"""
        self._stack = []

    def push(self, elm: object) -> None:
        """Pushes a new object to the top of the stack"""
        self._stack.append(elm)

    def pop(self) -> object:
        """Pops an object off the top of the list and returns it"""
        return self._stack.pop()

    def is_empty(self) -> bool:
        """Returns if the Stack is empty or not"""
        return len(self._stack) == 0

    def __len__(self) -> int:
        return len(self._stack)
