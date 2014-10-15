#!/usr/bin/python
__author__ = 'Volodimir Duda'

"""
Plans to either use a CommandLine Interface or GUI
"""

import os



def start(dirPath):
    if os.path.exists(dirPath):
        print("Working...")
        for root, dirs, files in os.walk(dirPath):

    else:
        print("Try again...")
        raise OSError("Directory Not Found!")

 def verifyFile(file):
 	""" Verify correct file to scan; this should be improved in future """
 	return file.rfind('.txt') > 0


def populateList():
    return []


