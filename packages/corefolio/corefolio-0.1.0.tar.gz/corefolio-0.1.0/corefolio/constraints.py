"""This module contains the Constraints class, which is used to apply constraints to the optimization problem."""

import cvxpy as cp


class Constraints:
    @staticmethod
    def apply_constraints(variables: list[int], max_assets: int = 5):
        constraints = []
        constraints.append(cp.sum(variables) <= max_assets)
        return constraints
