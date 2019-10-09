#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Andi Albrecht, albrecht.andi@gmail.com
#
# This module is part of python-bsqlparse and is released under
# the BSD License: https://opensource.org/licenses/BSD-3-Clause

"""Entrypoint module for `python -m bsqlparse`.

Why does this file exist, and why __main__? For more info, read:
- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

import sys

from bsqlparse.cli import main

if __name__ == '__main__':
    sys.exit(main())
