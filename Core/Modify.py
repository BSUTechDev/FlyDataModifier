import string
import os
import shutil
import errno

"""
Multiline comments - usually used to describe overview of python script
"""

__author__ = 'Joe Bruno, Volodimir Duda'

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
        try:
            # copy file contents to a similar file
            newFileName = fileLoc[:fileLoc.rfind('.txt')] + ".awd"
            newFilePath = os.path.join(dirPath,os.path.basename(newFileName))
            print "New File name: %s" %newFilePath
            shutil.copy2(fileLoc,newFilePath)

            # Open file in read/write mode
            reader = open(fileLoc, "r+")

            # Old header is first 4 lines
            contents = reader.readlines()

            # Verify we have a header; else pass
            if len(contents) < 5:
                pass
            oldHeader = contents[:4]

            newHeader = constructNewHeader(oldHeader)
            if newHeader == None:
                pass

            writer = open(newFilePath, "w")
            for line in newHeader:
                writer.write(line)

            for line in contents[4:]:
                writer.write(line)

            writer.close()
            reader.close()
        except:
            print "Some error occurred."


def constructNewHeader(xData):
    # Read first line in the list
    nameSpaceSep = xData[0].find(" ")
    if nameSpaceSep == -1:
        return None
    xName = xData[0][:nameSpaceSep].strip()
    xDate = formatDate(xData[0][nameSpaceSep:].strip())

    # Setting the base at a minimum
    xAge = 50

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
                             # imagine if 'clear' was 'rm -rf /' ...



def formatDate(oldDate):
    # Add the dashes
    return oldDate.replace(" ", "-")

def formatTime(oldTime): 
    # This should be replaced with the DateTime library
    # Add a colon and trailing zero's
    return oldTime[0:2] + ":" + oldTime[2:4] + ":00"

if __name__ == "__main__":
    main(isModule=False)
