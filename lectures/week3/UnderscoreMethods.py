class MyClass:
    """MyClass inherits object by default

    === Attributes ===
    foo: an integer
    """

    foo: int  # MyClass HAS foo, it IS an object

    def __init__(self, foo: int):
        self.foo = foo

    def __str__(self):
        return f"FOO: {self.foo}"


class MyOtherClass(MyClass):
    """MyOtherClass inherits MyClass, and MyClass inherits object,
    so MyOtherClass is also able to reference object methods

    === Attributes ===
    foo: an integer
    bar: a string
    """

    bar: str  # MyOtherClass HAS bar, it IS a MyClass and object

    def __init__(self, foo: int, bar: str):
        super().__init__(foo)
        self.bar = bar

    def __str__(self):
        return f"FOO: {self.foo}, BAR: {self.bar}"
