========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/marvelator/badge/?style=flat
    :target: https://readthedocs.org/projects/marvelator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/leonardok/marvelator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/leonardok/marvelator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/leonardok/marvelator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/leonardok/marvelator

.. |requires| image:: https://requires.io/github/leonardok/marvelator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/leonardok/marvelator/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/leonardok/marvelator/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/leonardok/marvelator

.. |codecov| image:: https://codecov.io/github/leonardok/marvelator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/leonardok/marvelator

.. |version| image:: https://img.shields.io/pypi/v/marvelator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/marvelator

.. |commits-since| image:: https://img.shields.io/github/commits-since/leonardok/marvelator/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/leonardok/marvelator/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/marvelator.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/marvelator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/marvelator.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/marvelator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/marvelator.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/marvelator


.. end-badges

Python abstraction for developer.marvel.com requests

* Free software: BSD license

Installation
============

::

    pip install marvelator

Documentation
=============

https://marvelator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox