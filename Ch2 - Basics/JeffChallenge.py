'''This is my attempt at the Chapter 2 Challenge'''

def isPalendrome(mystr):
    if mystr == mystr[::-1]:
        return True
    return False

run = True
while(run):
    testStr = input('Enter a string for the pallendrome test or enter \'exit\':')

    # If user types in exit, then exit the program
    if testStr == 'exit':
        run = False
        break

    # Convert the string to all lower case
    testStr = testStr.lower()

    # Strip out any spaces or punctuation from testStr
    newstr = ''
    for x in testStr:
        if x.isalnum():
            newstr += x

    print('Palendrode test:', isPalendrome(newstr))