import string

__author__ = 'Joe Bruno'

def main():
    # To be the list of all found files in need of modification
    fileList = ['/Users/joe/Desktop/FDMTesting/MyRunM001C01.txt']

    modFiles(fileList)

def modFiles(fileLocList):
    # Loop through each file
    for fileLoc in fileLocList:
        xFile = open(fileLoc, "r+")

        # Old header is first 45 bytes
        oldHeader = xFile.readlines(45)

        newHeader = constructNewHeader(oldHeader)


def constructNewHeader(xData):
    # Read first line in the list
    xName = xData[0][0:13]
    xDate = formatDate(xData[0][15:26])


def formatDate(oldDate):
    return oldDate.replace(" ", "-")

main()