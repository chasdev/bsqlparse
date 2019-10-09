.. _analyze:

Analyzing the Parsed Statement
==============================

When the :meth:`~bsqlparse.parse` function is called the returned value
is a tree-ish representation of the analyzed statements. The returned
objects can be used by applications to retrieve further information about
the parsed SQL.


Base Classes
------------

All returned objects inherit from these base classes.
The :class:`~bsqlparse.sql.Token` class represents a single token and
:class:`~bsqlparse.sql.TokenList` class is a group of tokens.
The latter provides methods for inspecting its child tokens.

.. autoclass:: bsqlparse.sql.Token
   :members:

.. autoclass:: bsqlparse.sql.TokenList
   :members:


SQL Representing Classes
------------------------

The following classes represent distinct parts of a SQL statement.

.. autoclass:: bsqlparse.sql.Statement
   :members:

.. autoclass:: bsqlparse.sql.Comment
   :members:

.. autoclass:: bsqlparse.sql.Identifier
   :members:

.. autoclass:: bsqlparse.sql.IdentifierList
   :members:

.. autoclass:: bsqlparse.sql.Where
   :members:

.. autoclass:: bsqlparse.sql.Case
   :members:

.. autoclass:: bsqlparse.sql.Parenthesis
   :members:

.. autoclass:: bsqlparse.sql.If
   :members:

.. autoclass:: bsqlparse.sql.For
   :members:

.. autoclass:: bsqlparse.sql.Assignment
   :members:

.. autoclass:: bsqlparse.sql.Comparison
   :members:

