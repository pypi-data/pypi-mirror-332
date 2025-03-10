# CoreFolio

`corefolio` is a Python package for optimizing asset selection using CVXPY. It allows users to define a universe of assets, apply constraints, and optimize the portfolio based on specified criteria.

## Installation

To install the package, use the following command:

```sh
pip install corefolio
```

## Requirements
- Python >= 3.10
- pandas
- cvxpy >= 1.6.2
- pytest

## Usage

```python
from corefolio.optimizer import Optimizer
from corefolio.universe import Universe
from corefolio.constraints import Constraints

# Define your universe and constraints
universe = Universe(data)
constraints = Constraints()

# Create an optimizer instance
optimizer = Optimizer(universe, constraints, sense="maximize", max_assets=5)

# Optimize the portfolio
selected_assets = optimizer.optimize()

print("Selected assets:", selected_assets)
```

## License
This project is licensed under the MIT License.
