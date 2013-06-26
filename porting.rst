When you are starting to apply *nine* on Python 2 code to achieve Python 3
compatibility, you can start by following this list of tasks. It isn't
exhaustive, just a good start:

* Replace str(), usually with nine's native_str() or with bytes()
* Replace unicode() with str() and ``from nine import str``
* Replace __unicode__() with __str__(); apply the *nine* decorator on the class
* Apply the *nine* decorator on classes that define __repr__()
* Search for *range* and replace with nine's *range* or *range_list*
* Where performance matters, replace d.keys() or d.iterkeys()
  with nine's *iterkeys(d)*
* Where performance matters, replace d.values() or d.itervalues()
  with nine's *itervalues(d)*
* Where performance matters, replace d.items() or d.iteritems()
  with nine's *iteritems(d)*
* Where performance matters, replace map(), zip() and filter() with
  nine's versions (which always return iterators).

If you had been using *six* or another library before:

* Replace ``string_types`` with nine's ``basestring``
