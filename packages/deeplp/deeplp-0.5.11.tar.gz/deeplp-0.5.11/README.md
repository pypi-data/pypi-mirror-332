# deeplp

**deeplp** is a Python package designed for solving linear programming problems using deep learning techniques. It leverages PyTorch for its backend computations and provides a simple API for defining problems and training models.

## Features

- Define linear programming problems with custom objective functions and constraints.
- Use deep learning methods to solve LPs.
- Built-in functions to generate problem data and train models.
- Command-line interface (CLI) available for ease-of-use.

## Requirements

**deeplp** requires Python 3.8+ and PyTorch. You can install PyTorch by following the instructions on the official [PyTorch website](https://pytorch.org/get-started/locally/).

### Installing PyTorch

For example, to install PyTorch with CUDA support (e.g. for CUDA 11.3) on Windows, run:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

For CPU-only support, simply run:

```bash
pip install torch torchvision torchaudio
```

## Installation

### Using GitHub with Poetry

If your package is hosted on GitHub, you can install it directly via pip:

```bash
pip install git+https://github.com/yourusername/deeplp.git
```

Or, if you prefer to clone the repository and install it in editable mode for development:

```bash
git clone https://github.com/yourusername/deeplp.git
cd deeplp
poetry install
```

## Basic Usage

### Defining a Problem

To define a problem, use the `createProblem` function. For example:

```python
from deeplp import createProblem

# Define your problem data:
c = [1.0, 2.0]  # Example objective coefficients
A = [
    [3, -5],
    [3, -1],
    [3,  1],
    [3,  4],
    [1,  3]
]  # Constraint matrix
b = [15, 21, 27, 45, 30]  # Right-hand side values
tspan = (0.0, 10.0)  # Time span

# Create a problem; if name is not provided, cutename() will be used.
problem = createProblem(c, A, b, tspan, name=None, test_points=None)
```

This function uses default behavior to generate a problem name (via `cutename()`) if none is provided and returns a named tuple with the fields required by **deeplp**.

### Training a Model

After defining your problem(s), you can train a model using the `train` function. For example:

```python
from deeplp import train
import argparse

# Suppose you collect command-line arguments via argparse
parser = argparse.ArgumentParser()
parser.add_argument("--batches", type=int, default=1)
parser.add_argument("--batch_size", type=int, default=128)
parser.add_argument("--iterations", type=int, default=1000)
parser.add_argument("--case", type=int, default=1)
parser.add_argument("--example", type=int, default=1)
parser.add_argument("--do_plot", action="store_true")
parser.add_argument("--folder", type=str, default="saved_models")
args = parser.parse_args()

# Train the model using the provided arguments:
train(
    batches=args.batches,
    batch_size=args.batch_size,
    epochs=args.iterations,
    cases=args.case,
    problems_ids=args.example,
    do_plot=args.do_plot,
    saving_dir=args.folder,
)
```

This command uses the parameters to run the training process and, if enabled, will plot results and save the model in the specified folder.

## Command-Line Interface

**deeplp** includes a CLI that lets you run training or evaluation directly from the command line. For example, after installation you might run:

```bash
deeplp --batches 1 --batch_size 128 --iterations 1000 --case 1 --example 1 --do_plot --folder saved_models
```

(Adjust the arguments as needed for your use case.)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, development process, and how to submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the PyTorch community for their excellent deep learning framework.
- Special thanks to the developers of deepXDE for inspiring parts of this project.
```

---

### Explanation

- **Title & Overview:**  
  The README starts with the package name, a brief description of what the package does, and its key features.

- **Requirements:**  
  It lists the Python version and dependency on PyTorch and provides installation instructions for PyTorch (both GPU and CPU options).

- **Installation:**  
  Instructions are provided for installing the package directly from GitHub using pip or via Poetry.

- **Basic Usage:**  
  The usage section explains how to define a problem using `createProblem` and how to train a model using the `train` function, along with example code.

- **CLI:**  
  A short section explains that the package includes a command-line interface, with an example command.

- **Contributing & License:**  
  Instructions for contributing and licensing information are included.

This README template should provide a solid starting point for your package documentation on GitHub. Adjust the text and examples as needed for your specific package details.