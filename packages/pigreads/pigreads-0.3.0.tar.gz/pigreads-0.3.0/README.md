# Pigreads

[![Pipeline Status][pipeline-badge]][pipeline-link]
[![Coverage Report][coverage-badge]][coverage-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![Latest Release][release-badge]][release-link]
[![PyPI platforms][pypi-platforms]][pypi-link]
[![PyPI version][pypi-version]][pypi-link]

<!-- SPHINX-START -->

Pigreads stands for **Python-integrated GPU-enabled reaction diffusion solver**.

## Getting started

Install this Python package in the standard way using `pip`, for instance from
[PyPI][pypi-link] or from a local copy of this repository, see [the Python
documentation for details][py-install]. For the command line interface (CLI),
also install the optional dependency `cli`:

```
$ pip install pigreads[cli] # from PyPI
$ pip install .[cli] # from current directory
```

Simulations can be performed via calls to the Python module (API) or using the
CLI. See the API and CLI sections in the [documentation for annotated
examples][rtd-link], or the examples directory in the [Pigreads
repository][repo].

<!-- prettier-ignore-start -->
[repo]:           https://gitlab.com/pigreads/pigreads
[coverage-badge]: https://gitlab.com/pigreads/pigreads/badges/main/coverage.svg
[coverage-link]:  https://gitlab.com/pigreads/pigreads/-/commits/main
[pipeline-badge]: https://gitlab.com/pigreads/pigreads/badges/main/pipeline.svg
[pipeline-link]:  https://gitlab.com/pigreads/pigreads/-/pipelines
[pypi-link]:      https://pypi.org/project/pigreads/
[pypi-platforms]: https://img.shields.io/pypi/pyversions/pigreads
[pypi-version]:   https://img.shields.io/pypi/v/pigreads
[release-badge]:  https://gitlab.com/pigreads/pigreads/-/badges/release.svg
[release-link]:   https://gitlab.com/pigreads/pigreads/-/releases
[rtd-badge]:      https://readthedocs.org/projects/pigreads/badge/?version=latest
[rtd-link]:       https://pigreads.readthedocs.io/en/latest/?badge=latest
[py-install]:     https://packaging.python.org/en/latest/tutorials/installing-packages/
<!-- prettier-ignore-end -->
