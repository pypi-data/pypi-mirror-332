What are human readable timedeltas?
===============================================

The ``ago.py`` module makes customizable human readable timedeltas. For example:

Testing past tense::

   Russell commented 1 year, 127 days, 16 hours ago
   You replied 1 year, 127 days ago

Testing future tense::

   Program will shutdown in 2 days, 3 hours, 27 minutes
   Job will run 2 days, 3 hours from now


Installation
============

There are a number of ways to install this package.

You could run this ad hoc command::

   pip install ago

or specify *ago* under the *setup_requires* list within your
`setuptools <https://setuptools.readthedocs.io>`_-compatible project's ``setup.py`` file.


How to Use
==========

The ``ago`` module comes with the following functions:

1. ``human``: Convert a datetime or timedelta to a human-readable string
2. ``delta2dict``: Convert a timedelta to a dictionary of units
3. ``extract_components``: Extract time components from a timedelta (builds on delta2dict)
4. ``format_components``: Format time components into a readable string
5. ``get_delta_from_subject``: Convert various input types to a timedelta

Basic Usage
-----------

The primary function you'll use is ``human``:

.. code-block:: python

   from ago import human
   from datetime import datetime, timedelta

   # With a datetime object
   db_date = datetime(year=2010, month=5, day=4, hour=6, minute=54, second=33)
   print('Created ' + human(db_date))  # "Created X years, Y months ago"

   # With a timedelta object
   delta = timedelta(days=5, hours=3, minutes=45)
   print('Due in ' + human(delta))  # "Due in 5 days, 3 hours"


Function Arguments
------------------

The ``human`` function accepts the following arguments:

.. code-block:: python

   human(subject, precision=2, past_tense='{} ago', future_tense='in {}', abbreviate=False)

**subject**
   A datetime, timedelta, or timestamp (integer/float) object to be converted to a human-readable string.

**precision** (default: 2)
   The desired amount of unit precision.

**past_tense** (default: ``'{} ago'``)
   The format string used for a past timedelta.

**future_tense** (default: ``'in {}'``)
   The format string used for a future timedelta.

**abbreviate** (default: False)
   Boolean flag to abbreviate units.


Examples
--------

Basic usage with different precisions:

.. code-block:: python

   from ago import human
   from datetime import datetime

   # Pretend this was stored in a database
   db_date = datetime(year=2010, month=5, day=4, hour=6, minute=54, second=33)

   # To find out how long ago, use the human function
   print('Created ' + human(db_date))  # "Created X years, Y months ago"

   # Optionally pass a precision
   print('Created ' + human(db_date, 3))  # Shows 3 units (e.g., years, months, days)
   print('Created ' + human(db_date, 6))  # Shows up to 6 units

Future dates and times:

.. code-block:: python

   from ago import human
   from datetime import datetime, timedelta

   PRESENT = datetime.now()
   FUTURE = PRESENT + timedelta(days=2, seconds=12447, microseconds=963)

   print(human(FUTURE))  # "in 2 days, 3 hours"

Custom format strings:

.. code-block:: python

   from ago import human
   from datetime import datetime, timedelta

   PRESENT = datetime.now()
   PAST = PRESENT - timedelta(days=492, seconds=58711, microseconds=45)
   FUTURE = PRESENT + timedelta(days=2, seconds=12447, microseconds=963)

   output1 = human(
       PAST,
       past_tense='titanic sunk {} ago',
       future_tense='titanic will sink in {} from now'
   )
   # "titanic sunk 1 year, 127 days ago"

   output2 = human(
       FUTURE,
       past_tense='titanic sunk {} ago',
       future_tense='titanic will sink in {} from now'
   )
   # "titanic will sink in 2 days, 3 hours from now"

Using abbreviations:

.. code-block:: python

   from ago import human
   from datetime import timedelta

   print(human(timedelta(days=5, hours=3, minutes=45), abbreviate=True))
   # "5d, 3h ago"


Advanced Usage
--------------

For more advanced use cases, you can utilize the other functions.

Getting a dictionary of time units:

.. code-block:: python

   from ago import delta2dict
   from datetime import timedelta

   delta = timedelta(days=400, hours=5, minutes=30)
   time_dict = delta2dict(delta)
   # Returns {"year": 1, "day": 35, "hour": 5, "minute": 30, "second": 0, ...}

Extracting non-zero time components:

.. code-block:: python

   from ago import extract_components
   from datetime import timedelta

   delta = timedelta(days=400, hours=5, minutes=30)
   components = extract_components(delta)
   # Returns a list of components:
   # [{"unit": "year", "abbr": "y", "value": 1},
   #  {"unit": "day", "abbr": "d", "value": 35}, ...]

Formatting time components:

.. code-block:: python

   from ago import extract_components, format_components
   from datetime import timedelta

   delta = timedelta(days=400, hours=5, minutes=30)
   components = extract_components(delta)
   formatted = format_components(components, precision=3, abbreviate=True)
   # "1y, 35d, 5h"


More Examples
-------------

For additional examples, please refer to the file ``test_ago.py``.

Acknowledgements
----------------

**How do I thank you?**

Follow me on Twitter: `@russellbal <http://twitter.com/russellbal>`_.

License
-------

This project is in the Public Domain.

Revision Control
----------------

The public revision control repository is available at: `https://git.unturf.com/python/ago <https://git.unturf.com/python/ago>`_.
