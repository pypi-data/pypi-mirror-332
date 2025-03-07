# Bamboo: A Domain-Specific Language for PDE Solvers on Structured Grids

<p>
  Copyright@Tsinghua High-Performance Computing Applications Group (TH-HPCA) 
  <img src="docs/th-hpca.png" style="height: 3em; vertical-align: middle;">
</p>

## Introduction

```python
from bamboo import Grid, Stencil

grid = Grid(shape=(100, 100))
@Stencil
def laplace(u):
    return 0.25 * (u[1, 0] + u[-1, 0] + u[0, 1] + u[0, -1])
```

Bamboo is a high-level domain-specific language (DSL) designed to simplify PDE solver development on structured grids. It abstracts away parallelization and optimization, allowing domain scientists to focus on physical algorithms rather than low-level performance tuning.

Embedded in Python, Bamboo provides an intuitive syntax for defining computations in terms of grids, discretization, and time integration. The back-end generates optimized code for CPUs (including Huawei Kunpeng), GPUs/DCUs, and next-generation Sunway architectures, ensuring performance portability across platforms.

## Installation

[Online] Install Bamboo via pip:

```sh
pip install bamboolang
```

[Local] Install Bamboo  locally via poetry at the root directory of bamboo:

```sh
poetry install
```

### Prerequisites

- Python 3.7.10
- Visual Studio Code (for developers)
- sphinx with sphinx_rtd_theme (for documentation)

## Getting Started

Refer to the [official documentation](docs/build/html/index.html) for detailed usage and examples.

[Build] Build html documentation using sphinx:

```sh
make docs -C docs
```

## Code Style

- Formatted using **Black**.
- Naming follows **PEP 8** guidelines.

## License

Bamboo is licensed under the [GNU General Public License v3](LICENSE). See the license file for details.
