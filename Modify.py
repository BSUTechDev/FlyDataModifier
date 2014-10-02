import string
import os

__author__ = 'Joe Bruno'

def main():
    # To be the list of all found files in need of modification
    fileList = ['/Users/joe/Desktop/FDMTesting/MyRunM001C01.txt']

    modFiles(fileList)

def modFiles(fileLocList):
    # Loop through each file
    for fileLoc in fileLocList:
        # Open file in read/write mode
        xFile = open(fileLoc, "r+")

        # Old header is first 45 bytes
        oldHeader = xFile.readlines(45)

        newHeader = constructNewHeader(oldHeader)

        # Datapoint start
        xFile.seek(40)

        # Read the rest of the file
        fileContent = xFile.read()

        # Start of file
        xFile.seek(0)

        # Write new header
        xFile.write(newHeader)

        # Write the data
        xFile.write(fileContent)

        # Close the handle
        xFile.close()

        # New file name
        removedExtension = fileLoc[:-3] + "awd"

        # Change the file extension
        os.rename(fileLoc, removedExtension)

def constructNewHeader(xData):
    # Read first line in the list
    xName = xData[0][0:13]
    xDate = formatDate(xData[0][15:26])

    # Setting the base at a minimum
    xAge = 1

    # 4th line has time
    xTime = formatTime(xData[3])

    # Epoch Value
    xEpoch = calculateEpoch(xData[2])

    # Set to female by default
    xGender = "F"

    # Build the new header and return it
    newHead = xName + "\n" + xDate + "\n" + xTime + "\n" + str(xEpoch) + "\n" + str(xAge) + "\n\n" + xGender
    return newHead

def calculateEpoch(numMin):
    return (eval(numMin) * 60) // 15

def formatDate(oldDate):
    # Add the dashes
    return oldDate.replace(" ", "-")

def formatTime(oldTime):
    # Add a colon and trailing zero's
    return oldTime[0:2] + ":" + oldTime[2:4] + ":00"

main()