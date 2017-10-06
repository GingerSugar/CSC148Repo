from typing import TypeVar, List, Generic

T = TypeVar("T")


class EmptyStackError(Exception):
    pass


class Stack(Generic[T]):
    items_ = List[T]

    def __init__(self):
        self.items_ = []

    def push(self, item: T) -> None:
        self.items_.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyStackError
        return self.items_.pop()

    def is_empty(self) -> bool:
        return len(self.items_) == 0
