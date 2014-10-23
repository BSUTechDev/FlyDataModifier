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
        files = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath,f))]
        for f in files:
            f = os.path.join(dirPath, f)
            if verifyFile(f):
                fileList.append(f)
    else:
        print("Try again...")
        raise OSError("Directory Not Found!")

def random():
    return False

def verifyFile(file):
    """ Verify correct file to scan; this should be improved in future 
        Would be better to check MIME types
        And check number of lines contained in File
    """
    return file.rfind('.txt') > 0


def populateList():
    return fileList

if __name__ == "__main__":
    start('/Users/vduda/BSUTechDev/FlyDataModifier/test')
    li = populateList()
    print "Items found: %d"% len(li)
    for i, item in enumerate(li):
        print "%s: %s" % (i+1, item)


