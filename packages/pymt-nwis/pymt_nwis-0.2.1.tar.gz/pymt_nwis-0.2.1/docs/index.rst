.. image:: _static/logo.png
    :align: center
    :scale: 35%
    :alt: pymt_nwis
    :target: https://pymt-nwis.readthedocs.io/en/latest/


`pymt_nwis <https://github.com/gantian127/pymt_nwis>`_ converts `bmi_nwis <https://bmi-nwis.readthedocs.io/en/latest/?badge=latest>`_ into a reusable,
plug-and-play data component for `PyMT <https://pymt.readthedocs.io/en/latest/?badge=latest>`_ modeling framework.
pymt_nwis allows the National Water Information System data to be easily coupled with other data or models that expose
a `Basic Model Interface <https://bmi.readthedocs.io/en/latest/>`_.


Installation
------------

Install the pymt in a new environment:

.. code::

  $ conda config --add channels conda-forge
  $ conda create -n pymt -c conda-forge python=3 pymt
  $ conda activate pymt


Install the pymt_nwis using pip:

.. code::

  $ pip install pymt_nwis

or conda

.. code::

  $ conda install -c conda-forge pymt_nwis

Coding Example
--------------

You can learn more details about the coding example from the
`tutorial notebook <https://github.com/gantian127/pymt_nwis/blob/master/notebooks/pymt_nwis.ipynb>`_.

.. code-block:: python

    import numpy as np
    import cftime
    import pandas as pd

    from pymt.models import Nwis

    # initiate a data component
    data_comp = Nwis()
    data_comp.initialize('config_file.yaml')

    # get variable info
    for var_name in data_comp.output_var_names:
        var_unit = data_comp.var_units(var_name)
        var_location = data_comp.var_location(var_name)
        var_type = data_comp.var_type(var_name)
        var_grid = data_comp.var_grid(var_name)
        var_itemsize = data_comp.var_itemsize(var_name)
        var_nbytes = data_comp.var_nbytes(var_name)

        print('variable_name: {} \nvar_unit: {} \nvar_location: {} \nvar_type: {} \nvar_grid: {} \nvar_itemsize: {}'
            '\nvar_nbytes: {} \n'. format(var_name, var_unit, var_location, var_type, var_grid, var_itemsize, var_nbytes))

    # get time info
    start_time = data_comp.start_time
    end_time = data_comp.end_time
    time_step = data_comp.time_step
    time_units = data_comp.time_units
    time_steps = int((end_time - start_time)/time_step) + 1

    print('start_time: {} \nend_time: {} \ntime_step: {} \ntime_units: {} \ntime_steps: {} \n'.format(
        start_time, end_time, time_step, time_units, time_steps))

    # get variable grid info
    grid_type = data_comp.grid_type(var_grid)
    grid_rank = data_comp.grid_ndim(var_grid)
    grid_node_count = data_comp.grid_node_count(var_grid)
    site_lon = data_comp.grid_x(var_grid)[0]
    site_lat = data_comp.grid_y(var_grid)[0]

    print('grid_type: {} \ngrid_rank: {} \ngrid_node_count: {} \nsite_lon: {} \nsite_lat: {}'.format(
        grid_type, grid_rank, grid_node_count, site_lon, site_lat))

    # initiate dataframe to store data
    dataset = pd.DataFrame(columns = ['00060','00065','time'])

    for i in range(0, time_steps):
        # get values
        stream_flow = data_comp.get_value('Stream flow')
        gage_height = data_comp.get_value('Height')
        time = cftime.num2pydate(data_comp.time, time_units)

        # add new row to dataframe
        dataset.loc[len(dataset)]=[stream_flow[0], gage_height[0], time]

        # update to next time step
        data_comp.update()

    # convert time to local time
    dataset = dataset.set_index('time').tz_localize(tz='UTC').tz_convert(tz='US/Central')

    # plot data
    ax = dataset.plot(y=['00060','00065'], subplots=True, figsize=(8,8),
                      xlabel='Time', title = 'Time Series Data at USGS Gage 03339000')
    ax[0].set_ylabel('Stream flow (ft3/s)')
    ax[1].set_ylabel('Gage height (ft)')

    # finalize the data component
    data_comp.finalize()


|ts_plot|

.. links:

.. |binder| image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/gantian127/pymt_nwis/master?filepath=notebooks%2Fpymt_nwis.ipynb

.. |ts_plot| image:: _static/plot.png