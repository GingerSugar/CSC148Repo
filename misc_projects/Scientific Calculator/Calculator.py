import uuid
from typing import Dict
import BracketEvaluator
import re


class EquationNotBalancedError(Exception):
    pass


class EquationManager:
    equations: Dict[str, "Equation"]
    _root: "Equation"

    def __init__(self, equation: str):
        if not BracketEvaluator.is_balanced(equation):
            raise EquationNotBalancedError

        self.equations = {}
        self._root = Equation(equation, self, uuid.uuid4())

    def evaluate(self):
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

    def prep(self) -> "Equation":
        self._equation = "".join(self._equation.split())
        # next_ = re.search(r'(\(.*?\))', self._equation)

        counter = 0
        start_ind = -1
        end_ind = -1
        for i, j in enumerate(self._equation):
            if j == "(":
                if counter == 0:
                    start_ind = i
                counter += 1
            elif j == ")":
                counter -= 1
                if counter == 0:
                    end_ind = i
                    break

        if start_ind != -1 and end_ind != -1:
            next_ = self._equation[start_ind: end_ind + 1]
        else:
            return self
        print(next_)

        id_ = uuid.uuid4()
        self._equation = self._equation.replace(next_, "#{}#".format(id_))
        Equation(next_[1:-1], self._manager, id_)
        self.prep()
        return self

    def __str__(self):
        return self._equation

    def evaluate(self):

        regex = r"(#[\w-]{36}#|\d+|[+-/*^])"
        toks = re.findall(regex, self._equation)

        print(toks)
        for i in toks:
            pass


def main():
    em = EquationManager("2 + (2 - (2(3/6))) / 6(1-3)")
    for i, j in em.equations.items():
        print(i, j)
    em.evaluate()


if __name__ == "__main__":
    main()
