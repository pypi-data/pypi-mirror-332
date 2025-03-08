==============
pymt_nwis
==============

.. image:: https://zenodo.org/badge/353523375.svg
  :target: https://zenodo.org/doi/10.5281/zenodo.10368875

.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. .. image:: https://img.shields.io/badge/recipe-pymt_nwis-green.svg
        :target: https://anaconda.org/conda-forge/pymt_nwis

.. image:: https://readthedocs.org/projects/pymt-nwis/badge/?version=latest
        :target: https://pymt-nwis.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
        :target: hhttps://github.com/gantian127/pymt_nwis/blob/master/LICENSE


pymt_nwis is a package that converts `bmi_nwis package <https://github.com/gantian127/bmi_nwis>`_ into a reusable,
plug-and-play data component for `PyMT <https://pymt.readthedocs.io/en/latest/?badge=latest>`_ modeling framework.
This allows the National Water Information System (`NWIS <https://waterdata.usgs.gov/nwis>`_) data to be easily coupled with other data or models that expose
a `Basic Model Interface <https://bmi.readthedocs.io/en/latest/>`_.

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

--------------------
Installing pymt_nwis
--------------------



To install `pymt_nwis`, use pip

.. code::

  pip install pymt_nwis
  
  
or conda

.. code::

  conda install -c conda-forge pymt_nwis

--------------------
Coding Example
--------------------

You can learn more details about the coding example from the
`tutorial notebook <https://github.com/gantian127/pymt_nwis/blob/master/notebooks/pymt_nwis.ipynb>`_.
