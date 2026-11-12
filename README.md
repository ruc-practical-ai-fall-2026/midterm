# Practical AI Midterm Exam

This midterm follows the same format as prior assignments and quizzes from the semester. Read and follow the directions in the exam folder to complete the assignment. Follow the instructions from the [assignments tutorial](https://github.com/ruc-practical-ai-fall-2026/tutorials/blob/main/05-assignments.md) to submit the assignment.

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if it is not already available, then run `uv sync` from the repository root.

```sh
uv sync
```

This creates the in-project `.venv` environment and installs the exam dependencies. In VS Code, open a notebook, choose **Select Kernel**, and select the Python environment at `.venv`.

The dependencies include Captum for Problem 19's integrated gradients and
`onnx` and `onnxscript` for PyTorch's ONNX export. Run `uv sync` after pulling
exam updates, and restart an already running notebook kernel.

The repository is installed into `.venv` in editable mode, so modules in `exam/` can be imported from notebooks no matter which folder Jupyter uses as its working directory. For example, add `exam/math.py` and import it via

```python
from exam import math
```

or

```python
from exam.math import some_function
```

Run a Python file with the same environment using `uv run python exam/example.py`.

To add a dependency, for example `pandas`, run `uv add pandas`. This updates `pyproject.toml` and `uv.lock`. Run `uv sync` after pulling changes to install the locked dependencies.

## Ruff and MyPy

`uv sync` also installs the development tools: Ruff, mypy, and
[nbQA](https://nbqa.readthedocs.io/en/latest/readme.html), which runs mypy on
notebook code cells. Run these checks from the repository root:

```sh
uv run ruff check exam/problems_11-17.ipynb
uv run ruff format --check exam/problems_11-17.ipynb
uv run nbqa mypy exam/problems_11-17.ipynb
```

The notebook keeps its answer choices commented out. Narrow inline exceptions
cover imports used only in those choices and names students define by selecting
an answer. Ruff and MyPy are not part of grading.

## License

This repository is provided with an MIT license. See the `LICENSE` file.

## Contributing

Please email Mauro Sanchirico at ms3978@camden.rutgers.edu (academic) or sanchirico.mauro@gmail.com (personal) with questions, comments, bug reports, or suggestions for improvement.

