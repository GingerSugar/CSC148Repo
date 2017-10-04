import uuid
from typing import Dict


class EquationManager:
    equations: Dict[str, "Equation"]
    _root: "Equation"

    def __init__(self, equation: str):
        self.equations = {}
        self._root = Equation(equation, self, uuid.uuid4())

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
        # next_ = re.search(r'(\(.*?\))', self._equation)

        counter = 0
        start_ind = -1
        end_ind = -1
        for i, j in enumerate(self._equation):
            if j == "(":
                if counter == 0:
                    start_ind = i
                counter += 1
            elif j == "(":
                counter -= 1
                if counter == 0:
                    end_ind = i
                    break

        if start_ind != -1 or end_ind != -1:
            next_ = self._equation[start_ind: end_ind + 1]
        else:
            return

        id_ = uuid.uuid4()
        self._equation = self._equation.replace(next_, "#{}#".format(id_))
        Equation(next_[1:-1], self._manager, id_)
        return self

    def __str__(self):
        return self._equation

    def evaluate(self):
        for i in self._equation:
            pass
        pass


def main():
    em = EquationManager("2 + (2 - (2(3/6))) / 6")
    for i, j in em.equations.items():
        print(i, j)


if __name__ == "__main__":
    main()
