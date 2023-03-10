*******************************************************************************
Installation
*******************************************************************************

|this| can be installed in multiple ways: choose the one that better suits your needs!


=========
From PyPI
=========

|this| is distributed through the `Python Package Index <https://pypi.org/>`_, so you can install it with your favourite dependency manager!

This is the recommended way to install the package, as it's the simplest to manage and will work properly for most use cases.


---------
Using pip
---------

.. warning::

    Never install packages outside a :mod:`venv`, unless you know very well what you're doing!

    You can create a *venv* (short for *virtual environment*) by entering:

    .. code-block:: console

        $ python -m venv .venv

    Then, you can activate that venv by entering:

    .. code-block:: console

        $ # On Bash
        $ source .venv/bin/activate
    
    .. code-block:: console

        $ # On Fish
        $ source .venv/bin/activate.fish

    .. code-block:: doscon

        > ; On Windows
        > .venv/Scripts/activate.ps1

    Once activated, all :mod:`pip` commands you enter will affect only the virtual environment, and won't prevent the correct functioning of your operating system!


To install |this| using :mod:`pip`:

#. Add |this| to your ``requirements.txt`` file:

    .. code-block:: text
        
        emblematic

#. Update your dependencies:

    .. code-block:: console
        
        $ pip install --upgrade --requirement requirements.txt


----------
Using pipx
----------

To install |this| using :mod:`pipx`:

#. Run the following command:

    .. code-block:: console
        
        $ pipx install emblematic


===========
From source
===========

You can install |this| by manually retrieving its source and installing it in your environment!

This may be useful if you want to tweak its behaviour without making a full fork.


------------
Using PEP518
------------

.. warning::

    Never install packages outside a :mod:`venv`, unless you know very well what you're doing!

    See `Using pip` for more details on how to use *venvs*.

You can use the :mod:`pip` features introduced with :pep:`518` to automatically install |this| in your environment:

#. Access the source code directory:

    .. code-block:: console

        $ cd emblematic

#. Install |this| in editable mode using :mod:`pip`:

    .. code-block:: console

        $ pip install --editable .

.. note::

    Any edit applied to the source code will be automatically reflected to the 


===============
For development
===============

To contribute to |this|, you need to setup the project's environment using :mod:`poetry`:

#. Access the source code directory:

    .. code-block:: console

        $ cd emblematic

#. Install the project's dependencies with :mod:`poetry`:

    .. code-block:: console

        $ poetry install
    
    .. hint::

        It is recommended to set ``virtualenvs.in-project`` to :data:`True`!

        .. code-block:: console

            $ poetry config virtualenvs.in-project true
