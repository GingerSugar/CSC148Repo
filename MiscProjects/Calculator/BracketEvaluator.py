from MiscProjects.Calculator.Stack import Stack

_BRACKETS = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def is_balanced(equation: str) -> bool:
    bracket_stack = Stack()
    for i in equation:
        if i in _BRACKETS.values():
            bracket_stack.push(i)
        elif i in _BRACKETS.keys():
            if bracket_stack.pop() != _BRACKETS[i]:
                return False
    return bracket_stack.is_empty()


if __name__ == "__main__":
    while True:
        s = input("Enter equation: ")
        print(f"Equation {s} is balanced: {is_balanced(s)}")
