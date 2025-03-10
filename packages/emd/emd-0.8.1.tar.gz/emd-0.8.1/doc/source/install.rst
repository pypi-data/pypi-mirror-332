Installing EMD
=================================

There are several ways to install the EMD toolbox. The best one to use depends
on how you want to use the code.

The latest release of EMD is tested against the following python versions:

.. container:: body

    .. raw:: html

        <a href='https://pypi.org/project/emd/'>
            <img src="https://img.shields.io/pypi/pyversions/emd">
        </a>

Quick Start
***********

A lot of the time you'll be able to get started using

.. code-block::

    pip install emd

More detailed instructions for other cases are included below.


Stable version (PyPI)
*********************

The `stable version of the code <https://pypi.org/project/emd/>`_ is hosted on `PyPI <https://pypi.org>`_ and will be updated relatively slowly. Any updates to PyPI will (hopefully) only contain working changes that have been running without problems on the development versions of the code for a while.


.. dropdown:: Install with pip

    EMD can be installed from `PyPI <https://pypi.org/project/emd/>`_ using pip:

    .. code-block::

        pip install emd

    pip will install the latest version of EMD from PyPI alongside any missing dependencies into the current python environment. You can install a specific version by specifying the version number:

    .. code-block::

        pip install emd==0.8.1




.. dropdown:: Install from conda-forge

    EMD can be installed from the `conda-forge <https://anaconda.org/conda-forge/emd>`_ channel:

    .. code-block::

        conda install -c conda-forge emd


.. dropdown:: Install in conda environment

    If you want to create a conda environment containing EMD, you can use the following yaml config:

    .. code-block::

        name: emd-env
        channels:
          - defaults
          - conda-forge
        dependencies:
          - emd

    This can be adapted to specify a particular release of EMD by adding the version number to the emd line:

    .. code-block::

        name: emd-env
        channels:
          - defaults
          - conda-forge
        dependencies:
          - emd==0.8.1

    This environment can be customised to include any other packages that you might be working with. The last two lines can also be added to an existing conda environment configuration file to include emd in that env.

    This env can be downloaded `HERE (emd_conda_env.yml) <https://gitlab.com/emd-dev/emd/-/blob/master/envs/emd_conda_env.yml>`_. You can download the config and install the enviromnent by changing directory to the install location and calling these commands:

    .. code-block::

        curl https://gitlab.com/emd-dev/emd/-/raw/master/envs/emd_conda_env.yml > emd_conda_env.yml
        conda env create -f emd_conda_env.yml

    this will automatically install the required dependancies alongside EMD. The environment can then be activated by calling:

    .. code-block::

        source activate emd



Development version (GitLab)
****************************

You can also install the `latest development version of EMD
<https://gitlab.com/emd-dev/emd>`_ from gitlab.com using a conda environment. An iconicon :fas:`fa-solid fa-code`, some more text, some more text.
This version is less stable and likely to change quickly during active
development - however you will get access to new bug-fixes, features and bugs
more quickly.

.. dropdown:: Install in conda environment

    A conda environment config file can be specified pointing at the development version of EMD on gitlab:

    .. code-block::

        name: emd
        channels:
        dependencies:
           - pip
           - pip:
             - git+https://gitlab.com/emd-dev/emd.git

    The env can be downloaded `HERE (emd-dev_conda_env.yml) <https://gitlab.com/emd-dev/emd/-/blob/master/envs/emd-dev_conda_env.yml>`_. You can download the config and install the enviromnent by changing directory to the install location and calling these commands:

    .. code-block::

        curl https://gitlab.com/emd-dev/emd/-/raw/master/envs/emd-dev_conda_env.yml > emd-dev_conda_env.yml
        conda env create -f emd-dev_conda_env.yml

    this will automatically install the required dependancies alongside EMD. The environment can then be activated by calling:

    .. code-block::

        source activate emd-dev


.. dropdown:: Install from source

    If you plan to actively contribute to EMD, you will need to install EMD directly from source using git. From the terminal, change into the directory you want to install emd into and run the following command:

    .. code-block::

        cd /home/andrew/src
        git clone https://gitlab.com/emd-dev/emd.git
        cd emd
        python setup.py install

    This will install EMD into the current python environment. You will then be able to use git as normal to switch between development branches of EMD and contribute your own.

    You may want to install EMD into a virtual environment or similar for better control over versions and dependencies.

    .. code-block::

        cd /home/andrew/src
        git clone https://gitlab.com/emd-dev/emd.git
        cd emd
        python -m venv ./.venv
        source ./.venv/bin/activate
        python setup.py install

