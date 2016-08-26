""" A module
"""

import collections

def func(foo_):
    """ A function

    Parameters
    ----------
    foo_ : str
        A string
    """
    pass

X = collections.namedtuple(
    'X',
    ('subject', 'from_', 'to', 'body',)
)
