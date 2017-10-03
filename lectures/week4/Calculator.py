from BracketEvaluator import is_balanced
from typing import Dict
import uuid
import re


class EquationManager:
    equations: Dict[str, "Equation"]
    _root: "Equation"

    def __init__(self, equation: str):
        root = Equation(equation, self, uuid.uuid4())

    def evaluate(self) -> str:
        self._root.evaluate()

    def put_equation(self, id_: str, equation: "Equation"):
        self.equations[id_] = equation


class Equation:
    _equation: str
    _manager: EquationManager
    id_: int

    def __init__(self, equation: str, manager: EquationManager, id: str):
        self._equation = equation
        self._manager = manager
        self.prep()
        self.id_ = id
        manager.put_equation(self.id_, self)

    def get_equation_str(self) -> str:
        return self._equation

    def prep(self):
        self._equation = "".join(self._equation.split())
        next_ = re.search(r'\((.*?)\)', self._equation).group(1)
        id_ = uuid.uuid4()
        self._equation.replace(next_, f"#{id_}")
        Equation(next_, self._manager, id_)
        return self

    def __str__(self):
        return self._equation

    def evaluate(self):
        for i in self._equation:
            pass
        pass


def main():
    em = EquationManager("2 + (2 - 3) / 6")
    for i, j in em.equations.values():
        print(i, j)


if __name__ == "__main__":
    main()
