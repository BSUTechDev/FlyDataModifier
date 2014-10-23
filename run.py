#!/usr/bin/python
__author__ = 'Joe Bruno, Volodimir Duda'

from Interface import Interface
from Core import Modify
import os, argparse

print("Running...")
parser = argparse.ArgumentParser(description="""
	Scan a directory for the purposes of converting FlyData generated
	using Perl scripts into an appropriate format. The Data is located within
	txt based files, but we need this data converted into the awd format along
	with internal data modifications to each file itself. 
	""")
parser.add_argument('loc', metavar="LOCATION", help="Location path to be scanned for text files")
args = parser.parse_args()
dirPath = args.loc
# Uncomment next line for testing purposes and/or uncomment line above
#dirPath = os.path.join(os.path.join(os.path.dirname(__file__)), "samples")
print(dirPath)
Interface.start(dirPath)
fileList = Interface.populateList()
Modify.main(fileList)
print("Done!")
