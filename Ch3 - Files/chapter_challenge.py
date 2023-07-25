'''Chapter 3 challenge.  Create a python script that with get the file contents
of a directory and then: 
1: Create a folder named results
2: Create a text file name results.txt
3: In the results file give the sum (in bytes) of all the files in the directory
4: List all of the files found in the directory'''

import os
from os import path

def main():

    workingDir = str(os.path.abspath(os.getcwd()))
    myDir = ''
    tBytes = 0
    if path.exists(workingDir + '/results') is False:
       myDir = str(os.mkdir(workingDir + '/results'))
    
    # myDir = str(os.mkdir(workingDir + '/results'))
    os.chdir('results')
    myFile = open('results.txt', 'w+')

    os.chdir("..")
    dirlist = os.listdir()
    dirlist.sort()

    for entry in dirlist:
    # make sure it's a file!
        if os.path.isfile(entry):
            # add the file size to the total
            filesize = os.path.getsize(entry)
            tBytes += filesize

    # Write explanitory text into results.txt
    myFile.write("Total bytecount:" + str(tBytes) + "\n")
    myFile.write("Files list:\n")
    myFile.write("--------------\n")
    # write the results into the file
    for entry in dirlist:
        if os.path.isfile(entry):
            # write the file name to the results ledger
            myFileSize = str(os.path.getsize(entry))
            myFile.write(entry + ": " + myFileSize + " bytes.\n")

    # close the file when done
    myFile.close()













if __name__ == "__main__":
    main()
