#!/usr/bin/python
__author__ = 'Volodimir Duda'

"""
Plans to either use a CommandLine Interface or GUI
"""

import os

fileList = []

def start(dirPath):
    if os.path.exists(dirPath):
        print("Working...")
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                if verifyFile(file):
                    fileList.append(os.path.join(root, file))
    else:
        print("Try again...")
        raise OSError("Directory Not Found!")

def random():
    return False

def verifyFile(file):
    """ Verify correct file to scan; this should be improved in future """
    return file.rfind('.txt') > 0


def populateList():
    return fileList

if __name__ == "__main__":
    start('/Users/vduda/BSUTechDev/FlyDataModifier')
    li = populateList()
    print "Items found: %d"% len(li)
    for i, item in enumerate(li):
        print "%s: %s" % (i+1, item)


