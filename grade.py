from os import *
import sys

def getListOfFiles(dirName):
    listOfFile = listdir(dirName)
    allFiles = []
    # Iterate over all the entries
    for entry in listOfFile:
        fullPath = path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory.
        if path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif fullPath.endswith(".java"):
            allFiles.append(fullPath)
                
    return allFiles

# Get path to submissions and clean up if necessary.
submissions_path = input("\nEnter the path to the folder in which the student submissions are contained: ").strip()
if (submissions_path[0] == "'" and submissions_path[-1] == "'") or (submissions_path[0] == '"' and submissions_path[-1] == '"'):
    submissions_path = submissions_path[1:-1]

# Check if containing folder exists.
if not path.exists(submissions_path):
    sys.exit("\n{} is not a valid path.".format(submissions_path))

# Check if the folder is empty. 
if len(listdir(submissions_path)) == 0:
    sys.exit("\n{} is empty.".format(submissions_path))

print(getListOfFiles(submissions_path))

