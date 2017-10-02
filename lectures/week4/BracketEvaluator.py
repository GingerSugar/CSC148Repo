from Stack import Stack


def is_balanced(equation: str) -> bool:
    s = Stack()
    for i in equation:
        if i == "(":
            s.push("(")
        elif i == ")":
            if s.pop() != "(":
                break
        elif i == "{":
            s.push("{")
        elif i == "}":
            if s.pop() != "{":
                break
        elif i == "[":
            s.push("[")
        elif i == "]":
            if s.pop() != "[":
                break
    else:
        return True
    return False


if __name__ == "__main__":
    assert is_balanced("(x-3){}[]") is True
    assert is_balanced("{[}]") is False
