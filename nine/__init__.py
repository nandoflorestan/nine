# -*- coding: utf-8 -*-

'''For documentation, please see the file README.rst.

Here is a checklist of tasks when starting to apply *nine* on Python 2 code:

* Replace str(), usually with nine's native_str() or with bytes()
* Replace unicode() with str() and ``from nine import str``
* Replace __unicode__() with __str__(); apply the *nine* decorator on the class
* Apply the *nine* decorator on classes that define __repr__()

If you had been using *six* or another library before:

* Replace ``string_types`` with ``basestring``
'''

import sys
# Test for Python 2, not 3; don't get bitten when Python 4 comes out:
IS_PYTHON2 = (sys.version_info[0] == 2)
IS_PYPY = hasattr(sys, 'pypy_translation_info')
del sys

if IS_PYTHON2:  # Rename Python 2 builtins so they become like Python 3
    native_str = bytes
    str = unicode
    basestring = basestring
    integer_types = (int, long)
    from types import ClassType
    class_types = (type, ClassType)
    del ClassType
    range_list = range
    range = xrange
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
    from itertools import imap as map, izip as zip, ifilter as filter
else:  # For Python 3, declare these variables so they can be chain imported:
    basestring = native_str = str = str
    integer_types = int
    class_types = type
    range = range
    range_list = lambda *a: list(range(*a))
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())
    filter = filter
    map = map
    zip = zip

if IS_PYTHON2:
    # Turn code into string to avoid SyntaxError on Python 3:
    exec('def reraise(tp, value, tb=None):\n  raise tp, value, tb')
else:
    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value

# ===== Class decorators =====
if IS_PYTHON2:
    def implements_to_string(cls):
        '''Class decorator. You define __str__() and Python 2 gets both
        __unicode__() and __str__().
        '''
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda x: x.__unicode__().encode('utf-8')
        return cls

    def implements_iterator(cls):
        '''Apparently, next() has been renamed to __next__().'''
        cls.next = cls.__next__
        del cls.__next__
        return cls

    def implements_repr(cls):
        '''You implement __repr__() returning a unicode string, and in
        Python 2, I encode it for you.
        '''
        cls.__repr_unicode__ = cls.__repr__

        def wrapper(self):
            return self.__repr_unicode__().encode('utf-8')
        cls.__repr__ = wrapper
        return cls

    def nine(cls):
        '''All the above class decorators in one.'''
        if hasattr(cls, '__str__'):
            cls = implements_to_string(cls)
        if hasattr(cls, '__next__'):
            cls = implements_iterator(cls)
        if hasattr(cls, '__repr__'):
            cls = implements_repr(cls)
        return cls
else:
    implements_to_string = implements_iterator = implements_repr = nine = \
        lambda cls: cls
