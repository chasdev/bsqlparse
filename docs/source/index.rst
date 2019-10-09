.. python-bsqlparse documentation master file, created by
   sphinx-quickstart on Thu Feb 26 08:19:28 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-bsqlparse
===============

:mod:`bsqlparse` is a non-validating SQL parser for Python.
It provides support for parsing, splitting and formatting SQL statements.

The module is compatible with Python 2.7 and Python 3 (>= 3.3)
and released under the terms of the `New BSD license
<https://opensource.org/licenses/BSD-3-Clause>`_.

Visit the project page at https://github.com/andialbrecht/bsqlparse for
further information about this project.


tl;dr
-----

.. code-block:: bash

   $ pip install bsqlparse
   $ python
   >>> import bsqlparse
   >>> print(bsqlparse.format('select * from foo', reindent=True))
   select *
   from foo
   >>> parsed = bsqlparse.parse('select * from foo')[0]
   >>> parsed.tokens
   [<DML 'select' at 0x7f22c5e15368>, <Whitespace ' ' at 0x7f22c5e153b0>, <Wildcard '*' … ]
   >>>


Contents
--------

.. toctree::
   :maxdepth: 2

   intro
   api
   analyzing
   ui
   changes
   indices


Resources
---------

Project page
   https://github.com/andialbrecht/bsqlparse

Bug tracker
   https://github.com/andialbrecht/bsqlparse/issues

Documentation
   https://bsqlparse.readthedocs.io/
