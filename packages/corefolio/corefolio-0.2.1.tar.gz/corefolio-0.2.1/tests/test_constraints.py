"""Tests for the constraints module."""

import cvxpy as cp

from corefolio.constraints import Constraints


def test_apply_constraints():
    x = cp.Variable(3, boolean=True)
    constraints = Constraints(max_assets=2)
    applied_constraints = constraints.apply_constraints(x)
    assert len(applied_constraints) == 1
    assert applied_constraints[0].args[1].value == 2
