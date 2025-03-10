"""Tests for the Optimizer class."""

import pandas as pd

from corefolio.constraints import Constraints
from corefolio.universe import Universe
from corefolio.optimizer import Optimizer


def test_optimizer():
    df = pd.DataFrame({"ID": [1, 2, 3, 4], "value": [10, 20, 30, 40]})
    universe = Universe(df)
    constraints = Constraints()
    optimizer = Optimizer(universe, constraints,
                          sense="maximize", max_assets=2)
    selected_ids = optimizer.optimize()
    assert len(selected_ids) <= 2
    assert all(id in df["ID"].values for id in selected_ids)
