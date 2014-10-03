#!/usr/bin/python
__author__ = 'Joe Bruno, Volodimir Duda'

from Interface import Interface
from Core import Modify
import os

print("Running...")
#dirPath = input("Enter DirectoryPath: ")
dirPath = os.path.join(os.path.join(os.path.dirname(__file__)), "samples")
print(dirPath)
Interface.start(dirPath)
fileList = Interface.populateList()
Modify.main(fileList)
print("Done!")
