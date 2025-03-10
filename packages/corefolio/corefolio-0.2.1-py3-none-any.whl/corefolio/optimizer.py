"""This module contains the Optimizer class, which is responsible for optimizing the portfolio."""

import cvxpy as cp

from corefolio.constraints import Constraints
from corefolio.universe import Universe


class Optimizer:
    def __init__(self, universe: Universe, constraints: Constraints, sense: str = "maximize"):
        self.universe = universe
        self.constraints = constraints
        self.sense = self._parse_sense(sense)

    def _parse_sense(self, sense: str):
        sense_map = {"maximize": 1, "minimize": -1}
        if sense not in sense_map:
            raise ValueError(
                "Invalid sense value. Choose 'maximize' or 'minimize'.")
        return sense_map[sense]

    def optimize(self):
        df = self.universe.get_data()
        ids = df[self.universe.id_column].tolist()
        values = df["value"].values

        # Define decision variables
        x = cp.Variable(len(ids), boolean=True)

        # Define objective
        objective = cp.Maximize(self.sense * values @ x)

        # Define constraints
        constraints = self.constraints.apply_constraints(x)

        # Solve problem
        problem = cp.Problem(objective, constraints)
        problem.solve()

        # Get results
        selected_ids = [ids[i]
                        for i in range(len(ids)) if x.value[i] > 0.5]

        return selected_ids
