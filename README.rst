nine
====

When the best Python 2/Python 3 compatibility libraries -- especially
the famous *six* library invented by Benjamin Peterson --
were invented, they were written from the point of view of a Python 2
programmer starting to grok Python 3.

It is 2013.

Python 3.3 is here.

When thou writeth Python, thou shalt write Python 3 and, just for a while,
ensure that the thing worketh on Python 2.7 and, possibly, even 2.6.

Just before Python 2 is finally phased out, thine codebase shall
look more like 3 than like 2.

*nine* facilitates this new point of view.

For instance, you don't type ``unicode`` anymore, you type ``str``, and *nine*
makes ``str`` point to ``unicode`` on Python 2 (if you use our boilerplate).
Also, ``map``, ``zip`` and ``filter`` have Python 3 behaviour, on Python 2,
meaning they return iterators, not lists.

The author(s) of *nine* donate this module to the public domain.

To understand most of the intricacies involved in porting your code from
Python 2 to Python 3, I recommend reading this:
http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/

Using nine
==========

In your code, start by importing Python 3 behaviours from __future__.
Then import variables from *nine*, as per this boilerplate::

    # -*- coding: utf-8 -*-
    from __future__ import (absolute_import, division, print_function,
                            unicode_literals)
    from nine import (IS_PYTHON2, str, basestring, integer_types,
        class_types, range, range_list, reraise,
        iterkeys, itervalues, iteritems, map, zip, filter,
        implements_iterator, implements_to_string, implements_repr, nine)

If you need *pickle*, import it like this::

    try:
        import cPickle as pickle  # Python 2.x
    except ImportError:
        import pickle

Want StringIO? I recommend you build lists instead. But if you really need it::

    if IS_PYTHON2:
        from cStringIO import StringIO as BytesIO, StringIO
        NativeStringIO = BytesIO
    else:
        from io import BytesIO, StringIO
        NativeStringIO = StringIO

The coverage of Python version differences isn't exhaustive and maybe the
solutions aren't optimal, but contributions are welcome.
