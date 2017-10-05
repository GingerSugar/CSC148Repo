from labs.lab4.stack import Stack


class StackEmptyError(Exception):
    pass


def main():
    main_stack: Stack[str] = Stack[str]()
    undo_stack: Stack[str] = Stack[str]()

    while True:
        user_input = input("Enter next operation: ")
        if user_input == 'UNDO':
            if main_stack.is_empty():
                raise StackEmptyError
            else:
                current = main_stack.pop()
                print(current)
                undo_stack.push(current)
        elif user_input == 'REDO':
            if undo_stack.is_empty():
                raise StackEmptyError
            else:
                current = undo_stack.pop()
                print(current)
                main_stack.push(current)
        else:
            main_stack.push(user_input)
            while not undo_stack.is_empty():
                undo_stack.pop()


if __name__ == "__main__":
    main()
