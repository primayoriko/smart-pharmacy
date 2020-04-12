"""Add module

A module that contains about a single add function.
Returns number after added by one.
"""
from __future__ import print_function
import numbers

def add(_x):
    """Add function

    Takes one argument, returns the number added by one if it's a number
    Returns false if it's not a number"""
    if isinstance(_x, numbers.Number):
        return _x + 1
    return False
