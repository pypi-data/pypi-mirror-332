"""This module contains the Constraints class, which is used to apply constraints to the optimization problem."""

import cvxpy as cp


class Constraints:
    def __init__(self, max_assets: int = 5):
        self.max_assets = max_assets

    def apply_constraints(self, variables: list[int]):
        constraints = []
        constraints.append(cp.sum(variables) <= self.max_assets)
        return constraints
