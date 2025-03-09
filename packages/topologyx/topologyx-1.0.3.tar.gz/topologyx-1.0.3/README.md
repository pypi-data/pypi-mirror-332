<a href="https://merylldindin.com">
  <img src="https://cdn.merylldindin.com/github/topologyx.webp" alt="topologyx" width="100%">
</a>

<div align="center">
  <a href="https://github.com/merylldindin/topologyx/graphs/contributors" target="_blank">
    <img src="https://img.shields.io/github/contributors/merylldindin/topologyx.svg?style=for-the-badge" alt="contributors"/>
  </a>

  <a href="https://github.com/merylldindin/topologyx/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/merylldindin/topologyx.svg?style=for-the-badge" alt="stars"/>
  </a>

  <a href="https://github.com/merylldindin/topologyx/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/merylldindin/topologyx.svg?style=for-the-badge" alt="issues"/>
  </a>

  <a href="https://pypi.python.org/pypi/topologyx" target="_blank">
    <img src="https://img.shields.io/pypi/v/topologyx.svg?style=for-the-badge" alt="pypi version"/>
  </a>

  <a href="https://github.com/merylldindin/topologyx/blob/master/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/merylldindin/topologyx.svg?style=for-the-badge" alt="license"/>
  </a>
</div>

<div align="center">
  <p align="center">
    <h2> Topology Data Analysis Routines </h2>
    <a href="https://github.com/merylldindin/topologyx/issues">
        Report Bug
    </a>
  </p>
</div>

## <summary>Table of Contents</summary>

<ol>
    <li><a href="#about-topologyx">About TopologyX</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#get-started">Get Started</a></li>
</ol>

## About TopologyX

Topological Data Analysis, also abbreviated _TDA_, is a recent field that emerged from various works in applied topology and computational geometry. It aims at providing well-founded mathematical, statistical, and algorithmic methods to exploit the topological and underlying geometric structures in data. My aim is to develop some tools in this repository that may be applied to data science in general. Some of them have already proven useful for classification tasks.

Read more about applied TDA:

- [General introduction to TDA](https://hal.inria.fr/hal-02155849/file/1906.05795.pdf)
- [Medium article with general TDA overview](https://towardsdatascience.com/from-tda-to-dl-d06f234f51d)
- [Medium article about TDA for clustering](https://towardsdatascience.com/tda-to-rule-them-all-tomato-clustering-878e03394a1)
- [Paper on applied TDA for arrhythmia detection](https://arxiv.org/abs/1906.05795)

## Built With

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Gudhi](https://gudhi.inria.fr/)
- [Keras](https://keras.io/)

## Get Started

```bash
pip install topologyx
# or with poetry
poetry add topologyx
```

### How To Use

```python
from topologyx.filtrations import Filtration

filtration = Filtration(data, use_alpha=False)
filtration.build_persistence_diagram(filtration_type=FiltrationType.SIMPLE, dimension=0)
```

```python
from topologyx.clustering import TomatoClustering

tomato = TomatoClustering(data)
_ = tomato.estimate_clusters(visualize=True)
_ = tomato.fit_predict(n_clusters=3, visualize=True)
```

### Local Installation

```bash
git clone https://github.com/merylldindin/topologyx
# install dependencies
make install
```

### Using Notebooks

`ipykernel` comes out of the box with our dependencies, so you can directly use the notebooks provided in the `examples` folder. I use `VSCode` as engine for my jupyter notebooks.

**Tutorial: Filtration of a 3D shape:** This [notebook](https://github.com/merylldindin/topologyx/blob/master/examples/filtrations.ipynb) gives a simple example of how to handle three-dimensional shapes. The whole example is based on the height as filtration function, so not invariant in space. However, it gives a pretty good idea of what the output of a topological analysis may give.

**Tutorial: ToMaTo clustering:** This [notebook](https://github.com/merylldindin/topologyx/blob/master/examples/clustering.ipynb) rather focus on a specific strength of TDA: its robustness to detect centroids in dataset, along with its ability to record the relationships between each point, enabling us to retrace the whole structure of the centroids. Examples are provided in the notebook.
