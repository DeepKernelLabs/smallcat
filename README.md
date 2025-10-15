<p align="center">
  <img src="docs/assets/images/smallcat-logo.png" width="140" alt="smallcat logo">
</p>

<h1 align="center">smallcat</h1>
<p align="center"><em>A small, modular data catalog.</em></p>

<p align="center">
  <a href="https://pypi.org/project/smallcat/"><img src="https://img.shields.io/pypi/v/smallcat.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/smallcat/"><img src="https://img.shields.io/pypi/pyversions/smallcat.svg" alt="Python versions"></a>
  <a href="https://github.com/DeepKernelLabs/smallcat/actions"><img src="https://img.shields.io/github/actions/workflow/status/<USER>/<REPO>/ci.yml?label=CI" alt="CI"></a>
  <a href="https://codecov.io/gh/DeepKernelLabs/smallcat"><img src="https://img.shields.io/codecov/c/github/<USER>/<REPO>" alt="coverage"></a>
  <a href="https://github.com/DeepKernelLabs/smallcat/blob/main/LICENSE"><img src="https://img.shields.io/github/license/<USER>/<REPO>.svg" alt="license"></a>
  <a href="https://pepy.tech/project/smallcat"><img src="https://static.pepy.tech/badge/smallcat" alt="downloads"></a>
  <a href="https://DeepKernelLabs.github.io/smallcat/"><img src="https://img.shields.io/badge/docs-mkdocs%20material-blue" alt="docs"></a>
</p>

## Install
```bash
pip install smallcat
```

## Quickstart
```python
from smallcat import Catalog

cat = Catalog.from_path("catalog/")
print(cat.list())
```

## Docs
Read more at (pending).
