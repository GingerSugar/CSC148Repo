from BracketEvaluator import is_balanced


class EquationManager:
    def __init__(self, equation: str):
        pass


class Equation:
    _equation: str
    id_: int

    def __init__(self, equation: str):
        self._equation = equation

    def get_equation_str(self) -> str:
        return self._equation

    def prep(self) -> "Equation":
        self._equation = "".join(self._equation.split())
        return self


def main():
    pass


if __name__ == "__main__":
    main()
