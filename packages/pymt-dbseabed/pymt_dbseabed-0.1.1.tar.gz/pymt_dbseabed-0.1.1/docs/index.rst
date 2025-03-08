.. image:: _static/logo.png
    :align: center
    :scale: 28%
    :alt: pymt_dbseabed
    :target: https://pymt-dbseabed.readthedocs.io/en/latest/

`pymt_dbseabed <https://github.com/gantian127/pymt_dbseabed>`_ is a package that uses
the `bmi_dbseabed <https://github.com/gantian127/bmi_dbseabed>`_ pacakge to convert
`dbSEABED <https://instaar.colorado.edu/~jenkinsc/dbseabed/>`_ datasets into a reusable,
plug-and-play data component for `PyMT <https://pymt.readthedocs.io/en/latest/>`_ modeling framework developed by Community Surface
Dynamics Modeling System (`CSDMS <https://csdms.colorado.edu/wiki/Main_Page>`_).
This allows dbSEABED datasets to be easily coupled with other datasets or
models that expose a Basic Model Interface.

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

------------------------
Installing pymt_dbseabed
------------------------


To install `pymt_dbseabed`, use pip

.. code::

  pip install pymt_dbseabed

or conda

.. code::

  conda install -c conda-forge pymt_dbseabed


--------------
Coding Example
--------------
You can learn more details about the coding example from the
`tutorial notebook <https://github.com/gantian127/pymt_dbseabed/blob/master/notebooks/pymt_dbseabed.ipynb>`_.

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np

    from pymt.models import DbSeabedData

    # initiate a data component
    data_comp = DbSeabedData()
    data_comp.initialize('config_file.yaml')

    # get variable info
    var_name = data_comp.output_var_names[0]
    var_unit = data_comp.var_units(var_name)
    var_location = data_comp.var_location(var_name)
    var_type = data_comp.var_type(var_name)
    var_grid = data_comp.var_grid(var_name)
    var_itemsize = data_comp.var_itemsize(var_name)
    var_nbytes = data_comp.var_nbytes(var_name)

    print(f'{var_name=} \n{var_unit=} \n{var_location=} \n{var_type=} \n{var_grid=} \n{var_itemsize=} \n{var_nbytes=}')

    # get variable grid info
    grid_type = data_comp.grid_type(var_grid)
    grid_rank = data_comp.grid_ndim(var_grid)
    grid_shape = data_comp.grid_shape(var_grid)
    grid_spacing = data_comp.grid_spacing(var_grid)
    grid_origin = data_comp.grid_origin(var_grid)

    print(f'{grid_type=} \n{grid_rank=} \n{grid_shape=} \n{grid_spacing=} \n{grid_origin=}')

    # get variable data
    data = data_comp.get_value(var_name)
    data_2D = data.reshape(grid_shape)

    # get X, Y extent for plot
    min_y, min_x = grid_origin
    max_y = min_y + grid_spacing[0]*(grid_shape[0]-1)
    max_x = min_x + grid_spacing[1]*(grid_shape[1]-1)
    dy = grid_spacing[0]/2
    dx = grid_spacing[1]/2
    extent = [min_x - dx, max_x + dx, min_y - dy, max_y + dy]

    # plot data
    fig, ax = plt.subplots(1,1, figsize=(9,5))
    im = ax.imshow(data_2D, extent=extent)
    fig.colorbar(im)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("dbSEABED dataset (Carbonate in %)")

    # finalize the data component
    data_comp.finalize()

