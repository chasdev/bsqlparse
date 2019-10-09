python-bsqlparse - Parse PLSQL statements
======================================

bsqlparse is a PLSQL parser module for Python.

|buildstatus|_
|coverage|_


Install
-------

From pip, run::

    $ pip install git+https://github.com/yoyoasa/bsqlparse.git

Consider using the ``--user`` option_.

.. _option: https://pip.pypa.io/en/latest/user_guide/#user-installs

From the repository, run::

    python setup.py install

to install python-bsqlparse on your system.

python-bsqlparse is compatible with Python 2.7 and Python 3 (>= 3.3).


Run Tests
---------

To run the test suite run::

    tox

Note, you'll need tox installed, of course.


python-bsqlparse is licensed under the BSD license.

Parts of the code are based on pygments written by Georg Brandl and others.
pygments-Homepage: http://pygments.org/

.. |buildstatus| image:: https://secure.travis-ci.org/andialbrecht/bsqlparse.png?branch=master
.. _buildstatus: http://travis-ci.org/#!/ammaradil/bsqlparse
.. |coverage| image:: https://coveralls.io/repos/andialbrecht/bsqlparse/badge.svg?branch=master&service=github
.. _coverage: https://coveralls.io/github/ammaradil/bsqlparse?branch=master
