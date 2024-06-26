*******************************************************************************
Usage
*******************************************************************************

:mod:`emblematic` currently supports only a single mode of operation.


=======================
Generate a basic emblem
=======================

A *basic emblem* can be generated by running:

.. code-block:: console

    $ emblematic basic --background="./bg.svg" --icon="./icon.svg" --fill="#feedb4" --output-dir="./output/"

It is composed by:

1. taking the SVG background image contained in the file given as the ``--background`` option, such as the following:

    .. figure:: ryg6-bg.png
        :width: 150
        :height: 150

2. overlaying a rescaled version of the SVG foreground icon contained in the file given as the ``--icon`` option, filled with the color given in the ``--fill`` option, such as the following:

    .. figure:: fontawesome-ice-cream.png
        :width: 150
        :height: 150

3. converting the resulting document to a 2000x2000 PNG file for better compatibility with applications (very few support correctly the ``preserveAspectRatio`` property):

    .. figure:: ryg6-ice-cream.png
        :width: 150
        :height: 150


.. note::
    
    The previous images are SVG files converted to PNG, as ReadTheDocs doesn't seem to work correctly with SVG files.

    You can find the original SVG files in the code repository!


---------------------------------
Multiple emblems with one command
---------------------------------

Multiple emblem files can be generated at once.

* Pass the ``--icon`` parameter multiple times to generate emblems with the same settings but different icons:

    .. code-block:: console

        $ emblematic basic --background="./bg.svg" --icon="./icon1.svg" --icon="./icon2.svg" --icon="./icon3.svg" --fill="#feedb4" --output-dir="./output/"

* Pass a directory as the ``--icon`` parameter to render all contained files matched by the ``**/*.svg`` glob:

    .. code-block:: console

        $ emblematic basic --background="./bg.svg" --icon="./fontawesome/" --fill="#feedb4" --output-dir="./output/"


-----------
Drop shadow
-----------

A drop shadow can be added to icons by passing the ``--icon-shadow-fill``, ``--icon-shadow-x``, ``--icon-shadow-y`` and ``--icon-shadow-blur`` parameters.

.. code-block:: console

    $ emblematic basic --background="./bg.svg" --icon="./icon.svg" --fill="#feedb4" --output-dir="./output/" --icon-shadow-fill="#000000" --icon-shadow-x="8" --icon-shadow-y="-4" --icon-shadow-blur="16"
