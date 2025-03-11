# Bayes by Backprop

A Bayesian Neural Network framework for regression tasks implemented in PyTorch. This framework provides tools for uncertainty estimation in neural networks through variational inference.

## Installation

```bash
pip install bayes-by-backprop
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/zchccsx/Bayes-by-Backprop.git
```

## Usage

```python
import Bayes
from Bayes import BayesianLinear, BayesianRegressor

# Create a Bayesian neural network
model = BayesianRegressor(input_dim=10, hidden_dims=[32, 16], output_dim=1)

# Use it for regression with uncertainty estimation
...
```

## License

MIT
