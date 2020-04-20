"""Testing file

This module is not really a module. Just a script used to test whether the linter is good or nay
This script writes "Testing" into stdout. Just like that
"""
import sys
import sqlite3
sys.path.insert(1, "../src")

import package.add_module as addModule

def test_add() :
    assert addModule.add(0) == 1
    assert addModule.add(100) == 101
    assert addModule.add("Not a number") == False