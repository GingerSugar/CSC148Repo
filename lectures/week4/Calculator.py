from BracketEvaluator import is_balanced
from typing import Dict
import uuid


class EquationManager:
    equations: Dict[str, "Equation"]
    _root: "Equation"

    def __init__(self, equation: str):
        root = Equation(equation, self)

    def evaluate(self) -> str:
        self._root.evaluate()

    def put_equation(self, id_: str, equation: "Equation"):
        self.equations[id_] = equation


class Equation:
    _equation: str
    _manager: EquationManager
    id_: int

    def __init__(self, equation: str, manager: EquationManager):
        self._equation = equation
        self._manager = manager
        self.prep()
        self.id_ = uuid.uuid4()

    def get_equation_str(self) -> str:
        return self._equation

    def prep(self):
        self._equation = "".join(self._equation.split())

        return self

    def evaluate(self):
        for i in self._equation:
            pass
        pass


def main():
    EquationManager("2 + (2 - 3) / 6").evaluate()


if __name__ == "__main__":
    main()
