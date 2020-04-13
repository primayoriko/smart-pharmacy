"""Testing file

This module is not really a module. Just a script used to test whether the linter is good or nay
This script writes "Testing" into stdout. Just like that
"""
import sys
import sqlite3
sys.path.insert(1, "../src")

import main as main

def test_main() :
    assert main.AppWindow.isInteger("123012") == True
    assert main.AppWindow.isInteger("1230.12") == False
    assert main.AppWindow.isInteger("-123012") == True
    assert main.AppWindow.isInteger("k2was2") == False