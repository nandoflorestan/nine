# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import unittest


class TestNine(unittest.TestCase):
    def test_import(self):
        from nine import (IS_PYTHON2, str, basestring, integer_types,
            class_types, range, range_list, reraise,
            iterkeys, itervalues, iteritems, map, zip, filter,
            implements_iterator, implements_to_string, implements_repr, nine)
