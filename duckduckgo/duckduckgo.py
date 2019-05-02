from __future__ import unicode_literals
from __future__ import absolute_import

from .modules import standard_search

__author__ = "Arthur Barros <arthbarros@gmail.com> "
__version__ = "1.0.0"


"""Defines the public inteface of the API."""

search = standard_search.search

if __name__ == "__main__":
    import doctest
    doctest.testmod()
