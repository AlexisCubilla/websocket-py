import asyncio
from jmetal.core.solution import (FloatSolution)
from jmetal.core.problem import (FloatProblem)

from OptimizerWebSocket import WsClient


class CustomProblem(FloatProblem):
   
    def __init__(self):
        super(CustomProblem, self).__init__()
        self.functions = []
        self.constraints = []
        self.problem_name = None
        self.objetives_count = 0

    def set_name(self, name) -> "CustomProblem":
        self.problem_name = name

        return self

    def add_function(self, function) -> "CustomProblem":
        self.functions.append(function)

        return self

    def add_constraint(self, constraint) -> "CustomProblem":
        self.constraints.append(constraint)

        return self

    def add_variable(self, lower_bound, upper_bound) -> "CustomProblem":
        self.lower_bound.append(lower_bound)
        self.upper_bound.append(upper_bound)

        return self

    def number_of_objectives(self) -> int:
        # return len(self.functions)
        return self.objetives_count

    def number_of_constraints(self) -> int:
        return len(self.constraints)

    def evaluate(self, solution: FloatSolution) -> None:
        ws = WsClient("ws://localhost:8000")
        objetives=eval(ws.send_data(solution.variables))

        for i in range(self.number_of_objectives()):
            solution.objectives[i] =objetives[i]
       
       
        # for i in range(self.number_of_constraints()):
        #     solution.constraints[i] = self.constraints[i](solution.variables)

    def name(self) -> str:
        return self.problem_name
    

    