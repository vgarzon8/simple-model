.. Simple Model documentation master file, created by
   sphinx-quickstart on Fri May 21 11:26:33 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Project documentation
=====================

Simple classification model to demo GitHub workflows

* UCLA Graduate school data set
  * 400 samples, 3 features, 3 classes
* Data queried from a PostgreSQL database
* Random forest or gradient boosting classifier
* YAML configuration files for training and prediction
* Simple command-line interface
* Simple model serialization (Pickle files)
* Prediction using serialized model and data from configurable table

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

ghdemo data
-----------

.. automodule:: ghdemo.data
   :members:

ghdemo model
------------

.. automodule:: ghdemo.model
   :members:

ghdemo cli
----------

.. automodule:: ghdemo.cli
   :members:
