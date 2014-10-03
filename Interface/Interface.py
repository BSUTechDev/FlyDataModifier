#!/usr/bin/python
__author__ = 'Volodimir Duda'

"""
Plans to either use a CommandLine Interface or GUI
"""

import os

def start(dirPath):
    if os.path.exists(dirPath):
        print("Working...")
    else:
        print("Try again...")
        raise OSError("Directory Not Found!")


def populateList():
    return []


