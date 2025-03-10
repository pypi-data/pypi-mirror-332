"""Tests for the Universe class."""

import pytest
import pandas as pd

from corefolio.universe import Universe


def test_universe_initialization():
    data = pd.DataFrame({"ID": [1, 2, 3], "value": [10, 20, 30]})
    universe = Universe(data)
    assert universe.number_of_assets == 3


def test_universe_nan_values():
    data = pd.DataFrame({"ID": [1, 2, None], "value": [10, 20, 30]})
    with pytest.raises(Exception, match="DataFrame contains NaN values."):
        Universe(data)


def test_universe_duplicate_ids():
    data = pd.DataFrame({"ID": [1, 2, 2], "value": [10, 20, 30]})
    with pytest.raises(Exception, match="DataFrame contains duplicate IDs."):
        Universe(data)


def test_universe_from_dataframe():
    data = pd.DataFrame({"ID": [1, 2, 3], "value": [10, 20, 30]})
    universe = Universe.from_dataframe(data)
    assert universe.to_dataframe().equals(data)


def test_universe_custom_id_column():
    data = pd.DataFrame({"Asset_ID": [1, 2, 3], "value": [10, 20, 30]})
    universe = Universe.from_dataframe(data, id_column="Asset_ID")
    assert universe.number_of_assets == 3
