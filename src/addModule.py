"""Add module

A module that contains about a single add function.
Returns number after added by one.
"""
import numbers

def add(x) :
    if (isinstance(x, numbers.Number)) :
        return x + 1
    else :
        return False
