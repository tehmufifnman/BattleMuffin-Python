Changelog
*********

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_, and this project adheres to the
`Semantic Versioning`_ scheme.

0.1.10 - Unreleased
===================

0.1.9 - 2020-07-02
==================
Updated
- Updated retry logic to retry on all verbs, not just default idempotent ones

0.1.8 - 2020-07-02
==================
Updated
- Failed to mount HTTPS for retries in previous versions

0.1.7 - 2020-07-02
==================
Updated
- Blizzard API has a habit of aborting connections. BattleMuffin will now retry when this happens

0.1.6 - 2020-05-03
==================
Added

- Created ``get_auctions_raw_response(connectedRealmId)`` endpoint for returning the
  raw auctions response so headers can be analyzed.
- Created ``get_auctions_if_modified_since(connectedRealmId, if_modified_since)``
  endpoint for returning raw auctions response if the ``Last-Modified`` header is after a given date.
  This date must adhere to the standard format ``"%a, %d %b %Y %H:%M:%S %Z"``.  If the data is not modified,
  a ``304`` status code will be returned.


.. General Links
.. _`Keep a Changelog`: http://keepachangelog.com/en/1.0.0/
.. _`Semantic Versioning`: https://packaging.python.org/tutorials/distributing-packages/#semantic-versioning-preferred
