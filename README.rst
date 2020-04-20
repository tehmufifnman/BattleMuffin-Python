BattleMuffin
************
|Build Status| |Coverage Status| |Code Style|

Python Implementation of Blizzard's Web API

Requires Python >= 3.4

Quick Setup
===========
Some easy examples to get you started!

.. code-block:: python

   from clients.warcraft_client import WarcraftClient


   client = new WarcraftClient("CLIENT_ID", "CLIENT_SECRET")
   response = client.get_achievement_categories_index()

It is possible to specify a region, using its default locale

.. code-block:: python

   from clients.warcraft_client import WarcraftClient
   from config.region_config import Region


   client = new WarcraftClient("CLIENT_ID", "CLIENT_SECRET", Region.eu)
   response = client.get_achievement_categories_index()

It is also possible to specify both the region and locale

.. code-block:: python

   from clients.warcraft_client import WarcraftClient
   from config.region_config import Region, Locale


   client = WarcraftClient(client_id, client_secret, Region.eu, Locale.es_ES)
   response = client.get_achievement_categories_index()

Installation
============

To install the latest stable release, you can use ``pip`` (or ``pipenv``):

::

    $ pip install -U battle-muffin

.. |Build Status| image:: https://github.com/tehmufifnman/BattleMuffin-Python/workflows/BattleMuffin-Python/badge.svg
   :target: https://github.com/tehmufifnman/BattleMuffin-Python/actions
.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black
.. |Coverage Status| image:: https://codecov.io/gh/tehmufifnman/BattleMuffin-Python/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/tehmufifnman/BattleMuffin-Python
