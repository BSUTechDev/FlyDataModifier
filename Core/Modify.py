import string
import os
import shutil
import errno

"""
Multiline comments - usually used to describe overview of python script
"""

__author__ = 'Joe Bruno'

def main(fileList = None, searchPath=None, isModule = True):
    # To be the list of all found files in need of modification
    # li = fileList
    # print "Items found: %d"% len(li)
    # for i, item in enumerate(li):
    #     print "%s: %s" % (i+1, item)
    if not fileList and isModule:
        raise AttributeError('No Files were passed in!')

    if not isModule:
        # variables used to help with testing - can keep hitting run without any damage
        # This portion will probably be moved elsewhere - just quick to do it here
        rootDir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        sampleDir = "samples"
        testDir = "test"
        testFile = "MyRunM001C01.txt"
        sampleFilePath = os.path.join(rootDir, sampleDir, testFile)
        testDirPath = os.path.join(rootDir, testDir)
        testFilePath = os.path.join(rootDir, testDir, testFile)

        shutil.copyfile(sampleFilePath, testFilePath) # copy sample to test directory
        os.remove(os.path.join(rootDir, testDir, testFile[:testFile.rfind('.')]+'.awd'))
        print("Testing with File: %s" % testFilePath)
        searchPath = testDirPath
        fileList = [testFilePath]
    dirPath = os.path.join(searchPath,"output-awd")
    mkdir_P(dirPath)
    modFiles(fileList, dirPath)

def mkdir_P(directory_name):
    try:
        os.makedirs(directory_name)
    except OSError as exc:     
        pass

def modFiles(fileLocList, dirPath):
    # Loop through each file
    for fileLoc in fileLocList:
        # copy file contents to a similar file
        newFileName = fileLoc[:-3] + "awd"
        newFilePath = os.path.join(dirPath,os.path.basename(newFileName))
        print(newFilePath)
        shutil.copy2(fileLoc,newFilePath)


        # Open file in read/write mode
        xFile = open(newFilePath, "r+")

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

        # Change the file extension
        #os.rename(fileLoc, removedExtension)
        # do this operation at the start as to leave original file in tact. 


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
    newHead = xName + "\n" + xDate + "\n" + xTime + "\n" + str(xEpoch) + "\n" + str(xAge) + "\n\n" + xGender +"\n"
    return newHead

def calculateEpoch(numMin):
    return (int(numMin) * 60) // 15 # Who keeps forcing you guys to use eval lol - use casting instead
                             # you can delete your whole file system if numMin = "__import__('os').system('clear')"



def formatDate(oldDate):
    # Add the dashes
    return oldDate.replace(" ", "-")

def formatTime(oldTime):
    # Add a colon and trailing zero's
    return oldTime[0:2] + ":" + oldTime[2:4] + ":00"

if __name__ == "__main__":
    main(isModule=False)