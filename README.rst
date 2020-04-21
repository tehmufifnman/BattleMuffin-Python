BattleMuffin
************
|Build Status| |Coverage Status| |Code Style|

Python Implementation of Blizzard's Web API

BattleMuffin officially supports Python 3.6-3.8.

Requirements
============

This package requires client credentials from Blizzard.

You can find out more about how to generate these credentials for your project at the `Blizzard Developer Portal`_.

.. _`Blizzard Developer Portal`: https://develop.battle.net/

Quick Setup
===========
Some easy examples to get you started!

.. code-block:: python

   from battlemuffin.clients.warcraft_client import WarcraftClient


   client = new WarcraftClient("CLIENT_ID", "CLIENT_SECRET")
   response = client.get_achievement_categories_index()

It is possible to specify a region, using its default locale

.. code-block:: python

   from battlemuffin.clients.warcraft_client import WarcraftClient
   from battlemuffin.config.region_config import Region


   client = new WarcraftClient("CLIENT_ID", "CLIENT_SECRET", Region.eu)
   response = client.get_achievement_categories_index()

It is also possible to specify both the region and locale

.. code-block:: python

   from battlemuffin.clients.warcraft_client import WarcraftClient
   from battlemuffin.config.region_config import Region, Locale


   client = WarcraftClient(client_id, client_secret, Region.eu, Locale.es_ES)
   response = client.get_achievement_categories_index()

Installation
============

To install the latest stable release, you can use ``pip`` (or ``pipenv``):

::

    $ pip install -U battlemuffin

Implemented Endpoints
=====================

World of Warcraft (Retail):

Game Data:

+------------------------------------+
| Name                               |
+====================================+
| Achievement Categories Index       |
+------------------------------------+
| Achievement Category               |
+------------------------------------+
| Achievements Index                 |
+------------------------------------+
| Achievement                        |
+------------------------------------+
| Achievement Media                  |
+------------------------------------+
| Auctions                           |
+------------------------------------+
| Azerite Essences Index             |
+------------------------------------+
| Azerite Essence                    |
+------------------------------------+
| Azerite Essence Media              |
+------------------------------------+
| Connected Realms Index             |
+------------------------------------+
| Connected Realm                    |
+------------------------------------+
| Creature Families Index            |
+------------------------------------+
| Creature Family                    |
+------------------------------------+
| Creature Types Index               |
+------------------------------------+
| Creature Type                      |
+------------------------------------+
| Creature                           |
+------------------------------------+
| Creature Display Media             |
+------------------------------------+
| Creature Family Media              |
+------------------------------------+
| Guild Crest Components Index       |
+------------------------------------+
| Guild Crest Border Media           |
+------------------------------------+
| Guild Crest Emblem Media           |
+------------------------------------+
| Item Classes Index                 |
+------------------------------------+
| Item Class                         |
+------------------------------------+
| Item Sets Index                    |
+------------------------------------+
| Item Set                           |
+------------------------------------+
| Item Subclass                      |
+------------------------------------+
| Item                               |
+------------------------------------+
| Item Media                         |
+------------------------------------+
| Journal Expansions Index           |
+------------------------------------+
| Journal Expansion                  |
+------------------------------------+
| Journal Encounters Index           |
+------------------------------------+
| Journal Encounter                  |
+------------------------------------+
| Journal Instances Index            |
+------------------------------------+
| Journal Instance                   |
+------------------------------------+
| Journal Instance Media             |
+------------------------------------+
| Mounts Index                       |
+------------------------------------+
| Mount                              |
+------------------------------------+
| Mythic Keystone Affixes Index      |
+------------------------------------+
| Mythic Keystone Affix              |
+------------------------------------+
| Mythic Keystone Affixe Media       |
+------------------------------------+
| Mythic Keystone Dungeons Index     |
+------------------------------------+
| Mythic Keystone Dungeon            |
+------------------------------------+
| Mythic Keystone Index              |
+------------------------------------+
| Mythic Keystone Periods Index      |
+------------------------------------+
| Mythic Keystone Period             |
+------------------------------------+
| Mythic Keystone Seasons Index      |
+------------------------------------+
| Mythic Keystone Season             |
+------------------------------------+
| Mythic Keystone Leaderboards Index |
+------------------------------------+
| Mythic Keystone Leaderboard        |
+------------------------------------+
| Mythic Raid Leaderboard            |
+------------------------------------+
| Pets Index                         |
+------------------------------------+
| Pet                                |
+------------------------------------+
| Playable Classes Index             |
+------------------------------------+
| Playable Class                     |
+------------------------------------+
| Playable Class Media               |
+------------------------------------+
| PvP Talent Slots                   |
+------------------------------------+
| Playable Races Index               |
+------------------------------------+
| Playable Race                      |
+------------------------------------+
| Playable Specializations Index     |
+------------------------------------+
| Playable Specialization            |
+------------------------------------+
| Playable Specialization Media      |
+------------------------------------+
| Power Types Index                  |
+------------------------------------+
| Power Type                         |
+------------------------------------+
| Professions Index                  |
+------------------------------------+
| Profession                         |
+------------------------------------+
| Profession Media                   |
+------------------------------------+
| Profession Skill Tier              |
+------------------------------------+
| Recipe                             |
+------------------------------------+
| Recipe Media                       |
+------------------------------------+
| PvP Seasons Index                  |
+------------------------------------+
| PvP Season                         |
+------------------------------------+
| PvP Leaderboards Index             |
+------------------------------------+
| PvP Leaderboard                    |
+------------------------------------+
| PvP Rewards Index                  |
+------------------------------------+
| PvP Tiers Index                    |
+------------------------------------+
| PvP Tier                           |
+------------------------------------+
| PvP Tier Media                     |
+------------------------------------+
| Quests Index                       |
+------------------------------------+
| Quest                              |
+------------------------------------+
| Quest Categories Index             |
+------------------------------------+
| Quest Category                     |
+------------------------------------+
| Quest Areas Index                  |
+------------------------------------+
| Quest Area                         |
+------------------------------------+
| Quest Types Index                  |
+------------------------------------+
| Quest Type                         |
+------------------------------------+
| Realms Index                       |
+------------------------------------+
| Realm                              |
+------------------------------------+
| Regions Index                      |
+------------------------------------+
| Region                             |
+------------------------------------+
| Reputation Factions Index          |
+------------------------------------+
| Reputation Faction                 |
+------------------------------------+
| Reputation Tiers Index             |
+------------------------------------+
| Reputation Tiers                   |
+------------------------------------+
| Spell                              |
+------------------------------------+
| Spell Media                        |
+------------------------------------+
| Talents Index                      |
+------------------------------------+
| Talent                             |
+------------------------------------+
| PvP Talents Index                  |
+------------------------------------+
| PvP Talent                         |
+------------------------------------+
| Titles Index                       |
+------------------------------------+
| Title                              |
+------------------------------------+
| WoW Token Index                    |
+------------------------------------+

.. |Build Status| image:: https://github.com/tehmufifnman/BattleMuffin-Python/workflows/BattleMuffin-Python/badge.svg
   :target: https://github.com/tehmufifnman/BattleMuffin-Python/actions
.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black
.. |Coverage Status| image:: https://codecov.io/gh/tehmufifnman/BattleMuffin-Python/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/tehmufifnman/BattleMuffin-Python
