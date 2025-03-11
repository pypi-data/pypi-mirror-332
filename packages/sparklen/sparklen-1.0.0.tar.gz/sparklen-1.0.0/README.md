
<a href="https://github.com/romain-e-lacoste/sparklen">
    <img src="doc/logos/sparklen-logo-black.svg" alt="Sparklen black logo" width=250/>
</a>


# Toolkit for Hawkes Processes in Python


## Goal

The purpose of `Sparklen` package is to provide the `Python` community with 
a complete suite of cutting-edge tools specifically tailored for 
the study of exponential Hawkes processes, with a particular focus 
on high-dimensional framework. It notably features:

  * A efficient cluster-based simulation method for generating events.

  * A highly versatile and flexible framework for performing inference of 
    multivariate Hawkes process.

  * Novel approaches to address the challenge of multiclass 
    classification within the supervised learning framework.


## Installation

This section describes how to install the necessary dependencies to 
set up the package.

### 1. Install SWIG

`Sparklen` uses a `C++` core code for computationally intensive 
components, ensuring both efficiency and performance. The binding between `C++` 
and `Python` is handled through `SWIG` wrapper code.

So first, you need to install `SWIG`. Below are the instructions for various platforms.

#### **Anaconda/Miniconda**

If you're using Anaconda or Miniconda, install `SWIG` from the `conda-forge` channel:

```bash
conda install -c conda-forge swig
```

#### **Linux (Ubuntu/Debian)**

On Ubuntu or Debian-based systems, you can install `SWIG` using `apt`:

```bash
sudo apt update
sudo apt install swig
```

#### **macOS (Homebrew)**

On macOS, you can install `SWIG` using `Homebrew`:

```bash
brew install swig
```

#### Windows 

For Windows, follow these steps:

1. Download the latest `SWIG` release from the [SWIG website](http://www.swig.org/download.html)
2. Add the `SWIG` folder to your system's PATH environment variable

If you are using Chocolatey you can also install `SWIG` by running:

```bash
choco install swig
```

### 2. Get the Source Code

Clone the repository to get the latest version of the source code:

```bash
git clone https://github.com/romain-e-lacoste/sparklen.git
cd sparklen
```

### 3. Install the Package

It's recommended to set up a dedicated Python environment (e.g., using `venv` or `conda`). 
Once your environment is ready, install the package by running:

```bash
pip install .
```

## Citing this work

If you found this package useful, please consider citing it in your work:

```bibtex
@article{lacoste2025sparkle,
      title={Sparkle: A Statistical Learning Toolkit for High-Dimensional Hawkes Processes in Python}, 
      author={Lacoste, Romain E.},
      year={2025},
      eprint={2502.18979},
      archivePrefix={arXiv},
      primaryClass={stat.ME},
      url={https://arxiv.org/abs/2502.18979}, 
}
```

## Acknowledgement

This work has been supported by the Chaire “Modélisation Mathématique et Biodiversité”
of Veolia-École polytechnique-Museum national d’Histoire naturelle-Fondation X